def generate_square():
    sq= []
    for i in range(1,6):
        square = i*i
        sq.append(square)
    return sq

#print(generate_square())

def generate_square_genrator(n):
    yield n*n

for i in range(1,6):
    print(next(generate_square_genrator(i)))