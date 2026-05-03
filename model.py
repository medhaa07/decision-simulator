import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

model = None
feature_columns = None
target_column = None


def train_model(df, target):
    global model, feature_columns, target_column

    feature_columns = [col for col in df.columns if col != target]
    target_column = target

    X = df[feature_columns]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = LinearRegression()
    model.fit(X_train, y_train)


def predict(input_data):
    global model

    df = pd.DataFrame([input_data])
    return model.predict(df)[0]