#!/usr/bin/python3

name = input ("What is your name?")
height = float(input("How tall are you? (In metres)"))
weight = float(input("How heavy are you? (In kg)"))
BMI = weight/(height**2)
print (f"You are {name}. You are {height}m tall and weigh {weight}kg.")
print (f"Your BMI is {BMI}.")
if BMI >25:
    print ("Move it Fatty! Lose some weight!")
else:
    print ("Better keep it that way!")
