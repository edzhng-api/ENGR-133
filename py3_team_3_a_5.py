"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Aproximates e^x using the Maclaurin series expansion with given values of n and x.

Assignment Information:
    Assignment:     15.2.3. Py3 Team 3 A
    Team ID:        SC1 - 05
    Author:         Reese Jared, rjared@purdue.edu
    Date:           09/24/2026

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import math as m
import numpy as np

def my_factorial(integer):
    if integer < 0: #Check if the integer is valid
        return -999
    else: 
        factorial = 1 #Set inital value to make code work
        for i in range(integer):
            factorial = factorial*integer
            integer=integer-1 #Increment down 1 to find factorial
        return factorial

def maclaurin_step(x, n):
    return (x ** n) / my_factorial(n)

def my_sum(n, x):
    return sum(maclaurin_step(x, i) for i in range(0, n + 1))

def main():
    n = int(input("Enter the value of n: "))
    x = float(input("Enter the value of x: "))
    aprox_sum = my_sum(n, x)
    actual_value = m.e ** x
    error = (aprox_sum-actual_value) / actual_value * 100

    print(f"Actual value: {actual_value:.2f}")
    print(f"Approximate value: {aprox_sum:.2f}")
    print(f"Error: {error:.1f}%")

if __name__ == "__main__":
    main()
