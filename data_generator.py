import numpy as np
from datetime import datetime, timedelta

np.random.seed(2024)
DEMO_MODE = True  # Set True to trigger fast warnings for demo

START_DATE = datetime(2024, 1, 1, 0, 0, 0)

class TrainSensorStream:
    def __init__(self):
        self.time = START_DATE
        self.health = 1.0  # 1.0 = healthy, 0.0 = failure

    def degrade(self):
        if DEMO_MODE:
            self.health -= np.random.uniform(0.001, 0.003)  # FAST for demo
        else:
            self.health -= np.random.uniform(0.00001, 0.00005)  # realistic
        self.health = max(self.health, 0)

    def read_sensors(self):
        self.degrade()

        row = {
            "timestamp": self.time,
            "vibration": 2 + (1 - self.health) * 4 + np.random.normal(0, 0.2),
            "temperature": 60 + (1 - self.health) * 25 + np.random.normal(0, 0.4),
            "brake_pressure": 30 - (1 - self.health) * 6 + np.random.normal(0, 0.3),
            "motor_current": 200 + (1 - self.health) * 50 + np.random.normal(0, 3),
            "wheel_rpm": 1200 - (1 - self.health) * 120 + np.random.normal(0, 8),
            "health": self.health
        }

        self.time += timedelta(seconds=1)
        return row
