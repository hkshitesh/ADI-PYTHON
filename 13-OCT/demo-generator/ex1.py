def fn1():
    res = 10+20
    return res
print(fn1())

def fn2():
    yield 2
    yield 3
    yield 4

res = fn2()
print(next(res))
print(next(res))
print(next(res))

