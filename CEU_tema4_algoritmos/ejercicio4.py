import math

def bisection(f, a, b, tol=1e-6, max_iter=100):
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    return c, iter_count

def secant(f, x0, x1, tol=1e-6, max_iter=100):
    iter_count = 0
    while abs(x1 - x0) > tol and iter_count < max_iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, x2
        iter_count += 1
    return x2, iter_count

def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    iter_count = 0
    while abs(f(x0)) > tol and iter_count < max_iter:
        x0 = x0 - f(x0) / df(x0)
        iter_count += 1
    return x0, iter_count

def f(x):
    return x**3 - 6*x**2 + 11*x - 6

def df(x):
    return 3*x**2 - 12*x + 11

a, b = 0, 3
x0, x1 = 0, 3

result_bisection, iter_bisection = bisection(f, a, b)
result_secant, iter_secant = secant(f, x0, x1)
result_newton, iter_newton = newton_raphson(f, df, x0)

print("Bisección:")
print("Resultado:", result_bisection)
print("Iteraciones:", iter_bisection)

print("\nSecante:")
print("Resultado:", result_secant)
print("Iteraciones:", iter_secant)

print("\nNewton-Raphson:")
print("Resultado:", result_newton)
print("Iteraciones:", iter_newton)
