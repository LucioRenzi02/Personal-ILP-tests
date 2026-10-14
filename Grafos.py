import networkx as nx
import matplotlib.pyplot as plt

#---------------------------------------------------------------------
# Actividad 1

# Generamos un grafo G
G = nx.Graph()

# Agregamos los nodos y las aristas al grafo
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5), (1, 3), (1, 5), (3, 5)])

# Dibujamos el grafo G
# nx.draw(G, with_labels=True)
# plt.show()

#---------------------------------------------------------------------
# Actividad 2

# Generamos un grafo hipercubo
H = nx.hypercube_graph(4)

# Dibujamos el grafo hipercubo
# nx.draw(H, with_labels=True)
# plt.show()

#---------------------------------------------------------------------
# Actividad 3

# Definimos la función es_clique que verifica si un conjunto
# de nodos C forma un clique en el grafo G
def es_clique(G, C):
    for i in range(len(C)):
        for j in range(i + 1, len(C)):
            if not G.has_edge(C[i], C[j]):
                return False
    return True

#---------------------------------------------------------------------
# Actividad 4

# Definimos la función maximalizar_clique que toma un grafo G
# y una clique C dentro de G, y devuelve una clique maximal que
# contiene a C
def maximalizar_clique(G, C):
    M = list(C)
    for v in G:
        if v not in M:
            ok = True
            for u in M:
                if not G.has_edge(v,u):
                    ok = False
            if ok:
                M.append(v)
    return M

#---------------------------------------------------------------------
# Actividad 5

# Definimos la función vecindario que toma un grafo G y un nodo u,
# y devuelve la lista de nodos vecinos de u en G
def vecindario(G, u):
    V = []
    for v in G:
        if G.has_edge(v,u):
            V.append(v)
    return(V)

# Definimos la función es_coloreo que toma un grafo G y
# y un diccionario f que asigna un color a cada nodo, y luego
# verifica si f es un coloreo válido de G
def es_coloreo(G,f):
    es = True
    for u in G:
        for v in vecindario(G, u):
            if f[u] == f[v]:
                es = False
    return es
