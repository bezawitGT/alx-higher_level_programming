#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg = ' and is less than 6 and not 0'
pos = ' and is greater than 5'
if (number >= 0):
    last = number % 10
else:
    last = number % 10
if (last > 5):
    print('Last digit of ' + str(number) + ' is ' + str(last) + pos)
elif (last == 0):
    print('Last digit of ' + str(number) + ' is ' + str(last) + ' and is 0')
else:
    print('Last digit of ' + str(number) + ' is ' + str(last) + neg)
