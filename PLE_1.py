from docplex.mp.model import Model
import networkx as nx
import matplotlib.pyplot as plt

# Coloreo

## Caso Particular (Petersen)

"""
Petersen = nx.petersen_graph()

modelo_petersen = Model(name='coloreo_petersen')

def max_grado(G):
    grados = [G.degree(v) for v in G]
    return max(grados)

CP = range(0,max_grado(Petersen) + 1)

X = [[modelo_petersen.binary_var(name='x_' + str(v) + '_' + str(k)) for k in CP] for v in Petersen]

W = [modelo_petersen.binary_var(name='w_' + str(k)) for k in CP]

modelo_petersen.minimize(modelo_petersen.sum(W[k] for k in CP))

for v in Petersen:
    modelo_petersen.add_constraint(modelo_petersen.sum(X[v][k] for k in CP) == 1)

for u, v in Petersen.edges:
    for k in CP:
        modelo_petersen.add_constraint(X[u][k] + X[v][k] <= W[k])

sol = modelo_petersen.solve(log_output=True)
sol.display()
"""

# Caso General 
"""
def max_grado(G):
    grados = [G.degree(v) for v in G]
    return max(grados)

def colorear(G):
    modelo = Model(name='coloreo') # Inicializamos el modelo 

    C = range(0, max_grado(G) + 1)  # Conjunto de colores
    
    # Variables
    X = [[modelo.binary_var(name='x_' + str(v) + '_' + str(k)) for k in C] for v in G]
    W = [modelo.binary_var(name='w_' + str(k)) for k in C]
    
    # Funcion objetivo
    modelo.minimize(modelo.sum(W[k] for k in C))
    
    # Restricciones
    for v in G:
        modelo.add_constraint(modelo.sum(X[v][k] for k in C) == 1)
    for u, v in G.edges:
        for k in C:
            modelo.add_constraint(X[u][k] + X[v][k] <= W[k])
    
    # Resolver modelo
    sol = modelo.solve() # No imprimimos el log
    
    assert sol, "No se encontró solución"
    
    # Imprimir resumen
    resumen(modelo, sol)
    
def resumen(modelo, sol):
    print(
        "Variables: ", modelo.number_of_variables, ", ",
        "Restricciones: ", modelo.number_of_constraints, ", ",
        "Estado: ", modelo.solve_details.status, ", ",
        "Tiempo: ", modelo.solve_details.time, "s, ",
        "Gap: ", modelo.solve_details.gap, ", ",
        "Valor: ", sol.get_objective_value()
    )


Q = nx.bull_graph()

nx.draw(Q, with_labels=True)
plt.show()

colorear(Q)
"""


# Actividad 2

GP = nx.Graph()

GP.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (0, 4)])
GP.add_edges_from([(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)])
GP.add_edges_from([(5, 7), (7, 9), (6, 9), (6, 8), (5, 8)])

nx.draw(GP, with_labels=True)
plt.show()

def vecindario(G, v):
    V = []
    for u in G.nodes():
        if G.has_edge(u, v):
            V.append(u)
    return V

def dominacion(G):
    modelo = Model(name='dominacion') # Inicializamos el modelo

    nodos = G.nodes()

    # Variables
    X = [modelo.binary_var(name='x_' + str(v)) for v in nodos]

    # Funcion objetivo
    modelo.minimize(modelo.sum(X[v] for v in nodos))

    # Restricciones
    for v in nodos:
        modelo.add_constraint(X[v] + modelo.sum(X[u] for u in vecindario(G, v)) >= 1)

    # Resolver modelo
    sol = modelo.solve() # No imprimimos el log
    sol.display()
    
    assert sol, "No se encontró solución"
        
    # Imprimir resumen
    resumen(modelo, sol)
        
def resumen(modelo, sol):
    print(
        "Variables: ", modelo.number_of_variables, ", ",
        "Restricciones: ", modelo.number_of_constraints, ", ",
        "Estado: ", modelo.solve_details.status, ", ",
        "Tiempo: ", modelo.solve_details.time, "s, ",
        "Gap: ", modelo.solve_details.gap, ", ",
        "Valor: ", sol.get_objective_value())

dominacion(GP)