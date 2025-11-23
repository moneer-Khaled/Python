# 1. Multiplication

# Create a function that gets a number as a parameter, and then prints the multiplication 
# table for that number from 1 to 10. E.g., when the parameter is 12,
# the first line printed is “1 x 12 = 12” and the last line printed is “10 x 12 = 120.”
print("1. Multiplication")
def multiply(number):
    for i in range(1,11):
        print (1,"x",number,"=", i*number)
        
multiply(12)




# 2. Sum of two strings

# Write a function that takes two strings as parameters.
# The function returns the number of characters that the strings have in common.
# Each character counts only once, e.g., the strings "bee" and "peer" only have one character 
# in common (the letter “e”). You can consider capitals different from lowercase letters. Note: the function should return the number 
# of characters that the strings have in common, and not print it. To test the function, you can print the result in your main program.

print("2. Sum of two strings")
def strings(str1, str2):
    set1=set(str1)
    set2=set(str2)
    
    set3 =set1.intersection(set2)
    print("The commen charecter:",len(set3))

strings("pen","Apple")

# 3. Guessing a number

# Write a guessing number function that holds a random number between 1 and 10 and get a parameter number. The return for that function will be :

# "Too big" if the parameter number is bigger than the held number.

# "Too small" if the parameter number is smaller than the held number.

# "You are SUPER" if the parameter number is the same as the held number.

# Enter the parameter number via the terminal with the help of the input method.

import random


print("\n Guessing a Number")

import random

def guessed_number(number):
    held_number=random.randint(1,10)
    
    if number> held_number:
        return "Too big"
    elif number < held_number:
       return "Too Small"
    else:
        return "You are SUPER"
    
guess=int(input("Enter a number between 1 and 10:"))
print(guessed_number(guess))

