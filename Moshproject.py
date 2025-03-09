# Full_name = "Jonh Smith"
# age = 20
# Is_new = True
# print(Full_name)
# print("Age", age)
# print("Is_new:", Is_new)

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

command = ""
while  True:
    command = input(">").lower() # the .lower puts whatever the use writes into lower case
    if command == "start":
        print("The car has started")
    elif command == "stop":
        print("The car has stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit the program
        """)
    elif command == "quit":
        break
    else:
     print("I do not understand your command")


























