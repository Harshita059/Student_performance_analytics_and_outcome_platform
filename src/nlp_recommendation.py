import sqlite3
import pandas as pd


def load_data():
    conn = sqlite3.connect("database/student_risk.db")
    df = pd.read_sql("SELECT * FROM students", conn)
    conn.close()
    return df


def generate_recommendation(row):

    risk_factors = []

    if row["G1"] < 8:
        risk_factors.append("low first exam score")

    if row["studytime"] < 2:
        risk_factors.append("low study time")

    if row["absences"] > 10:
        risk_factors.append("high number of absences")

    if row["failures"] > 0:
        risk_factors.append("previous academic failures")

    if risk_factors:
        description = "The student is facing academic risk due to " + ", ".join(risk_factors) + "."
        recommendation = "The student should increase study time, attend classes regularly and focus on improving early assessments."
    else:
        description = "The student is performing well."
        recommendation = "The student should continue maintaining current study habits."

    return description + "\n" + recommendation


if __name__ == "__main__":

    df = load_data()

    for index, row in df.head().iterrows():

        print("\nStudent Data")
        print("G1 :", row["G1"])
        print("Study Time :", row["studytime"])
        print("Absences :", row["absences"])

        rec = generate_recommendation(row)

        print("\nRecommendation:")
        print(rec)
        print("-" * 50)