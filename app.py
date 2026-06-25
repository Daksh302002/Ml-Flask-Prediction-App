from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle

app = Flask(__name__)


scaler = pickle.load(open("models/scaler.pkl", 'rb'))
linRegressor = pickle.load(open("models/linRegressor.pkl", 'rb'))


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':

        Hours = float(request.form['Hours'])
        Previous_Scores = float(request.form['Previous_Scores'])
        Extracurricular = float(request.form['Extracurricular_Activities'])
        Sleep_Hours = float(request.form['Sleep_Hours'])
        Practice = float(request.form['Sample_Question_Papers_Practiced'])

        features = np.array([[Hours, Previous_Scores,
                              Extracurricular, Sleep_Hours, Practice]])

        scaled_features = scaler.transform(features)
        prediction = linRegressor.predict(scaled_features)

        return render_template("index.html", prediction=prediction[0])

    return render_template("index.html")   # ✅ REQUIRED



if __name__ == "__main__":
    app.run()
