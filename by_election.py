import count_votes
import datetime

# get current time
now = datetime.datetime.now()

date_string = now.strftime("%d/%m/%Y")

hour = int(now.strftime("%H"))
minute = int(now.strftime("%M"))
am_pm_string = "AM"

if(hour > 12):
    am_pm_string = "PM"
    hour -= 12
else:
    am_pm_string = "AM"

date_string = (str(hour) + ":" + str(minute) + " " + am_pm_string)
print(date_string)
