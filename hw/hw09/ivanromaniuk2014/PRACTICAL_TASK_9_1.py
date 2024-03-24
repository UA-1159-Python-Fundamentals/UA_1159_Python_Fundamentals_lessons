#Task_2

import random

user_name = input("Hello! what is your name? \n")

number = random.randint(1, 100)\

counter = 0

while counter <= 10:

  if counter == 10:
    print(f"Sorry, {user_name} but you lose! \n It was number {number}")
    break

  counter += 1
  
  guess_number = int(input("Enter your number from range: 1 to 100: "))
  
  if guess_number == number:
    print(f"Good work, {user_name}! You are winner!")
    break
  elif 1 <= guess_number <= 100 and guess_number < number:
    print("Your number is less! Try again Bro!")
  elif 1 <= guess_number <= 100 and guess_number > number:
    print("Your number is more! Try again Bro!")
  elif not 1 <= guess_number <= 100:
    print("your number is not in range 1 to 100, try again Bro!")