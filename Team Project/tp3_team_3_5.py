"""
Course Number: ENGR 13300
Semester: Fall 2026

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     9.1.3 Tp3 Team 3
    Team ID:        SC1 - 05
    Author:         Anthony Do, do132@purdue.edu
    Date:           11/3/2026

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
#import libraries and important functions from previous tasks
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from tp3_team_1_5 import predict_labels_knn,calculate_metrics,load_dataset,train_val_test_split
from tp3_team_2_5 import evaluate_logistic_regression,calculate_sigmoid,train_logistic_regression
def evaluate_knn_model(k_values, X_train, y_train, X_val, y_val):
    #empty results dictionary
    metrics = {
        "acc": {"train_acc": [], "val_acc": []},
        "error": {"train_error": [], "val_error": []}
    }
    #loop through each k
    for k in k_values:
        #predict train and validation labels
        y_train_pred = predict_labels_knn(X_train, X_train, y_train, k)
        y_val_pred = predict_labels_knn(X_val, X_train, y_train, k)
        #accuracy and error
        train_acc, train_error = calculate_metrics(y_train_pred, y_train)
        val_acc, val_error = calculate_metrics(y_val_pred, y_val)
        #store results
        metrics["acc"]["train_acc"].append(train_acc)
        metrics["acc"]["val_acc"].append(val_acc)
        metrics["error"]["train_error"].append(train_error)
        metrics["error"]["val_error"].append(val_error)
    return metrics
def plot_knn_performance(metrics,k_values):
    #create figure with 2 plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    #plot 1: Accuracy vs k
    ax1.plot(k_values, metrics["acc"]["train_acc"], marker="o", label="Training Accuracy")
    ax1.plot(k_values, metrics["acc"]["val_acc"], marker="o", label="Validation Accuracy")
    ax1.set_title("Accuracy vs. Number of Neighbors (k)")
    ax1.set_xlabel("k (Number of Neighbors)")
    ax1.set_ylabel("Accuracy")
    ax1.legend()
    #plot 2: Error rate vs k
    ax2.plot(k_values, metrics["error"]["train_error"], marker="o", label="Training Error")
    ax2.plot(k_values, metrics["error"]["val_error"], marker="o", label="Validation Error")
    ax2.set_title("Error Rate vs. Number of Neighbors (k)")
    ax2.set_xlabel("k (Number of Neighbors)")
    ax2.set_ylabel("Error Rate")
    ax2.legend()
    #save figure into train_val.png
    plt.tight_layout()
    plt.savefig("train_val.png")
    plt.close()
def select_best_k(k_values,metrics):
    best_value_index = np.argmax(np.array(metrics["acc"]["val_acc"]))
    best_k = k_values[best_value_index]
    return best_k
def evaluate_knn_test_set(X_test,y_test,X_train,y_train,best_k):
    y_test_pred = predict_labels_knn(X_test, X_train, y_train, best_k)
    test_accuracy, test_error = calculate_metrics(y_test_pred,y_test)
    return float(test_accuracy),float(test_error)
def evaluate_logistic_model(X_train, y_train, X_val, y_val, X_test, y_test, w, b):
    # Step 1: results dictionary
    metrics = {
        "train": {"accuracy": 0.0, "error": 0.0},
        "val": {"accuracy": 0.0, "error": 0.0},
        "test": {"accuracy": 0.0, "error": 0.0},
    }

    # Steps 2-3: evaluate the same trained model on each set
    train_acc, train_error = evaluate_logistic_regression(X_train, y_train, w, b)
    val_acc, val_error = evaluate_logistic_regression(X_val, y_val, w, b)
    test_acc, test_error = evaluate_logistic_regression(X_test, y_test, w, b)

    # Step 4: store results
    metrics["train"]["accuracy"] = train_acc
    metrics["train"]["error"] = train_error
    metrics["val"]["accuracy"] = val_acc
    metrics["val"]["error"] = val_error
    metrics["test"]["accuracy"] = test_acc
    metrics["test"]["error"] = test_error

    return metrics
def plot_logistic_training(loss_history, val_loss_history):
    plt.figure(figsize=(8, 5))
    #training and validation loss curves
    plt.plot(loss_history, label="Training Loss")
    plt.plot(val_loss_history, label="Validation Loss")
    #title, labels, legend
    plt.title("Logistic Regression Training Progress")
    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.legend()
    #save and close
    plt.savefig("training_progress.png")
    plt.close()
def main():
    #users inputs
    path = input("Enter the path to the feature dataset: ")
    shuffle = input("Shuffle the dataset? (yes/no): ")
    seed = int(input("Enter a seed for loading the dataset: "))
    #load and split data set
    features = ["hue_mean", "hue_std", "saturation_mean", "saturation_std",
                "value_mean", "value_std", "number_lines", "has_circle", "has_triangle"]
    label = "ClassId"
    x, y = load_dataset(path, features, label, shuffle == "yes", seed)
    x_train, y_train, x_val, y_val, x_test, y_test = train_val_test_split(x, y)
    print()
    print("Data loaded and split into")
    print()
    print("Training set:")
    print(f"  size: {x_train.shape[0]}")
    print("Validation set:")
    print(f"  size: {x_val.shape[0]}")
    print("Test set:")
    print(f"  size: {x_test.shape[0]}")
    #KNN across k values
    k_values = [1, 3, 5, 7, 9, 15, 31, 53]
    knn_metrics = evaluate_knn_model(k_values, x_train, y_train, x_val, y_val)

    print()
    print("KNN Validation Curve Summary")
    for i in range(len(k_values)):
        train_acc = knn_metrics["acc"]["train_acc"][i]
        val_acc = knn_metrics["acc"]["val_acc"][i]
        print(f"k = {k_values[i]}: train accuracy = {train_acc:.4f}, validation accuracy = {val_acc:.4f}")

    #plot, best k, test set
    plot_knn_performance(knn_metrics, k_values)

    best_k = select_best_k(k_values, knn_metrics)
    print()
    print(f"Based on the plots, the best k appears to be: {best_k}")

    knn_test_acc, knn_test_error = evaluate_knn_test_set(x_test, y_test, x_train, y_train, best_k)
    print()
    print("--- Final KNN Model Performance ---")
    print(f"Test Set Accuracy: {knn_test_acc:.4f}")
    print(f"Test Set Error Rate: {knn_test_error:.4f}")

    #train logistic regression
    learning_rate = 0.01
    num_iterations = 5000
    print()
    print(f"Training logistic regression model with learning rate = {learning_rate} and num_iterations = {num_iterations}...")
    print()
    w, b, loss_history, val_loss_history = train_logistic_regression(x_train, y_train, x_val, y_val, learning_rate, num_iterations)

    #evaluate, plot, and summarize
    log_metrics = evaluate_logistic_model(x_train, y_train, x_val, y_val, x_test, y_test, w, b)
    plot_logistic_training(loss_history, val_loss_history)
    print()
    print("Final Logistic Regression Evaluation:")
    print("-" * 50)
    for name, key in [("Training", "train"), ("Validation", "val"), ("Test", "test")]:
        acc = log_metrics[key]["accuracy"]
        err = log_metrics[key]["error"]
        print(f"{name} Set - Accuracy: {acc:.4f} ({acc*100:.2f}%), Error Rate: {err:.4f} ({err*100:.2f}%)")
    best_val_acc = max(knn_metrics["acc"]["val_acc"])
    print()
    print("Model Summary")
    print(f"Best KNN validation accuracy: {best_val_acc:.4f}")
    print(f"Logistic regression validation accuracy: {log_metrics['val']['accuracy']:.4f}")
    print(f"KNN test accuracy: {knn_test_acc:.4f}")
    print(f"Logistic regression test accuracy: {log_metrics['test']['accuracy']:.4f}")
    
if __name__ == "__main__":
    main()