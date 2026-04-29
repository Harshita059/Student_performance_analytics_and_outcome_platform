import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    conn = sqlite3.connect("database/student_risk.db")
    df = pd.read_sql("SELECT * FROM students", conn)
    return df


def basic_info(df):
    print("First 5 rows:\n")
    print(df.head())

    print("\nShape of dataset:")
    print(df.shape)

    print("\nColumn Names:\n")
    print(df.columns)

    print("\nMissing values:\n")
    print(df.isnull().sum())

    print("\nDuplicate rows:")
    print(df.duplicated().sum())


def eda_analysis(df):

    print("\nG3 Summary Statistics:\n")
    print(df["G3"].describe())

    plt.figure()
    df["G3"].hist()
    plt.title("Distribution of Final Grades (G3)")
    plt.xlabel("Final Grade")
    plt.ylabel("Frequency")
    plt.show()

    print("\nAverage G3 by Study Time:\n")
    print(df.groupby("studytime")["G3"].mean())

    plt.figure()
    sns.boxplot(x="studytime", y="G3", data=df)
    plt.title("Study Time vs Final Grade")
    plt.show()

    print("\nCorrelation between Absences and G3:")
    print(df["absences"].corr(df["G3"]))

    plt.figure()
    sns.scatterplot(x="absences", y="G3", data=df)
    plt.title("Absences vs Final Grade")
    plt.show()

    print("\nAverage G3 by Failures:\n")
    print(df.groupby("failures")["G3"].mean())

    plt.figure()
    sns.boxplot(x="failures", y="G3", data=df)
    plt.title("Failures vs Final Grade")
    plt.show()

    plt.figure()
    sns.scatterplot(x="G1", y="G3", data=df)
    plt.title("G1 vs G3")
    plt.show()

    plt.figure()
    sns.scatterplot(x="G2", y="G3", data=df)
    plt.title("G2 vs G3")
    plt.show()

    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

    print("\nCorrelation with G3 (Sorted):\n")
    print(df.corr(numeric_only=True)["G3"].sort_values(ascending=False))


if __name__ == "__main__":
    df = load_data()
    basic_info(df)
    eda_analysis(df)