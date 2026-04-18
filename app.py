from flask import Flask, render_template, jsonify
import random
import time
from datetime import datetime

app = Flask(__name__)

# Simple storage for sensor data
sensor_data = {
    'vibration': [],
    'temperature': [],
    'brake': [],
    'motor': [],
    'rpm': []
}

# Train health starts at 100%
train_health = 100
counter = 0

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/get_data')
def get_data():
    global train_health, counter
    
    # Make train slowly break down
    counter += 1
    if counter % 10 == 0:  # Every 10 seconds
        train_health -= random.randint(1, 3)
        if train_health < 0:
            train_health = 0
    
    # Generate sensor readings based on health
    new_data = {
        'time': datetime.now().strftime('%H:%M:%S'),
        'vibration': round(2 + (100 - train_health) * 0.1 + random.uniform(-0.5, 0.5), 1),
        'temperature': round(60 + (100 - train_health) * 0.3 + random.uniform(-1, 1), 1),
        'brake': round(30 - (100 - train_health) * 0.1 + random.uniform(-0.5, 0.5), 1),
        'motor': round(200 + (100 - train_health) * 0.5 + random.uniform(-2, 2), 1),
        'rpm': round(1200 - (100 - train_health) * 2 + random.uniform(-5, 5), 1),
        'health': train_health
    }
    
    # Add to history
    for key in sensor_data:
        sensor_data[key].append({
            'time': new_data['time'],
            'value': new_data[key]
        })
        # Keep last 20 readings only
        if len(sensor_data[key]) > 20:
            sensor_data[key].pop(0)
    
    # Simple alert logic
    alert = None
    if train_health < 30:
        alert = {
            'level': 'CRITICAL',
            'message': 'TRAIN NEEDS MAINTENANCE NOW!',
            'color': 'red'
        }
    elif train_health < 60:
        alert = {
            'level': 'WARNING',
            'message': 'Schedule maintenance soon',
            'color': 'orange'
        }
    elif train_health < 85:
        alert = {
            'level': 'INFO',
            'message': 'Keep monitoring',
            'color': 'blue'
        }
    
    return jsonify({
        'current': new_data,
        'history': sensor_data,
        'alert': alert
    })

if __name__ == '__main__':
    print("Starting Train Monitor...")
    print("Open http://127.0.0.1:5000 in your browser")
    app.run(debug=True)