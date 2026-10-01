"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Parse data from a text file and uses it to calculate the concentration of a substance

Assignment Information:
    Assignment:     Py4 Team 3
    Team ID:        SC1 - 05
    Author:         Edison Zheng, zhen1058@purdue.edu
    Date:           9/29/26

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


#This function calculates the concentration of a substance given its absorbency, path length, and molar extinction coefficient, and prints the results.            
def absorb_calc(a, b, c):
    for i in range(len(a)):
        concentration = a[i] / (b * c)
        print(f"For {a[i]:.4f} absorbency value, the concentration is {concentration:.7f}")
def main():
    data = {"Absorbency": []}
    with open("py4_task3_input.txt", "r") as f:
        for line in f: 
            line = line.strip() 
            if not line:
                continue
            key, value = line.split(":", 1) #Split a pair at :
            key, value = key.strip(), value.strip()
            #For each category, store its value in the dictonary.
            if key == "Absorbency":
                data[key].append(float(value))
            elif key == "Name":
                data[key] = value
            else:
                data[key] = float(value)
    
    print(f"The name of the substance is {data["Name"]}")
    absorb_calc(data["Absorbency"], data["Path Length"], data["Molar Extinction Coefficient"])


if __name__ == "__main__":
    main()
