import sqlite3
import pandas as pd
import joblib

model = joblib.load("models/student_model.pkl")

conn = sqlite3.connect("database/student_risk.db")

query = """
SELECT G1, failures, studytime, absences, Medu, famrel, traveltime
FROM students
LIMIT 4
"""

df = pd.read_sql(query, conn)
conn.close()

for index, student in df.iterrows():

    print("\n==============================")
    print("Student", index + 1)
    print("==============================")

    features = pd.DataFrame([student])

    predicted_grade = model.predict(features)[0]

    print("\nPredicted Grade :", predicted_grade)

    risk_reasons = []

    if student["G1"] < 8:
        risk_reasons.append("Low first exam score")

    if student["absences"] > 10:
        risk_reasons.append("High absences")

    if student["studytime"] < 2:
        risk_reasons.append("Low study time")

    if risk_reasons:
        print("\nRisk Level : High")
        print("Reason :", ", ".join(risk_reasons))
    else:
        print("\nRisk Level : Low")

    print("\nWhat-If Analysis")

    scenario1 = features.copy()
    scenario1["studytime"] = scenario1["studytime"] + 1
    print("If studytime increases :", model.predict(scenario1)[0])

    scenario2 = features.copy()
    scenario2["absences"] = scenario2["absences"] - 3
    scenario2["absences"] = scenario2["absences"].clip(lower=0)
    print("If absences decrease :", model.predict(scenario2)[0])

    print("\nRecommendation:")

    recommendations = []

    if student["G1"] < 8:
        recommendations.append("Focus on improving the first exam performance.")

    if student["studytime"] < 2:
        recommendations.append("Increase daily study time to improve understanding of subjects.")

    if student["absences"] > 10:
        recommendations.append("Reduce absences and attend classes regularly.")

    if student["failures"] > 0:
        recommendations.append("Seek extra academic support to overcome subject difficulties.")

    if recommendations:
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec}")
    else:
        print("1. The student is performing well. Continue maintaining current study habits.")