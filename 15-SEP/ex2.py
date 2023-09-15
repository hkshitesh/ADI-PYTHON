class Car:
    def speed(self):
        print("Normal car speed is 60 kmph")

class bmw(Car):
    def speed(self):
        print(" BMW normal speed is 100 kmph")

class f1(Car):
    def speed(self):
        print("f1 normal speed is 200 kmph")

c= Car()
b = bmw()
f = f1()
c.speed()
b.speed()
f.speed()