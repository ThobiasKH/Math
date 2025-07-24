import math

def f(x):
    return 4 + 2 * x * math.tan(x)

def trapezoidal_rule(a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))  
    for i in range(1, n):
        result += f(a + i * h)  
    result *= h  
    return result

a = 0
b = math.pi / 4
n = 25

integral_value = trapezoidal_rule(a, b, n)

print(f'Tilnærmet verdi av integralet: {integral_value}')

def f(x):
    return x**4 - 3*x*x + x + 1/2

def df(x):
    return 4*x**3 - 6*x + 1

xN = 3 
def findZero(xN, f, df, tolerance = 0.000000001):
    xNext = xN - f(xN) / df(xN)
    if (abs(xNext - xN) < tolerance):
        return xNext
    return findZero(xNext, f, df, tolerance)

print(f"Start value for x: {xN}")
print(findZero(xN, f, df))
