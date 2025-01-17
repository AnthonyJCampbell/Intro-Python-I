"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

cal = calendar.TextCalendar()
now = datetime.now()

# input
choice = input("Enter a month (1-12) and year, separated by a comma: ").split(',')

# if no input, print current month through datetime
if (len(choice[0]) == 0):
  print(cal.formatmonth(now.year, now.month))

# if one arg, second param defaults to current year and logs the calendar for that month
elif (len(choice) == 1):
  print(cal.formatmonth(2019, int(choice[0])))

# if two args, assume it's in [month][year] format, print that calendar
elif (len(choice) == 2):
  print(cal.formatmonth(int(choice[1]), int(choice[0])))

# else (in case of unexpected args) print an error message
else:
  print("Please provide an input that follows the format of `(1-12), (yyyy)` ")


