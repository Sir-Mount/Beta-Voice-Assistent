from vosk import Model, KaldiRecognizer
import pyaudio
import text_to_speech

import openai

from command.BaseCommand import BaseCommand
from command import PlayCommand, \
    WikiCommand, \
    ShutDownCommand, \
    JokeCommand, \
    TimeCommand, \
    DateCommand, \
    RunCommand, \
    AiCommand

en_model = Model(r'C:\Users\aron\PycharmProjects\pythonProject\VoskModels\vosk-model-small-en-us-0.15')
recognizer = KaldiRecognizer(en_model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

engine = text_to_speech.setup_tts()

BaseCommand.engine = engine

action_commands = [PlayCommand.PlayCommand("play"),
                   RunCommand.RunCommand("run")]

info_commands = [WikiCommand.WikiCommand("look up"),
                 AiCommand.AiCommand("ask"),
                 JokeCommand.JokeCommand("joke"),
                 TimeCommand.TimeCommand("time"),
                 DateCommand.DateCommand("day")]

control_commands = [ShutDownCommand.ShutDownCommand("stop")]

command_categories = [action_commands, info_commands, control_commands]

wake_word = "beta"


def get_input():
    data = stream.read(4896, exception_on_overflow=False)

    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        text = text[14:-3]

        return text


def run_beta():
    text = get_input()
    if text is not None:
        if wake_word in text:
            text = text.split(wake_word, 1)
            if len(text) == 2:
                if text[1] == '':
                    command = text[0]
                else:
                    command = text[1]

                print(command)
                exec_command = False

                for category in command_categories:
                    for command_obj in category:
                        if exec_command is False:
                            if command_obj.wake_command in command:
                                command = command.split(command_obj.wake_command, 1)
                                command = command[1]

                                command_obj.exec_command(command)
                                exec_command = True
            else:
                print("there was no command")
        else:
            print("there was no command")


while True:
    run_beta()
