import joblib
import pandas as pd
import sqlite3

model = joblib.load("models/student_model.pkl")

conn = sqlite3.connect("database/student_risk.db")

query = """
SELECT G1, failures, studytime, absences, Medu, famrel, traveltime, G3
FROM students
LIMIT 1
"""

df = pd.read_sql(query, conn)
conn.close()

student = df.drop("G3", axis=1)

print("Original Student Data:\n", student)

current_grade = model.predict(student)[0]

print("\nCurrent Predicted Grade:", current_grade)

scenario1 = student.copy()
scenario1["G1"] = scenario1["G1"] + 2

grade1 = model.predict(scenario1)[0]

print("\nIf first exam score improves :", grade1)

scenario2 = student.copy()
scenario2["absences"] = scenario2["absences"] - 3
scenario2["absences"] = scenario2["absences"].clip(lower=0)

grade2 = model.predict(scenario2)[0]

print("\nIf absences decrease :", grade2)

scenario3 = student.copy()
scenario3["G1"] = scenario3["G1"] + 2
scenario3["studytime"] = scenario3["studytime"] + 1

grade3 = model.predict(scenario3)[0]

print("\nIf both improve :", grade3)