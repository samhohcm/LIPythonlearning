#
# Example file for working with date information
#

from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class

  #today = date.today()
  #print("Today's date is ", today)

  # print out the date's individual components
  #print("Date components: ", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  #print("Today's weekday number is: ", today.weekday())
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  #days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
  #print ("Which is a: ", days[today.weekday()])

  # Get the current time
  today = datetime.now()
  print("The current date and time is ", today.now())
  t = datetime.time(datetime.now()) #passes the object from now, pass to time function
  print(t)

  
if __name__ == "__main__":
  main()
  