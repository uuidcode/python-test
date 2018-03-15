def sum(a, b):
    s = a + b
    return s

def total(*numbers):
    s = 0

    for n in numbers:
        s += n

    return s



s = sum(1, 3)
print(s)

s = total(1, 2, 3)
print(s)

