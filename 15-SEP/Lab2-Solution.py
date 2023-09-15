from abc import ABC, abstractmethod

class SensorData(ABC):
    @abstractmethod
    def get_data(self):
        pass

@SensorData.register
class TempratureData:
    def get_data(self):
        return {"Tempratute" : 25.5}

@SensorData.register
class HumidityData:
    def get_data(self):
        return {"Humidity ": 60.0}

@SensorData.register
class MotionData:
    def get_data(self):
        return {"Motion Detected ": True}

temp_data= TempratureData()
hum_data = HumidityData()
motion_data= MotionData()

sensor_data_objects= [temp_data,hum_data,motion_data]

for sensor_data in sensor_data_objects:
    data = sensor_data.get_data()
    print(f"{sensor_data.__class__.__name__} Data {data}")

