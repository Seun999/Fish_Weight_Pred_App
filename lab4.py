import pandas as pd
import numpy as np
from flask import Flask, request, jsonify

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset
url = 'https://raw.githubusercontent.com/Seun999/datasets/main/Fish.csv'
df = pd.read_csv(url)

# Check for missing values
df.dropna(inplace=True)

# One-hot encode the 'Species' column
df = pd.get_dummies(df, columns=['Species'])

# Split the data into features (X) and the target variable (y)
X = df.drop('Weight', axis=1)
y = df['Weight']

# Create and train the regression model
model = LinearRegression()
model.fit(X, y)

# Create the Flask app
app = Flask(__name__)

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract the input features from the JSON data
    species = data['Species']
    length1 = data['Length1']
    length2 = data['Length2']
    length3 = data['Length3']
    height = data['Height']
    width = data['Width']

    # Encode the species input using one-hot encoding
    species_bream = 1 if species == 'Bream' else 0
    species_parkki = 1 if species == 'Parkki' else 0
    species_perch = 1 if species == 'Perch' else 0
    species_pike = 1 if species == 'Pike' else 0
    species_roach = 1 if species == 'Roach' else 0
    species_smelt = 1 if species == 'Smelt' else 0
    species_whitefish = 1 if species == 'Whitefish' else 0

    # Prepare the input data for prediction
    input_data = np.array([[length1, length2, length3, height, width,
                            species_bream, species_parkki, species_perch,
                            species_pike, species_roach, species_smelt,
                            species_whitefish]])

    # Perform the prediction
    prediction = model.predict(input_data)

    # Create a response JSON with the prediction result
    response = {
        'predicted_weight': prediction[0]
    }

    return jsonify(response)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
