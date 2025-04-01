from flask import Flask, request, jsonify

app = Flask(__name__)

# Store sensor data in memory
sensor_data = []
import threading
import time
import random

def generate_sensor_data():
    while True:
        sensor_data.append({
            "temperature": round(random.uniform(20, 35), 2),
            "humidity": round(random.uniform(40, 70), 2)
        })
        time.sleep(5)  # New data every 5 seconds

# Start generating data in the background
threading.Thread(target=generate_sensor_data, daemon=True).start()


@app.route('/send-data', methods=['POST'])
def receive_data():
    data = request.json
    if "temperature" in data and "humidity" in data:
        sensor_data.append(data)
        return jsonify({"message": "Data received!"}), 200
    return jsonify({"error": "Invalid data"}), 400

@app.route('/get-data', methods=['GET'])
def get_data():
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(debug=True)
