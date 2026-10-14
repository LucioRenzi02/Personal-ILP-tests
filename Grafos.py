import networkx as nx
import matplotlib.pyplot as plt

# Actividad 1


G = nx.Graph()

G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5), (1, 3), (1, 5), (3, 5)])

nx.draw(G, with_labels=True)
plt.show()

# Actividad 2
"""
H = nx.hypercube_graph(4)

nx.draw(H, with_labels=True)
plt.show()

"""

# Actividad 3

"""
def es_clique(G, C):
    for i in range(len(C)):
        for j in range(i + 1, len(C)):
            if not G.has_edge(C[i], C[j]):
                return False
    return True
"""

# Actividad 4

"""
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
"""

# Actividad 5

"""
def vecindario(G, u):
    V = []
    for v in G:
        if G.has_edge(v,u):
            V.append(v)
    return(V)

def es_coloreo(G,f):
    es = True
    for u in G:
        for v in vecindario(G, u):
            if f[u] == f[v]:
                es = False
    return es
"""