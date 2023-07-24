#!/usr/bin/env python3

def happy_new_year():
    i=10
    while i > 0:
        print(i)
        i-=1
    print("Happy New Year!")
    
def square_integers(int_list):
    square_integers = [int*int for int in int_list]
    return square_integers

def fizzbuzz():
    for number in range (1, 101):
        if number % 5 == 0 and number % 3 == 0:
            print ("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print(number)        