import pandas as pd
df = pd.read_csv("data/student_data.csv")

print(df.head())

X = df[["study_hours", "attendance", "previous_score"]]
y = df["final_score"]

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

model = LinearRegression()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model.fit(X_train, y_train) 

test_predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, test_predictions)
mse = mean_squared_error(y_test, test_predictions)
rmse = mse ** 0.5
r2 = r2_score(y_test, test_predictions)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)

print("Actual Test Score:", y_test)
print("Predicted Test Score:", test_predictions)

print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)

new_student = pd.DataFrame(
    [[7, 85, 78]],
    columns=["study_hours", "attendance", "previous_score"]
)

prediction = model.predict(new_student)

print("Predicted Final Score:", prediction)