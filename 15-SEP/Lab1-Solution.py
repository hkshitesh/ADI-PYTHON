import random
from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def read_data(self):
        pass

class TempratureSensor(Sensor):
    def read_data(self):
        temp = round(random.uniform(20,30),2)
        return {"Temprature= ":temp}

class HumiditySensor(Sensor):
    def read_data(self):
        humidity = round(random.uniform(40,60),2)
        return {"Humidity : ":humidity}

class MotionSensor(Sensor):
    def read_data(self):
        motion = random.choice([True,False])
        return {"Motion_Detected : ":motion}

temp_sensor = TempratureSensor()
humidity_sensor = HumiditySensor()
motion_sensor = MotionSensor()

sensors = [temp_sensor,humidity_sensor,motion_sensor]

for sensor in sensors:
    data = sensor.read_data()
    print(f" {sensor.__class__.__name__} Data : {data}")
