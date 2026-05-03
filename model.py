import pandas as pd
from sklearn.linear_model import LinearRegression

model = None
features = []

def train_model(df, target):
    global model, features

    features = [col for col in df.columns if col != target]

    X = df[features]
    y = df[target]

    model = LinearRegression()
    model.fit(X, y)

def predict(input_data):
    global model, features

    df = pd.DataFrame([input_data])
    return model.predict(df)[0]