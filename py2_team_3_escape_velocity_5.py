"""
Course Number: ENGR 13300
Semester: e.g. Spring 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     Py 2 Team 3
    Team ID:        SC1 - 05
    Author:         Edison Zheng, zhen1058@purdue.edu
    Date:           9/15/2026

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


def calc_escape_velocity(G, mass, radius):
    if radius <= 0:
        print("Radius must be greater than zero!")
        return 0
    elif mass <= 0:
        print("Mass must be greater than zero!")
        return 0
    else:
        v_e = m.sqrt((2 * G * mass) / radius)
        return v_e

def main():
    """Write your code here (and delete this line)."""


if __name__ == "__main__":
    main()
