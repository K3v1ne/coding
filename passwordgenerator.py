## A simple password generator codes by python

import random

numbers = "1234567890"
letters = "qwertyuiopasdfghjklzxcvbnm"
characters = "!@#$%^&*()~"

def so():
	for i in range(10):
		print(random.choice(numbers), end ="")
def chu():
	for i in range(8):
		print(random.choice(letters), end="")
def kitu():
	for i in range(5):
		print(random.choice(characters), end="")

print("Your password is: ", end ="")
chu(), so(), kitu()