"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     e.g. 7.2.1 Py1 Team 1 (for Python 1 Team task 1)
    Team ID:        SC1 - 05
    Author:         Edison Zheng, zhen1058@purdue.edu
    Date:           10/29/26

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

import numpy as np
from pathlib import Path
import pandas as pd


def scale_features(Dataframe, cols_names):
    for colname in cols_names:
        mean = np.mean(Dataframe[colname])
        stdv = np.std(Dataframe[colname])
        Dataframe[colname] = Dataframe[colname].apply(lambda val: (val - mean) / stdv)
    return None
def load_dataset(file_path, feature_cols, label_col, shuffle, seed=42):
    """
    Loads a dataset from a CSV file, separates features and labels,
    and optionally shuffles the data.
    """
    df = pd.read_csv(file_path)

    # Use the existing feature scaling function from Checkpoint 2 Task 3
    scale_features(df, feature_cols)

    X = df[feature_cols].to_numpy()
    y = df[label_col].to_numpy()

    if shuffle:
        np.random.seed(seed)
        shuffled_indices = np.random.permutation(len(y))
        X = X[shuffled_indices]
        y = y[shuffled_indices]

    return X, y
def train_val_test_split(x, y, train_ratio=0.8, val_ratio=0.1, test_ratio=0.1):
    if train_ratio+val_ratio+test_ratio != 1.0:
        return
    rows= x.shape[0]
    
    #Find number of rows used in each split
    x_row_train = int(rows*train_ratio)
    x_row_val = int(rows*val_ratio)
    
    #Using the number of rows as indexes allocate the data
    x_train = x[:x_row_train]
    y_train = y[:x_row_train]
    x_val = x[x_row_train:x_row_train+x_row_val]
    y_val = y[x_row_train:x_row_train+x_row_val]
    x_test = x[x_row_train+x_row_val:]
    y_test = y[x_row_train+x_row_val:]
    return x_train, y_train, x_val, y_val, x_test, y_test
def knn_single_prediction(new_example, x_train, y_train, k):
    return
def predict_labels_knn(X_new, x_train, y_train, k):
    return
def calculate_metics(predicted_labels, true_labels):
    return
def main():
    """Write your code here (and delete this line)."""


if __name__ == "__main__":
    main()
