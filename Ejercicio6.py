import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Storage_Optimization", pulp.LpMinimize)

# 2. Variables de decisión
x = pulp.LpVariable("Almacenamiento_Estandar", lowBound=0, cat='Continuous')
y = pulp.LpVariable("Almacenamiento_Premium", lowBound=0, cat='Continuous')

# 3. Función objetivo
model += 20 * x + 60 * y, "Costo_Total"

# 4. Restricciones

# Velocidad mínima
model += x + 3 * y >= 15, "IOPS_Minimos"

# Retención mínima
model += x + y >= 7, "Retencion_Minima"

# 5. Resolver
model.solve()

# 6. Resultados
print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"TB Estándar: {x.varValue}")
print(f"TB Premium: {y.varValue}")
print(f"Costo mínimo mensual: ${pulp.value(model.objective)} USD")