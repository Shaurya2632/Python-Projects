from plyer import notification
import time, winsound, sys

def setReminder(timeList: list):

      hour, min, sec = timeList

      while True:

            if hour == min == sec == 0: break

            time.sleep(1)
            sec -= 1

            if sec == -1:
               min -= 1
               sec = 59

            if min == -1:
               hour -= 1
               min = 59

      notification.notify(title = 'Please drink water', app_name = "Drinking water", message = 'Please drink water for '
                                                                                          'your own safety', timeout = 5)
      for _ in range(10):
          winsound.Beep(1050, 500)

      sys.exit()

print("Started Reminder")
setReminder([0, 0, 1])

