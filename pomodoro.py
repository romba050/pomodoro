#!/usr/bin/env python3

# this was taken from:
# https://twitter.com/clcoding/status/1736518886663864445

# in order to run this script, do:
# $ venv pomodoro
# $ ./pomodoro.py
# import dbus # https://en.wikipedia.org/wiki/D-Bus
import time 
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Pomodoro",
            message="Take a break, it's been !",
            timeout = 10 # Alert closes after 10s
            )
        waiting_time = 15 # for 1h, take 60 minutes of 60 seconds each
        time.sleep(waiting_time)  
