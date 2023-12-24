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

    working_time_min = int(input('Enter the amount of working minutes (e.g. 25):'))
    break_time_min = int(input('Enter the amount of break minutes (e.g. 5):'))

    working_time_s = 10#working_time_min*60 # for 1h, take 60 minutes of 60 seconds each = 3600
    break_time_s = 10#break_time_min*60 # for 1h, take 60 minutes of 60 seconds each = 3600

    pync.notify("Pomodoro Timer started.", 
                title="Pomodoro 🍅", # macos: crtl + cmd + space for emoji picker 
                timeout=20)
    while True:
        time.sleep(working_time_s)        
        pync.notify(f"{working_time_min} minutes are up. Time for a {break_time_min} min break.", 
                    title="Pomodoro 🍅", # macos: crtl + cmd + space for emoji picker 
                    timeout=20) # Alert closes after 10s
        # TODO: somehow only the  notification about starting the break is displyed, not the one below, about ending the break
        time.sleep(break_time_s)
        pync.notify("{break_time_min} min break is up.", 
            title="Pomodoro 🍅", # macos: crtl + cmd + space for emoji picker 
            timeout=20)      

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