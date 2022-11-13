import os

import text_to_speech
from command.BaseCommand import BaseCommand


class RunCommand(BaseCommand):

    def exec_command(self, command):
        command = command[1:]
        path = "C:\\Users\\aron\\Desktop\\" + command
        print(path)

        try:
            os.startfile(path)
            text_to_speech.talk("Now running " + command, BaseCommand.engine)
        except FileNotFoundError:
            text_to_speech.talk("I could not find a program called: " + command, BaseCommand.engine)
