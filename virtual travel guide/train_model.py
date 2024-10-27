# train_model.py
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

# Simulated dataset with example data (use actual data if available)
data = pd.DataFrame({
    'humidity': [65, 70, 85, 80, 90],
    'pressure': [1012, 1010, 1008, 1015, 1013],
    'wind_speed': [4, 5, 3, 4, 6],
    'temperature': [25, 26, 28, 27, 29]  # Target variable
})

# Define the features (X) and the target (y)
X = data[['humidity', 'pressure', 'wind_speed']]
y = data['temperature']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Save the trained model
joblib.dump(model, 'temperature_predictor.pkl')
print("Model trained and saved successfully!")
