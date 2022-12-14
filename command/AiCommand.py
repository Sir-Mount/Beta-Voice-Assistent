from pathlib import Path

import text_to_speech
from command.BaseCommand import BaseCommand

import openai

# Load your API key from an environment variable or secret management service
openai.api_key_path = Path('OPENAI_API_KEY')

class AiCommand(BaseCommand):

    def exec_command(self, command):
        response = openai.Completion.create(model="text-davinci-003", prompt=command, temperature=1, max_tokens=500)
        answer = response.choices[0].text

        print(answer)
        text_to_speech.talk(answer, BaseCommand.engine)
