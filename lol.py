__author__ = 'Line'

def heyhey(x):
    return x + 1

def fact(n):
    if n<1:
        return 1
    else:
        return n * fact(n-1)

print(fact(4))
print