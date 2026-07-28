from scipy.optimize import minimize

def costo(v):
    x, y = v
    return x**2 + y**2 + x*y + 25000*x + 35000*y + 500000

iteracion = [0]

def mostrar_avance(v):
    iteracion[0] += 1
    x, y = v
    print(f"Iteración {iteracion[0]}: x={x:.4f}, y={y:.4f}, costo=${costo(v):,.2f}")

resultado = minimize(
    costo,
    x0=[1,1],
    method='BFGS',
    callback=mostrar_avance
)

print("\nMétodo CG")
print("x =", resultado.x[0])
print("y =", resultado.x[1])
print("Costo mínimo =", resultado.fun)