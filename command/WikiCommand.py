import wikipedia
from command.BaseCommand import BaseCommand
import text_to_speech


class WikiCommand(BaseCommand):

    def exec_command(self, command):
        try:
            text = wikipedia.summary(command, sentences=2, auto_suggest=True, redirect=True)
            text_to_speech.talk("This is what i found on  " + command, BaseCommand.engine)
        except wikipedia.exceptions.PageError:
            text = "I could not find anything on" + command

        print(text)
        text_to_speech.talk(text, BaseCommand.engine)
