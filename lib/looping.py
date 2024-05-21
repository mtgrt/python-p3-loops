#!/usr/bin/env python3

def happy_new_year():
   i = 10
   while i > 0:
      print(i)
      i -= 1
      print("Happy New Year!")
       
def square_integers(int_list):
     # Initialize an empty list to store the squared numbers
    squared_numbers= []
    # Iterate through each number in the input list
    for num in int_list:
         # Check if the current number is an integer
        if isinstance(num, int):
            # Square the current number and append it to the list
            squared_numbers.append(num**2)
    return squared_numbers

def fizzbuzz():
   # Iterate through the numbers from 1 to 100
   for i in range (1,101):
     # Check if the number is a multiple of both 3 and 5
     if i % 3 == 0 and i % 5 == 0:
       print("FizzBuzz")
        # Check if the number is a multiple of 3
     elif i % 3 ==  0  :
       print("Fizz")
       # Check if the number is a multiple of 5
     elif i % 5 == 0:
         print("Buzz")
         # If none of the above conditions are true, print the number
     else:
        print (i)
       
