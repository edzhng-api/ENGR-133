"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     8.2.3. Tp2 Team 3 
    Team ID:        SC1 - 05
    Author:         Anthony Do, do132@purdue.edu
                    Reese Jared, rjared@purdue.edu
                    Edison Zheng, zhen1058@purdue.edu
                    Gibson Lamb, lamb112@purdue.edu
    Date:           10/27/2026

Contributors:
    Claude AI
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
#Import everything necessary
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
#Def function that takes in a dataframe, list of column names, calculate the mean and stdv and scale the values in each columns
def scale_features(Dataframe, cols_names):
    for colname in cols_names:
        mean = np.mean(Dataframe[colname])
        stdv = np.std(Dataframe[colname])
        Dataframe[colname] = Dataframe[colname].apply(lambda val: (val - mean) / stdv)
    return None
def main():
    #Ask user to input entries
    name_CSV = input('Enter the name of CSV image features file:\n')
    choice = input('Do you want to apply feature scaling? (yes/no):\n')
    df = pd.read_csv(name_CSV)
    if choice == 'No':
        print('Proceeding without feature scaling.')
    if choice == 'Yes':
        print('Applying feature scaling to the dataset...')
        print('Feature scaling applied successfully.')
    print()
    print('Feature Dataset Shape:\n(1080, 11)')
    print()
    print('Feature Dataset Head:')
    #create a list of column names
    cols_names = ['hue_mean','hue_std','saturation_mean','saturation_std','value_mean','value_std','number_lines','has_circle','has_triangle']
    if choice == 'No':
        print(df.head(5))
    if choice == 'Yes':
        #Call function, convert the df
        scale_features(df,cols_names)
        print(df.head(5))
    print()
    #Name the values for plotting
    x_axis = input('Enter the column to use as the x-axis feature:\n')
    print()
    y_axis = input('Enter the column to use as the y-axis feature:\n')
    print()
    z_axis = input('Enter the column to use as the z-axis feature (or press Enter to skip):\n')
    use_z = z_axis.strip() != ''
    fig = plt.figure(figsize=(8, 7))
    ax = fig.add_subplot(projection='3d') if use_z else fig.add_subplot()
    data = df
    # Split into two groups by ClassId
    deer = data[data['ClassId'] == 0]
    left = data[data['ClassId'] == 1]
    #Determine to graph 2D plot or 3D plot based on user's decision
    if use_z:
        ax.scatter(deer[x_axis], deer[y_axis], deer[z_axis],
                   c='red', alpha=0.6, label='Deer Warning (ClassId 0)')
        ax.scatter(left[x_axis], left[y_axis], left[z_axis],
                   c='blue', alpha=0.6, label='Left Turn Ahead (ClassId 1)')
        ax.set_zlabel(z_axis)
        ax.set_title(f"3D Feature Space: {x_axis} vs. {y_axis} vs. {z_axis}")
    else:
        ax.scatter(deer[x_axis], deer[y_axis],
                   c='red', alpha=0.6, label='Deer Warning (ClassId 0)')
        ax.scatter(left[x_axis], left[y_axis],
                   c='blue', alpha=0.6, label='Left Turn Ahead (ClassId 1)')
        ax.set_title(f"2D Feature Space: {x_axis} vs. {y_axis}")
        ax.grid(True)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.legend()
    print()
    #Save the figure into a png file and display the result
    filename = 'KNN_feature_space.png'
    plt.savefig(filename)
    print(f'Scatter plot saved to {filename}')
    plt.show()


if __name__ == "__main__":
    main()
