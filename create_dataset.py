import numpy as np
import pandas as pd

np.random.seed(42)

students = []

for i in range(100):
    study_hours = np.random.randint(1, 11)
    attendance = np.random.randint(50, 101)
    previous_score = np.random.randint(40, 91)

    final_score = (
        0.5 * study_hours
        + 0.3 * attendance
        + 0.7 * previous_score
        + np.random.normal(0, 3)
    )

    students.append([
        study_hours,
        attendance,
        previous_score,
        final_score
    ])

df = pd.DataFrame(
    students,
    columns=[
        "study_hours",
        "attendance",
        "previous_score",
        "final_score"
    ]
)

df.to_csv("data/student_data.csv", index=False)

print("Dataset created successfully!")
print(df.head())