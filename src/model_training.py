import sqlite3
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def load_data():

    # connect to SQL database
    conn = sqlite3.connect("database/student_risk.db")

    query = """
    SELECT G1, failures, studytime, absences, Medu, famrel, traveltime, G3
    FROM students
    """

    df = pd.read_sql(query, conn)

    conn.close()

    return df


def prepare_data(df):

    # features
    X = df.drop("G3", axis=1)

    # target variable
    y = df["G3"]

    return X, y


def train_model(X_train, y_train):

    model = LinearRegression()

    model.fit(X_train, y_train)

    return model


def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)

    r2 = r2_score(y_test, predictions)

    print("\nModel Evaluation")

    print("Mean Squared Error:", mse)

    print("R2 Score:", r2)


def save_model(model):

    joblib.dump(model, "models/student_model.pkl")

    print("\nModel saved successfully in models/student_model.pkl")


if __name__ == "__main__":

    print("Loading data from SQL database...")

    df = load_data()

    print("Dataset shape:", df.shape)

    X, y = prepare_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("\nTraining model...")

    model = train_model(X_train, y_train)

    evaluate_model(model, X_test, y_test)

    save_model(model)