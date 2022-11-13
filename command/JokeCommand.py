import pyjokes
import text_to_speech
from command.BaseCommand import BaseCommand


class JokeCommand(BaseCommand):

    def exec_command(self, command):
        joke = pyjokes.get_joke()
        print(joke)
        text_to_speech.talk(joke, BaseCommand.engine)
