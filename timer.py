import time
from black_screen import black_screen

frequency_in_minutes = 30
seconds_in_a_minute = 60
total_interval_in_seconds = frequency_in_minutes * seconds_in_a_minute

timer_in_seconds = total_interval_in_seconds

break_interval_in_minutes = 2
break_interval_in_seconds = break_interval_in_minutes * seconds_in_a_minute

screen = black_screen()

def seconds_to_mmss(seconds):
    return f"{seconds // seconds_in_a_minute}:{seconds % seconds_in_a_minute}"

while True:
    if timer_in_seconds == 0:
        timer_in_seconds = total_interval_in_seconds
        screen.show_black_screen(break_interval_in_seconds, seconds_to_mmss)
    else:
        timer_in_seconds -= 1
        print(f"\r{' '*10}\r{seconds_to_mmss(timer_in_seconds)}", end = "")
        time.sleep(1)