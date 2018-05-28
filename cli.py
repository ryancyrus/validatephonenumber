#!/usr/bin/env python

import re
import datetime
import time
import sys, select, os

def validatePhoneNumber():
    number = input("Please enter a valid phone number:")
    if number == "":
        print("No input was given.")
    else:
        phoneNumberRegularExpression = re.compile('\d{3}-\d{3}-\d{4}')
        validate = phoneNumberRegularExpression.match(number)
        if validate:
            print("This is a valid phone number.")
        else:
            print("This is not a valid phone number.")

def main():
    delta = datetime.timedelta(seconds=1)
    nextTime = datetime.datetime.now()
    while True:
        print(nextTime.strftime("%Y-%m-%d" + "T" + "%H:%M:%S" + "Z"))
        timeDiffernce = nextTime + delta - datetime.datetime.now()
        time.sleep(timeDiffernce.total_seconds())
        nextTime = nextTime + delta
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            line = input()
            validatePhoneNumber()
            nextTime = datetime.datetime.now()

if __name__ == '__main__':
   main()