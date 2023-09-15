class Bike():
    def wheels(self):
        print("Two Wheels")
    def speed(self):
        print("Allowed speed is 50 kmph")
    def test_bike(self):
        print("Test Bike")

class Car():
    def wheels(self):
        print("Four Wheels")
    def speed(self):
        print("Allowed Speed is 80 kmph")
    def greeting(self):
        print("Greeting from Car Class")

def func(ob):
    ob.wheels()
    ob.speed();
    ob.test_bike()

ob_bike = Bike()
ob_car = Car()

func(ob_bike)
func(ob_car)

