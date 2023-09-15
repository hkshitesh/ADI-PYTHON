from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
class Triangle(Polygon):
    def sides(self):
        print("Triangle has three sides")
class Square(Polygon):
    def sides(self):
        print("Square has four equal sides")
class Pentagon(Polygon):
    def sides(self):
        print("Square has Five equal sides")
    def test(self):
        print("testing")

t = Triangle()
s = Square()
p = Pentagon()

t.sides()
s.sides()
p.sides()
