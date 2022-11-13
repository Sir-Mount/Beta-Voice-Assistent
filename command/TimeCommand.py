from datetime import datetime, time
import text_to_speech
from command.BaseCommand import BaseCommand


def is_now_in_timeperiod(start_time, end_time, now_time):
    if start_time < end_time:
        return start_time <= now_time <= end_time
    else:
        # Over midnight:
        return now_time >= start_time or now_time <= end_time


class TimeCommand(BaseCommand):

    def exec_command(self, command):
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        print("Currently it is " + str(current_time))
        text_to_speech.talk("Currently it is " + str(current_time), BaseCommand.engine)

        if is_now_in_timeperiod(time(1, 00), time(7, 00), now.time()):
            print("Go to bed")
            text_to_speech.talk("Go to bed", BaseCommand.engine)
