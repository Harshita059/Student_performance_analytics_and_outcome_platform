import pandas as pd
import sqlite3


def load_data():
    conn = sqlite3.connect("database/student_risk.db")
    df = pd.read_sql("SELECT * FROM students", conn)
    return df


def calculate_risk(df):

    risk_scores = []

    for _, row in df.iterrows():

        risk = 0

        if row["failures"] > 0:
            risk += 2

        if row["absences"] > 10:
            risk += 2

        if row["studytime"] < 2:
            risk += 1

        if row["G1"] < 10:
            risk += 2

        risk_scores.append(risk)

    df["risk_score"] = risk_scores

    return df


def risk_level(df):

    levels = []

    for score in df["risk_score"]:

        if score <= 2:
            levels.append("Safe")
        elif score <= 4:
            levels.append("Need Attention")
        else:
            levels.append("High Risk")

    df["risk_level"] = levels

    return df


if __name__ == "__main__":
    df = load_data()
    df = calculate_risk(df)
    df = risk_level(df)

    print(df[["G1","failures","absences","risk_score","risk_level"]].head())