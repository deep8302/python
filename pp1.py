#!/usr/bin/python3

import datetime

a=input("what is your name: ")  #taking the input from the user as his/her name 
b=input("what is your age: ")   #taking the input from the user his/her age

c=range(0,96) 
f=datetime.datetime.now()   #
g=f.year

if b in c is True:
	h=(95-b)+g
	print("you will be 95 in the year of "+str(h))
else:
	print("you are already "+str(b)+"years old")










