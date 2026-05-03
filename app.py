from flask import Flask, render_template, request, jsonify
import pandas as pd
from model import train_model, predict

app = Flask(__name__)

data = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    global data
    file = request.files["file"]
    data = pd.read_csv(file)
    return jsonify({"message": "File uploaded!"})

@app.route("/train", methods=["POST"])
def train():
    target = request.json["target"]
    train_model(data, target)
    return jsonify({"message": "Model trained!"})

@app.route("/simulate", methods=["POST"])
def simulate():
    input_data = request.json["input"]
    result = predict(input_data)
    return jsonify({"prediction": float(result)})

if __name__ == "__main__":
    app.run(debug=True)