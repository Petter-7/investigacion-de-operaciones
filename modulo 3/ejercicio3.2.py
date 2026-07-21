from scipy.optimize import minimize

# Función de costo (a minimizar)

def costo(x, y):
    return x**2 + y**2 + x*y + 25000*x + 35000*y + 500000

# scipy minimiza directamente el costo

def costo_total(v):
    x, y = v
    return costo(x, y)

limites = [(0, None), (0, None)]   # x >= 0, y >= 0

iteracion = [0]

def mostrar_avance(v):
    iteracion[0] += 1
    x, y = v
    print(f"Iteración {iteracion[0]}: x={x:.4f}, y={y:.4f}, costo=${costo(x,y):,.2f}")

resultado = minimize(
    costo_total,
    x0=[0, 0],
    method='L-BFGS-B',
    callback=mostrar_avance,
    bounds=limites
)

x_opt, y_opt = resultado.x
costo_min = resultado.fun

print(f"\nSitios web óptimos: {x_opt:.2f} (cientos)")
print(f"Terabytes óptimos: {y_opt:.2f} (cientos)")
print(f"Costo mínimo: ${costo_min:,.2f}")