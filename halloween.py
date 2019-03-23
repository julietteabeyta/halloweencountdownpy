from datetime import date
import time

# using time to grab certain components of the current date
currDay = int (time.strftime('%e'))
currMon = int (time.strftime('%m'))
currYr = int (time.strftime('%Y'))

print currDay, currMon, currYr

currDate = date(currYr, currMon, currDay)

# here we are just going to set the year based on 
# whether halloween has passed or not
if currMon < 10:
  hallowDay = date(currYr, 10, 31)
else:
  hallowDay = date(currYr+1, 10, 31)

print hallowDay

# aaaand now we are going to have the dates
# calculate the distance between themselves!
delta = hallowDay - currDate

print delta

if delta.days == 0:
  print 'BOO!'
else:
  print 'There are ' + str (delta.days) + ' days until Halloween!'