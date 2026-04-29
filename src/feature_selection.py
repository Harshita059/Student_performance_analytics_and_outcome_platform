import pandas as pd
import sqlite3


def load_data():
    conn = sqlite3.connect("database/student_risk.db")
    df = pd.read_sql("SELECT * FROM students", conn)
    return df


def select_features(df):

    selected_columns = [
        "G1",
        "failures",
        "studytime",
        "absences",
        "Medu",
        "famrel",
        "traveltime",
        "G3"
    ]

    df = df[selected_columns]
    return df


if __name__ == "__main__":
    df = load_data()
    df = select_features(df)

    print(df.head())
    print("\nSelected Features Shape:", df.shape)