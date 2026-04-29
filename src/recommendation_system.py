import pandas as pd
import sqlite3


def load_data():
     conn = sqlite3.connect("database/student_risk.db")
     df = pd.read_sql("SELECT * FROM students", conn)
     return df


def generate_recommendations(row):

    recommendations = []

    if row["studytime"] < 2:
        recommendations.append("Increase daily study time.")

    if row["absences"] > 10:
        recommendations.append("Reduce absences and attend classes regularly.")

    if row["failures"] > 0:
        recommendations.append("Focus on weak subjects and seek extra help.")

    if row["famrel"] < 3:
        recommendations.append("Improve communication with family for support.")

    if row["traveltime"] > 2:
        recommendations.append("Try to reduce travel time to school.")

    if not recommendations:
        recommendations.append("Student performance is stable. Keep maintaining study habits.")

    return "; ".join(recommendations)


if __name__ == "__main__":
    df = load_data()

    df["recommendations"] = df.apply(generate_recommendations, axis=1)

    print(df[["G1","studytime","absences","failures","recommendations"]].head())