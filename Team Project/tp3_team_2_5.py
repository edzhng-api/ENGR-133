"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     9.1.2 Tp3 Team 2 
    Team ID:        SC1 - 05
    Author:         Anthony Do, do132@purdue.edu
    Date:           10/29/2026

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

import pandas as pd
import numpy as np
#import functions from task 1
from tp3_team_1_5 import scale_features, load_dataset, train_val_test_split, calculate_metrics
#calculate sigmoid
def calculate_sigmoid(z):
    z = np.clip(z, -10, 10)
    result = 1 / (1 + np.exp(-z))
    return result
#calculate probability
def predict_proba(X, w, b):
    z = X @ w + b
    probabilities = calculate_sigmoid(z)
    return probabilities
#assign labels based on whether probabilities is larger than or equal to threshold = 0.5
def predict_labels(X, w, b, threshold=0.5):
    probabilities = predict_proba(X, w, b)
    predicted_labels = (probabilities >= threshold).astype(int)
    return predicted_labels

def compute_loss_and_grads(X,y,w,b):
    # Number of examples, used to average the loss and gradients
    m = X.shape[0]
    #predicted probability of class 1 for every example
    y_hat = predict_proba(X, w, b)
    #clip for the logs so log(0) never occurs
    eps = 1e-15
    y_hat_clipped = np.clip(y_hat, eps, 1 - eps)
    # Average binary cross-entropy loss over all examples
    loss = -np.mean(y * np.log(y_hat_clipped) + (1 - y) * np.log(1 - y_hat_clipped))
    # Prediction error for each example (uses the unclipped probabilities)
    error = y_hat - y
    # Gradient of the loss with respect to the weights, shape (n,)
    dw = (1 / m) * (X.T @ error)
    # Gradient of the loss with respect to the bias (scalar)
    db = np.sum(error) / m
    return float(loss), dw, float(db)
def train_logistic_regression(X_train, y_train, X_val, y_val, learning_rate, num_iterations):
    n_features = X_train.shape[1]
    # Start with small random weights (breaks symmetry) and a zero bias
    w = np.random.randn(n_features) * 0.01
    b = 0.0
    # Lists to record the loss at every iteration
    loss_history = []
    val_loss_history = []
    # Track the parameters that give the lowest validation loss so far
    best_val_loss = float("inf")
    w_best = w.copy()
    b_best = b
    for i in range(num_iterations):
        loss, dw, db = compute_loss_and_grads(X_train, y_train, w, b)
        # Gradient descent step: move opposite to the gradient
        w = w - learning_rate * dw
        b = b - learning_rate * db
        # Record the training loss for this iteration
        loss_history.append(loss)
        # Validation loss with the updated parameters (gradients are not used)
        val_loss, _, _ = compute_loss_and_grads(X_val, y_val, w, b)
        val_loss_history.append(val_loss)
        # Save a copy of the parameters if validation loss is the lowest so far
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            w_best = w.copy()
            b_best = b
        # Print progress at the start and every 100 iterations
        if i % 100 == 0:
            print(f"Iteration {i}, Train Loss: {loss:.4f}, Val Loss: {val_loss:.4f}")
    return w_best, b_best, loss_history, val_loss_history
def evaluate_logistic_regression(X, y, w, b):
    # Convert predicted probabilities to class labels (0 or 1)
    y_pred = predict_labels(X, w, b)
    # Compare predictions with the true labels
    accuracy, error_rate = calculate_metrics(y_pred, y)
    return accuracy, error_rate
def main():
    #User input
    path = input("Enter the path to the feature dataset: ")
    shuffle_answer = input("Shuffle the dataset? (yes/no): ")
    seed = int(input("Enter a seed for loading the dataset: "))
    shuffle = shuffle_answer.strip().lower() == "yes"
    np.random.seed(seed)
    feature_cols = ["hue_mean", "hue_std", "saturation_mean", "saturation_std",
                    "value_mean", "value_std", "number_lines", "has_circle",
                    "has_triangle"]
    #label is the last column of the file 
    label_col = pd.read_csv(path).columns[-1]   
    #load dataset
    X, y = load_dataset(path, feature_cols, label_col, shuffle, seed)
    print(f"\nFeatures shape: {X.shape}")
    print(f"Labels shape: {y.shape}")

    # Split
    X_train, y_train, X_val, y_val, X_test, y_test = train_val_test_split(X, y)
    print("Data loaded and split into")
    print(f"\nTraining set: size: {X_train.shape[0]}")
    print(f"Validation set: size: {X_val.shape[0]}")
    print(f"Test set: size: {X_test.shape[0]}")
    # Hyperparameters
    learning_rate = 0.01
    num_iterations = 5000
    # Train
    print(f"\nTraining logistic regression model with learning rate = {learning_rate} "
          f"and num_iterations = {num_iterations}...\n")
    w_best, b_best, loss_history, val_loss_history = train_logistic_regression(
        X_train, y_train, X_val, y_val, learning_rate, num_iterations)
    # Evaluate
    train_acc, train_err = evaluate_logistic_regression(X_train, y_train, w_best, b_best)
    val_acc, val_err = evaluate_logistic_regression(X_val, y_val, w_best, b_best)
    test_acc, test_err = evaluate_logistic_regression(X_test, y_test, w_best, b_best)
    print("\nFinal Model Evaluation with the best parameters:")
    print("-" * 50)
    print(f"Training Set - Accuracy: {train_acc * 100:.2f}%, Error Rate: {train_err * 100:.2f}%")
    print(f"Validation Set - Accuracy: {val_acc * 100:.2f}%, Error Rate: {val_err * 100:.2f}%")
    print(f"Test Set - Accuracy: {test_acc * 100:.2f}%, Error Rate: {test_err * 100:.2f}%")
    # Final parameters
    print("\nFinal Parameters:")
    print(f"Weights shape: {w_best.shape}")
    print(f"Bias: {b_best:.6f}")
    print(f"Final training loss: {loss_history[-1]:.6f}")
    # Feature importance
    print("\nFeature Importance (absolute weight values):")
    for j, weight in enumerate(np.abs(w_best)):
        print(f"Feature {j}: {weight:.6f}")

if __name__ == "__main__":
    main()
