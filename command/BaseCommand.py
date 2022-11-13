import text_to_speech


class BaseCommand:

    engine = None

    def __init__(self, wake_command):
        self.wake_command = wake_command

    def exec_command(self, command):
        text_to_speech.talk("This command does not yet have any functionality", BaseCommand.engine)
