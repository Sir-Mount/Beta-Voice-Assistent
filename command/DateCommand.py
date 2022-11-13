from datetime import datetime
import pandas as pd
import text_to_speech
from command.BaseCommand import BaseCommand


class DateCommand(BaseCommand):

    def exec_command(self, command):
        now = datetime.now()
        current_date = now.date()
        current_day = pd.to_datetime(current_date).day_name()

        print("Today is " + current_day + " " + str(current_date))
        text_to_speech.talk("Today is " + current_day + " " + str(current_date), BaseCommand.engine)
