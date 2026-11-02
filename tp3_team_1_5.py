"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     TP3 Team 1
    Team ID:        SC1 - 05
    Author:         Edison Zheng, zhen1058@purdue.edu
    Date:           10/29/26

Contributors:
    Claude AI

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
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
    # Euclidean distance from new_example to every training example
    distance = np.linalg.norm(x_train - new_example, 2, 1)

    # Indices of the k nearest training examples (smallest distances)
    nearest_index = np.argsort(distance)[:k]
    neighbor_labels = y_train[nearest_index]

    # Count votes for each class (0 = deer, 1 = left turn)
    deer_count = np.sum(neighbor_labels == 0)
    leftturn_count = np.sum(neighbor_labels == 1)

    # Predict the majority label
    if deer_count > leftturn_count:
        predicted_label = np.int64(0)
    else:
        predicted_label = np.int64(1)

    return predicted_label


def predict_labels_knn(X_new, x_train, y_train, k):
    # Number of examples we need predictions for
    n_new = X_new.shape[0]
    # Array to hold one integer prediction per example
    predicted_labels = np.zeros(n_new, dtype=int)

    # Predict each example one at a time using the single-example function
    for i in range(n_new):
        predicted_labels[i] = knn_single_prediction(X_new[i], x_train, y_train, k)

    return predicted_labels


def calculate_metrics(predicted_labels, true_labels):
    # Accuracy = fraction of predictions that match the true labels
    accuracy = float(np.mean(predicted_labels == true_labels))
    # Error rate is the fraction that were wrong
    error = 1 - accuracy
    return accuracy, error
def main():
    path = input("Enter the path to the feature dataset: ")
    shuffle = input("Shuffle the dataset? (yes/no): ")
    seed = int(input("Enter a seed for loading the dataset: "))
    k = int(input("Enter the value of k to use for KNN: "))
    #Column names of features and label taken directly from path
    features = ["hue_mean", "hue_std", "saturation_mean","saturation_std","value_mean","value_std","number_lines","has_circle","has_triangle"]
    label = "ClassId"
    
    #Load dataset
    if shuffle == "yes":
        x, y = load_dataset(path, features, label, True, seed)
    else: 
        x, y = load_dataset(path, features, label, False, seed)
    
    #Split data
    x_train, y_train, x_val, y_val, x_test, y_test = train_val_test_split(x, y)
    
    #Display sizes of train, value, and test sets
    print()
    print("Data loaded and split into")
    print()
    print("Training set:")
    print(f"  size: {x_train.shape[0]}")
    print("Validation set:")
    print(f"  size: {x_val.shape[0]}")
    print("Test set:")
    print(f"  size: {x_test.shape[0]}")
    
    #Prediction modeling
    train_prediction = predict_labels_knn(x_train, x_train, y_train, k)
    accuracy, error = calculate_metrics(train_prediction, y_train)
    print()
    print(f"Evaluating KNN model on Training set with k = {k}...")
    print()
    print("--- Model Performance on Training Set ---")
    print(f"Training Set Accuracy: {accuracy:.4f}")
    print(f"Training Set Error Rate: {error:.4f}")

    value_prediction = predict_labels_knn(x_val, x_train, y_train, k)
    accuracy, error = calculate_metrics(value_prediction, y_val)
    print()
    print(f"Evaluating KNN model on validation set with k = {k}...")
    print()
    print("--- Model Performance on Validation Set ---")
    print(f"Validation Set Accuracy: {accuracy:.4f}")
    print(f"Validation Set Error Rate: {error:.4f}")

    test_prediction = predict_labels_knn(x_test, x_train, y_train, k)
    accuracy, error = calculate_metrics(test_prediction, y_test)
    print()
    print(f"Evaluating KNN model on test set with k = {k}...")
    print()
    print("--- Model Performance on Test Set ---")
    print(f"Test Set Accuracy: {accuracy:.4f}")
    print(f"Test Set Error Rate: {error:.4f}")


if __name__ == "__main__":
    main()
