import pywhatkit
from command.BaseCommand import BaseCommand
import text_to_speech


class PlayCommand(BaseCommand):

    def exec_command(self, command):
        text_to_speech.talk("Now playing " + command, BaseCommand.engine)
        pywhatkit.playonyt(command)
