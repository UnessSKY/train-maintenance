# Train Predictive Maintenance System

A real-time predictive maintenance system for train monitoring using machine learning and a web dashboard.

## Features

- **Real-time Sensor Monitoring**: Simulates and monitors train sensors including vibration, temperature, brake pressure, motor current, and wheel RPM.
- **Predictive Analytics**: Uses machine learning models to predict equipment failure probability and remaining useful life (RUL).
- **Web Dashboard**: Interactive dashboard with live charts and alerts for maintenance decisions.
- **Alert System**: Automatic alerts based on train health status (INFO, WARNING, CRITICAL).

## Project Structure

```
siana projects/
├── app.py                 # Flask web application
├── data_generator.py      # Sensor data simulation
├── model.py               # Machine learning models
├── requirements.txt       # Python dependencies
├── static/
│   └── charts.js          # JavaScript for chart updates
├── templates/
│   └── dashboard.html     # HTML dashboard template
├── tests/
│   └── data_generator.py  # Tests for data generator
└── README.md              # This file
```

## Installation

1. **Clone or download the project**:
   ```
   cd path/to/projects/siana projects
   ```

2. **Install dependencies**:
   Make sure you have Python 3.7+ installed. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```
   python app.py
   ```

4. **Open in browser**:
   Navigate to `http://127.0.0.1:5000`

## Usage

- The dashboard displays real-time sensor data and health metrics.
- Charts update every second with new sensor readings.
- Alerts appear based on train health:
  - **INFO**: Health > 85% - Keep monitoring
  - **WARNING**: Health 60-85% - Schedule maintenance soon
  - **CRITICAL**: Health < 30% - Train needs maintenance now!

## Models

- **Failure Prediction**: Gradient Boosting Classifier trained on sensor data to predict failure probability.
- **Remaining Useful Life (RUL)**: Random Forest Regressor to estimate time until failure.

The models start training after collecting 200 data points and update continuously.

## Demo Mode

The system includes a demo mode that accelerates degradation for demonstration purposes. Set `DEMO_MODE = False` in `data_generator.py` for realistic simulation.

## Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: scikit-learn
- **Frontend**: HTML, JavaScript, Chart.js
- **Data Processing**: NumPy

## Contributing

Feel free to fork and contribute improvements!

## License

This project is open-source. Use at your own risk.