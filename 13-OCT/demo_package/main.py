from demo_package.two_d import area, perimeter
from demo_package.three_d import volume, surface_area

l=5
b=4
ar= area.calculate_area(l,b)
per= perimeter.caluculate_aparameter(l,b)
print("Area is :",ar)
print("Perimeter is :",per)

l=5
b=4
h=2
vol= volume.calculate_volume(l,b,h)
sur= surface_area.calculate_surface_area(l,b,h)
print("Volume is :",vol)
print("Surface Area is :",sur)