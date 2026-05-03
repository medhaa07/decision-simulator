from flask import Flask, render_template, request, jsonify
import pandas as pd
from model import train_model, predict

app = Flask(__name__)

data = None
target_column = None


@app.route("/")
def home():
    return render_template("index.html")


# Upload dataset
@app.route("/upload", methods=["POST"])
def upload():
    global data
    file = request.files["file"]
    data = pd.read_csv(file)

    return jsonify({
        "message": "Uploaded successfully",
        "columns": list(data.columns)
    })


# Train model
@app.route("/train", methods=["POST"])
def train():
    global data, target_column

    target_column = request.json["target"]

    train_model(data, target_column)

    return jsonify({"message": "Model trained successfully"})


# WHAT-IF SIMULATION 🔥
@app.route("/simulate", methods=["POST"])
def simulate():
    input_data = request.json["input"]

    result = predict(input_data)

    return jsonify({
        "prediction": float(result)
    })


if __name__ == "__main__":
    app.run(debug=True)