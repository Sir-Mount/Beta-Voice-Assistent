import text_to_speech
from command.BaseCommand import BaseCommand


class ShutDownCommand(BaseCommand):

    def exec_command(self, command):
        text_to_speech.talk("Now shutting down, good night", BaseCommand.engine)
        exit()
