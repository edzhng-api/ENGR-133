"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     15.2.2 Py3 Team 2 
    Team ID:        SC1 - 05 
    Author:         Anthony Do, do132@purdue.edu
    Date:           09/22/2026

Contributors:
    Edison Zheng, zhen1058@purdue.edu

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

""" Write any import statements here (and delete this line)."""

#Calculates the factorial of the given integer. Checks for a negative value, if true, returns an error, otherwise returns the factorial
def my_factorial(integer):
    if integer < 0: #Check if the integer is valid
        return -999
    else: 
        factorial = 1 #Set inital value to make code work
        for i in range(integer):
            factorial = factorial*integer
            integer=integer-1 #Increment down 1 to find factorial
        return factorial

def main():
    number = int(input("Enter a number: ")) #Takes an integer input
    if number < 0: #Checks if input is valid
        print(f"Error {my_factorial(number)} [Negative input].")
        return #Exits the program
    print(f"The Factorial of {number} is {my_factorial(number)}.") #Displays the result


if __name__ == "__main__":
    main()
