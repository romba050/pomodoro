#!/usr/bin/env python3

# this was taken from:
# https://twitter.com/clcoding/status/1736518886663864445

# in order to run this script, do:
# $ source pomodoro/bin/activate # only uses virtualenv, since the extension virtualenvwrapper is broken
# $ ./pomodoro.py
# For more virtuelenv documentation, see: https://github.com/bbengfort/venv/blob/master/virtualenv_cheatsheet.md

# from plyer import notification
# import dbus # https://en.wikipedia.org/wiki/D-Bus
import time 
import pync

if __name__ == "__main__":
    waiting_time = 10 # for 1h, take 60 minutes of 60 seconds each = 3600

    while True:
        pync.notify("Take a break! It has been an hour.", 
                    title="Pomodoro", 
                    timeout=3) # Alert closes after 10s
        time.sleep(waiting_time)  

# if __name__ == "__main__":
#     while True:
#         notification.notify(
#             title="Pomodoro",
#             message="Take a break, it's been !",
#             timeout = 10 # Alert closes after 10s
#             )
#         waiting_time = 15 # for 1h, take 60 minutes of 60 seconds each
#         time.sleep(waiting_time)  

# if __name__ == "__main__":
#     while True:
#         notification.notify(
#             title = "ALERT!!!",
#             message = "Take a break! It has been an hour!",
#             timeout = 10
#         )
#         time.sleep(3600)
#clcoding.com

## plyer code above gives this stuborn error:
# Traceback (most recent call last):
#   File "/Users/basile/Documents/Programming/pomodoro/pomodoro.py", line 33, in <module>
#     notification.notify(
#   File "/Users/basile/Documents/Programming/pomodoro/pomodoro/lib/python3.12/site-packages/plyer/facades/notification.py", line 84, in notify
#     self._notify(
#   File "/Users/basile/Documents/Programming/pomodoro/pomodoro/lib/python3.12/site-packages/plyer/platforms/macosx/notification.py", line 38, in _notify
#     usrnotifctr.setDelegate_(self)
#     ^^^^^^^^^^^^^^^^^^^^^^^^