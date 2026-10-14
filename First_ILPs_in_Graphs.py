from docplex.mp.model import Model
import networkx as nx
import matplotlib.pyplot as plt

#---------------------------------------------------------------------
# Coloreo

#-----------------------------------------------
## Caso Particular (Grafo de Petersen)

# Definimos el grafo de Petersen
Petersen = nx.petersen_graph()

# Definimos el modelo de programación lineal para el problema
# de coloreo en el grafo de Petersen
modelo_petersen = Model(name='coloreo_petersen')

# Definimos la función max_grado que toma un grafo G y devuelve
# el grado máximo de sus nodos
def max_grado(G):
    grados = [G.degree(v) for v in G]
    return max(grados)

# Definimos el conjunto de colores CP
CP = range(0,max_grado(Petersen) + 1)

# Definimos las variables binarias X[v][k] y W[k] para el
# modelo de coloreo
X = [[modelo_petersen.binary_var(name='x_' + str(v) + '_' + str(k)) for k in CP] for v in Petersen]

W = [modelo_petersen.binary_var(name='w_' + str(k)) for k in CP]

# Definimos la función objetivo del modelo de coloreo
modelo_petersen.minimize(modelo_petersen.sum(W[k] for k in CP))

# Definimos las restricciones del modelo de coloreo
for v in Petersen:
    modelo_petersen.add_constraint(modelo_petersen.sum(X[v][k] for k in CP) == 1)

for u, v in Petersen.edges:
    for k in CP:
        modelo_petersen.add_constraint(X[u][k] + X[v][k] <= W[k])

# Resolvemos el modelo de coloreo para el grafo de Petersen
sol = modelo_petersen.solve()

# Imprimimos el resumen de la solución
sol.display()


#-----------------------------------------------
## Caso General 

# Definimos la función colorear que toma un grafo G y resuelve el
# problema de coloreo utilizando programación lineal entera
def colorear(G):
    # Inicializamos el modelo
    modelo = Model(name='coloreo') 

    # Definimos el conjunto de colores C
    C = range(0, max_grado(G) + 1)
    
    # Definimos las variables binarias X[v][k] y W[k]
    X = [[modelo.binary_var(name='x_' + str(v) + '_' + str(k)) for k in C] for v in G]
    W = [modelo.binary_var(name='w_' + str(k)) for k in C]
    
    # Definimos la función objetivo
    modelo.minimize(modelo.sum(W[k] for k in C))
    
    # Definimos las restricciones
    for v in G:
        modelo.add_constraint(modelo.sum(X[v][k] for k in C) == 1)

    for u, v in G.edges:
        for k in C:
            modelo.add_constraint(X[u][k] + X[v][k] <= W[k])
    
    # Resolvemos el modelo
    sol = modelo.solve()

    # Si no se encuentra solución, lanzamos una excepción
    assert sol, "No se encontró solución"

    # Imprimimos la solución
    sol.display()

    # Imprimimos el resumen de la solución
    resumen(modelo, sol)

# Definimos la función resumen que toma un modelo y una solución,
# e imprime un resumen de la solución obtenida
def resumen(modelo, sol):
    print("Variables: ", modelo.number_of_variables, ", ")
    print("Restricciones: ", modelo.number_of_constraints, ", ")
    print("Estado: ", modelo.solve_details.status, ", ")
    print("Tiempo: ", modelo.solve_details.time, "s, ")
    print("Gap: ", modelo.solve_details.gap, ", ")
    print("Valor: ", sol.get_objective_value())


# Definimos el grafo Q (grafo bull)
Q = nx.bull_graph()

# Dibujamos el grafo Q
# nx.draw(Q, with_labels=True)
# plt.show()

# Resolvemos el problema de coloreo para el grafo Q
colorear(Q)

#---------------------------------------------------------------------
# Dominación

# Definimos la función vecindario que toma un grafo G y un nodo v,
# y devuelve la lista de nodos vecinos de v en G
def vecindario(G, v):
    V = []
    for u in G.nodes():
        if G.has_edge(u, v):
            V.append(u)
    return V

# Definimos la función dominacion que toma un grafo G y resuelve el
# problema de dominación utilizando programación lineal entera
def dominacion(G):
    # Inicializamos el modelo
    modelo = Model(name='dominacion')

    # Definimos el conjunto de nodos del grafo G
    nodos = G.nodes()

    # Definimos las variables binarias X[v] para cada nodo v en G
    X = [modelo.binary_var(name='x_' + str(v)) for v in nodos]

    # Definimos la función objetivo
    modelo.minimize(modelo.sum(X[v] for v in nodos))

    # Definimos las restricciones del modelo de dominación
    for v in nodos:
        modelo.add_constraint(X[v] + modelo.sum(X[u] for u in vecindario(G, v)) >= 1)

    # Resolvemos el modelo
    sol = modelo.solve()

    # Si no se encuentra solución, lanzamos una excepción
    assert sol, "No se encontró solución"

    # Imprimimos la solución
    sol.display()

    # Imprimir resumen
    resumen(modelo, sol)

# Resolvemos el problema de dominación para el grafo de Petersen
dominacion(Petersen)
