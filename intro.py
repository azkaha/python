# REFRESHING BASIC PYTHON CONCEPTS
message = 'Hello World' # you can use single or double quote for string but depends on text 
print(message[0:5])
print(message.lower())
print(message.count('l'))

newmessage = message.replace('World', 'Universe')
print(newmessage)

# print((dir(newmessage)))

course = ['Maths', 'Physics', 'Chem', 'CompSci']

#  Basic For Loops 

for item in course:
    print(item)
for index, item in enumerate(course, start =1):
    print(index, item)

# Functions

def findindex(to_search, target):
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1

#  Variable Scopes & LEGB Rule
import builtins

def myMin(z):
    pass

m = min([5,6,4,3,2])

print(m)
# x = 'global x'
def outer():
    x = 'outer x'
    
    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)
outer()

#  Sorting & Slicing Lists 

a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print (a_list[-2:2:-2])
print (a_list[::-1]) #reverse list

sample = "whattt"
print (sample[4:])

nums = [1,2,3,4,5,6,7,8,9,10]

# my_list= [n for n in nums]
my_list = []
for n in nums:
    my_list.append(n*n)
    
print (my_list)

my_list = list(filter(lambda n: n%2 ==  0, nums))
print (my_list)

#  OS Module

import os

print (dir(os))
print (os.getcwd())

#  Date & Time

import datetime
d = datetime.date(2016,7,24)

v = datetime.date.today()
print(d)

print(v.day)

print(v.isoweekday())

tdelta = datetime.timedelta(days = 7)

print (v - tdelta)

bday = datetime.date(2024,7,18)
till_bday = bday - v
print(till_bday.total_seconds())


import pytz


dt = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

umm = datetime.timedelta(hours =12)
# dt_now = datetime.datetime.now(tz=ptyz.UTC)

for tz in pytz.all_timezones:
    print(tz)

# File Handling

# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line, end ='')

# with open('test.txt', 'r') as f:
#     for line in f:
#         print(line, end ='')
    
#     size_to_read = 10
#     f_contents = f.read(size_to_read)
#     while len(f_contents) > 0:
#         print(f_contents, end = '*')
#         f_contents = f.read(size_to_read)

# print(f.closed())

# f = open('text.txt', 'r')

# Random Numbers

import random
greetings = ['Hello', 'Hi', 'What']

results = random.choices(greetings, k = 10)
print (results)

#  Try/Except Blocks for Error Handling
try:
    f = open('testfile.txt')
except FileNotFoundError as e:
    print (e)
except Exception:
    print ("Doesn't Exist. Smthn went wrong")

# if__name__ = '__main__' Tut
print ("First Module's Name: {}".format(__name__))
def main():
    pass

if __name__ == '__main__':
    main()

#  Duck Typing

class Duck:
    def quack(self):
        print("Quack, Quack")

    def fly(self):
        print("Flap, Flap")

class Person:
    def quack(self):
        print("I'm Quacking smthn smthn")
    
    def fly(self):
        print("I'm Flapping smthn smthn")

def quackandfly(thing):
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()

d = Duck()
quackandfly(d)

p = Person()
quackandfly(p)

# Classes 

class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
        
employee1 = Employee('Azkah', 'Sjsk', 5000)
employee2 = Employee('Test', 'User', 49493)

employee1.fullname()
print(Employee.fullname(employee1))

# Working with JSON Data
# import json

# data= json.loads(people_string)

# Image Processing with Pillow
from PIL import Image

image1 = Image.open('dog8.jpg')
image1.show()

image1.convert(mode='L'.save('dog8_mod.jpg'))

