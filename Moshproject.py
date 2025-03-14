# Full_name = "Jonh Smith"
# age = 20
# Is_new = True
# print(Full_name)
# print("Age", age)
# print("Is_new:", Is_new)
import os

from pyexpat.errors import messages

#Ask tow questions persons name and color and the print "Charmu likes Black"

# name =input("What is your name: ")
# color = input("What is your favourite color: ")
# print( name + " likes " + color)

#Write a program that will require birth year and quickly calculates your age and the print your age on the terminal
#
# Birth_year = input("Enter Birth Year: ")
# age = 2025 - int(Birth_year)
# print( "Age: ", age)

# #Ask the user their weighty  in pounds lbs and then convert it to kilograms kgs and print it on the terminal
# weight_pounds = input( "What is your weighty in pounds?" )
# your_kgs =int(weight_pounds) * 0.45
# print( "Weight:", your_kgs, "kgs" )

# import math
# print(math.ceil(5.6))

# Create a program that runs the following
#If its a hot day
    #its a hot day
    #Drinks lots of water
#Otherwise
    #Its a cold day
    #Wear warm clothes
#Otherwise
    #its a lovely day


# is_hot = False
# is_cold = True
#
# if is_hot:
#      print("Its a hot day")
#      print("Drink lots of water")
# elif is_cold:
#     print("Its a cold day")
#     print("Wear warm clothes")
# else:
#      print("Its a lovely day")

# input temperature for the conditions to work

# day_temp = float(input("What is the temperature today: "))

# Define the conditions
# is_hot = (day_temp > 20)
# is_cold = (day_temp < 15)
# if is_hot:
#      print("Its a hot day")
#      print("Drink lots of water")
# elif is_cold:
#     print("Its a cold day")
#     print("Wear warm clothes")
# else:
#      print("Its a lovely day")

#Price of a house is $1 million dollars.If buyer has a good credit ,they need to put down 10%,
# Otherwise they need to put down 20%.
# Write a programme that will print the down payment.

# # Define conditions
# price = 1000000
# has_good_credit = False
# if has_good_credit:
#     down_payment = price * 0.10
# else:
#     down_payment = price * 0.2
#
# print(f"Downpayment: ${down_payment}")

#Create a weight converter program which allows user to input their weight
# and then the program asks if its pounds or kilos and based on the answer
# it converts and displays the weight witha message
#You are *** Kgs

# Weight = int(input("Enter Weight:"))
# unit = input("(L)bs or (K)g: " )
# if unit.upper() == "L":
#     converted = round(Weight * 0.45,2)
#     print(f"You are:{converted} kilos")
# else:
#     converted = round( Weight / 0.45,2)
#     print(f"You are:{converted} pounds ")

# Use while loop to create a timer that counts from 1 to 5 then prints boooom.
# n = 1
# while n <= 10:
#     print(n)
#     n = n + 1
# print("Boooooom❤❤❤❤💥")

# Create a guessing programme where a user has 3 chances to get a secret number. Once has 3 failed attempts print "Zvaramba".
#If gueses correctly print "Makaipa" and  terminate the loop. Secret code is 7

# secret_code = 7
# guess_count = 07
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = (int(input("Guess : ")))
#     guess_count += 1
#     if guess == secret_code:
#         print("Makaipa")
#         break
# else:
#     print("Zvaramba")

#Build a car game with commands that is just the engine though wthou a Graphic User Interface GUI.

# command = ""
# car_started = False
#
# while  True:
#     command = input(">").lower() # the .lower puts whatever the use writes into lower case
#     if command == "start":
#         if car_started:
#             print("Car was started already")
#         else:
#             car_started = True
#             print("The car started")

#     elif command == "stop":
#         if not car_started:
#             print("Car was stopped already")
#         else:
#             car_started = False
#             print("The car has stopped")
#
#     elif command == "help":
#         print("""
# start - to start the car
# stop - to stop the car
# quit - to quit the program
#         """)
#     elif command == "quit":
#         break
#     else:
#      print("I do not understand your command")

#Use For Lops to iterate over numbers or names
# for n in range(1,11, 3):
#     print(n)
# for x in ["Charmu", "Jabu", "Trevor"]:
#     print(x)
# for item in  range(15):
#     item +=1
#     print(item)

#Calculate the total prices using for Loops for
#prices(10, 20, 30)

# prices = (10, 20, 30)
# total = 0
# for price in prices:
#     total += price
# print(f"Total,{total}")
#Write a program to find the largest number in a list
# numbers = (100, 250,70,50,895,1258)
# largest = max(numbers)
# print(largest)

# numbers = [100, 250,70,50,895,1258]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print(largest)

#Remove duplicates in a list - write a program
# numbers = (10,5,11,10,12,87.87,11)
# unique = set(numbers)
# unique_list=list(unique)
# print(unique)
#Using for loop:
# numbers = [10,5,11,10,12,87,87,11]
# unique = []
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)

# Write a program that converts mesasge to emojis
# message = input(">")
# words = message.split(" ")
# emojis = {
#     ":)": "😃",
#     ":(": "😪😪",
#     ":((": "😴"
# }
# output = " "
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# Create a function that calculates a square of a number/ returns a value or result of a function

# def square(number):
#     return number * number
# result = square(5)
# result_15 = square(15)
# print(result)
# print(result_15)

#Creating a reusable function from emoji converter

# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😃",
#         ":(": "😪😪",
#         ":((": "😴"
#     }
#     output = " "
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output

#
# message = input(">").lower()
# print(emoji_converter(message))

#Create an Employee class using OOP features with fist, last,age abd email methods.

# class Employee:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         self.email = first + '.' + last + '@' + 'gmail.com'
#     def fullname(self):
#         return f"{self.first} {self.last}"
#
#
# employee1 = Employee('John', 'Smith', 25)
# employee2 = Employee('Trevor', 'Noah', 45)
#
# print(employee1.fullname(),employee1.age)
# print(employee1.email)

#recreat a program to find max number form a list and package it as a module and
# save it under highest and the import it in another python doument and access the functions

# numbers = [100, 74 ,859,3,1000]
# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print(max_num)

# Create a dice program which randomly spits out two integers at each roll. The program should have a class called dice
# and have a method called roll.When the method is call it should print two random numbers everytime.

# import  random
#
# class  Dice:
#     def roll(self):
#         first = random.randint(1, 50)
#         second = random.randint(1, 50)
#         return first, second
#
# dice = Dice()
#
# print(dice.roll())

import random
class Leader:
    def pick_leader(self):
        names =["Jonh", "Teddy", "Celumusa","Charmu", "Clever", "Wandai"]
        chosen_name = random.choice(names)
        return f"The leader is:{chosen_name}"

leader=Leader()
print(leader.pick_leader())

















































