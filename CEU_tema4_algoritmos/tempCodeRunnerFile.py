import numpy as np
import matplotlib.pyplot as plt

# Definir la función para la cual quieres encontrar la raíz
def f(x):
    return x**3 - 6*x**2 + 11*x - 6

# Derivada de la función
def df(x):
    return 3*x**2 - 12*x + 11

# Método de bisección
def bisection(a, b, tol, max_iter):
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

# Método de la secante
def secant(x0, x1, tol, max_iter):
    iter_count = 0
    
    while iter_count < max_iter:
        fx0 = f(x0)
        fx1 = f(x1)
        
        if abs(fx1 - fx0) < tol:
            break  # Avoid division by nearly zero difference
          
        x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        
        if abs(f(x2)) < tol:
            break  # We found a good approximation
          
        x0, x1 = x1, x2
        iter_count += 1
    
    return x2, iter_count


# Método de Newton-Raphson
def newton_raphson(x0, tol, max_iter):
    iter_count = 0
    while abs(f(x0)) > tol and iter_count < max_iter:
        x0 = x0 - f(x0) / df(x0)
        iter_count += 1
    return x0, iter_count

# Configurar parámetros iniciales
a, b = 0, 3
x0, x1 = 1, 2
tol = 1e-6
max_iter = 1000

# Aplicar los métodos
root_bisection, iter_bisection = bisection(a, b, tol, max_iter)
root_secant, iter_secant = secant(x0, x1, tol, max_iter)
root_newton, iter_newton = newton_raphson(x1, tol, max_iter)

# Mostrar resultados
print("Bisection:")
print("Root:", root_bisection)
print("Iterations:", iter_bisection)

print("\nSecant:")
print("Root:", root_secant)
print("Iterations:", iter_secant)

print("\nNewton-Raphson:")
print("Root:", root_newton)
print("Iterations:", iter_newton)

# Graficar la función
x_vals = np.linspace(a, b, 100)
plt.plot(x_vals, f(x_vals), label='f(x)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.scatter([root_bisection, root_secant, root_newton], [0, 0, 0], color='red', label='Roots')
plt.legend()
plt.show()
