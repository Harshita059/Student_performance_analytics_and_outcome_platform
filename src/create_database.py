import pandas as pd
import sqlite3

data = pd.read_csv("data/student-mat.csv",sep=";")

conn = sqlite3.connect("database/student_risk.db")

data.to_sql("students", conn, if_exists="replace", index=False)

conn.close()

print("Database created successfully")