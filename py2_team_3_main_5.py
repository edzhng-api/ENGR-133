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

import py2_team_3_volume_5 as vol
import py2_team_3_mass_5 as mass
import py2_team_3_escape_velocity_5 as ev


def main():
    G = 6.674 * 10**-11
    rho = float(input("Enter the average density of the planet: "))
    r = float(input("Enter the radius of the planet: "))
    volume = vol.calc_volume(r)
    mass_value = mass.calc_mass(rho, volume)
    e_v = ev.calc_escape_velocity(G, mass_value, r)
    r = r/1000

    print(f"For a planet with radius {r:,.1f} km and density {rho:,.2f} kg/m^3, the estimated escape velocity is {e_v:,.2f} m/s")



if __name__ == "__main__":
    main()
