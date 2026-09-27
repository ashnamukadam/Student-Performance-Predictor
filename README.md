# Student Performance Predictor

A beginner-friendly machine learning project that predicts a student's final score based on study hours, attendance, and previous academic performance.

## Features

- Study hours
- Attendance percentage
- Previous score

## Machine Learning Model

This project uses Linear Regression to predict the student's final score.

## Workflow

1. Generate a synthetic student dataset
2. Store the dataset as a CSV file
3. Load the dataset using Pandas
4. Separate features and target
5. Split the data into training and testing sets
6. Train a Linear Regression model
7. Evaluate the model
8. Predict the final score for a new student

## Model Evaluation

The model was evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### Results

Metric | Score
--- | ---
MAE | 1.66
MSE | 4.30
RMSE | 2.07
R² | 0.964

## Example Prediction

For a student with:

- Study hours: 7
- Attendance: 85%
- Previous score: 78

The model predicts a final score of approximately:

83.93

## Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn

## Dataset

The dataset used in this project is synthetically generated for learning purposes.

## How to Run

Install the required dependencies:

pip install -r requirements.txt

Generate the dataset:

python create_dataset.py

Run the predictor:

python student_predictor.py

## Note

This project is intended for educational purposes. The dataset is synthetic, so the model's performance should not be interpreted as a real-world prediction system.