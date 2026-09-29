"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     16.2.2. Py4 Task 2
    Team ID:        SC1 - 05
    Author:         Reese Jared, rjared@purdue.edu
    Date:           09/29/2026

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

from datetime import date

def main():
    f = open("py4_team_2_5.txt", "r+")
    f.truncate(0)  # Clear the file contents before writing new data
    Additional_Entry = "yes"
    while Additional_Entry == "yes":
        try:
            Last_Name = input("Enter your last name:\n")
            First_Name = input("Enter your first name:\n")
            Birthday_str = input("Enter your birthday (MM/DD/YYYY):\n")
            Date_str = input("Enter the current date (MM/DD/YYYY):\n")
            Additional_Entry = input("Would you like to enter another person (yes/no)?\n")


            # Convert strings to date objects
            Birthday_split = Birthday_str.split('/')
            Date_split = Date_str.split('/')
            Birthday = date(int(Birthday_split[2]), int(Birthday_split[0]), int(Birthday_split[1]))
            Date = date(int(Date_split[2]), int(Date_split[0]), int(Date_split[1]))

            # Calculate age
            years_between = (Date - Birthday).days // 365
            seconds_between = (Date - Birthday).days * 86400

            # Saves the information to the file
            f.write(f"{First_Name} {Last_Name}\n")
            f.write(f"You are {years_between} years old.\n")
            f.write(f"You are {seconds_between} seconds old.\n")

            # Error detection for invalid date formats
        except ValueError:
            print("Invalid date format. Please use MM/DD/YYYY.")
            """
        except Exception as e:
            print(f"An error occurred: {e}")
            """
    f.seek(0)  # Move the file pointer to the beginning of the file
    print(f.read())
    f.close()

if __name__ == "__main__":
    main()