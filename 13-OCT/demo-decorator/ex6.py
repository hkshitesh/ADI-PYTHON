def division(a,b):
    print(a/b)


def decorator_division(func):
    def inner(x,y):
        if x<y:
            x,y = y,x
        return func(x,y)
    return inner


division = decorator_division(division)
division(10,5)

