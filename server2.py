import random
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins

def generate_sensor_data():
    """Generate random livestock health parameters."""
    return {
        "temperature": round(random.uniform(36.0, 42.0), 1),
        "heart_rate": random.randint(40, 120),
        "activity": round(random.uniform(0.5, 3.0), 1)
    }

def analyze_health(temperature, heart_rate, activity):
    """Determine livestock health status based on input parameters."""
    if temperature > 39.5 or heart_rate > 100 or activity < 1.0:
        return "SICK"
    return "HEALTHY"

@app.route('/get_status', methods=['GET'])
def get_status():
    """Endpoint to get random livestock health status."""
    sensor_data = generate_sensor_data()
    sensor_data["status"] = analyze_health(sensor_data["temperature"], sensor_data["heart_rate"], sensor_data["activity"])
    return jsonify(sensor_data)

@app.route('/submit_data', methods=['POST'])
def submit_data():
    """Endpoint to process user input and return livestock health status."""
    data = request.json
    temperature = float(data.get("temperature", 0))
    heart_rate = int(data.get("heart_rate", 0))
    activity = float(data.get("activity", 0))

    status = analyze_health(temperature, heart_rate, activity)

    return jsonify({
        "temperature": temperature,
        "heart_rate": heart_rate,
        "activity": activity,
        "status": status
    })

if __name__ == '__main__':
    app.run(debug=True)
