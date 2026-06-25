# Student Performance Prediction using Multiple Linear Regression

This is a Machine Learning web application built using Flask and Multiple Linear Regression.
The application predicts a student's performance based on several input features such as study hours, previous scores, extracurricular activities, sleep hours, and sample question papers practiced.

## Features

* Predict student performance using trained ML model
* User-friendly web interface using Flask
* Real-time prediction based on user inputs
* Data preprocessing using StandardScaler

## Tech Stack

* Python
* Flask
* NumPy
* Pandas
* Scikit-learn
* HTML / CSS

## Project Structure

├── app.py
├── requirements.txt
├── Student_Performance.csv
│
├── models/
│   ├── linRegressor.pkl
│   └── scaler.pkl
│
└── templates/
└── index.html

## Installation

Clone the repository:

git clone <your-repo-link>

Move into project directory:

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

## Usage

1. Open the web application in browser
2. Enter:

   * Hours studied
   * Previous scores
   * Extracurricular activities
   * Sleep hours
   * Sample question papers practiced
3. Click Predict
4. Get predicted student performance score

## Machine Learning Model

* Algorithm: Multiple Linear Regression
* Preprocessing: StandardScaler
* Target: Student Performance Prediction

## Future Improvements

* Better UI design
* Model deployment on cloud
* Support for multiple ML algorithms
* Accuracy comparison with other regression models

