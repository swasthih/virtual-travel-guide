from flask import Flask, render_template, jsonify
import requests
import joblib

app = Flask(__name__)

# Load the saved ML model
model = joblib.load('temperature_predictor.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather/<city>', methods=['GET'])
def weather(city):
    api_key = "9db37cf394e8d04acf480dc5b7a1f2ab"  # Replace with your OpenWeatherMap API key
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(weather_url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        condition = data['weather'][0]['description']

        # Get the features for the ML model
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind_speed = data['wind']['speed']
        features = [[humidity, pressure, wind_speed]]

        # Predict future temperature with the ML model
        predicted_temp = model.predict(features)[0]

        tips = f"Predicted future temperature: {predicted_temp:.2f}°C. Remember to plan accordingly based on the forecast!"

        return jsonify({
            "city": city,
            "temperature": temperature,
            "condition": condition,
            "predicted_temperature": predicted_temp,
            "tips": tips
        })
    else:
        return jsonify({"error": "City not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
