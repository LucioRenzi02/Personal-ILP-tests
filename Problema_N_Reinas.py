# Comenzamos importando los paquetes necesarios para llamar a CPLEX
import cplex
from docplex.mp.model import Model

# Guardamos el modelo en una variable de python de nombre "modelo"
# para referenciarlo más adelante
modelo = Model(name='queens')

# Número de Reinas y tamaño del tablero
N = 8
NN = range(8)

# Matriz de variables binarias que representan la posición de las reinas en el tablero
X = [[modelo.binary_var(name='x_'+ str(i) + '_' + str(j)) for i in NN] for j in NN]

# Definimos la función objetivo, que es maximizar el número de reinas colocadas en el tablero
fobj = modelo.sum(X[i][j] for i in NN for j in NN)

# Indicamos que es un problema de maximización
modelo.maximize(fobj)

# Agregamos las restricciones de que no puede haber más de una reina en cada fila y en cada columna
for i in NN:
    modelo.add_constraint(modelo.sum(X[i][j] for j in NN) <= 1)
for j in NN:
    modelo.add_constraint(modelo.sum(X[i][j] for i in NN) <= 1)


# Agregamos las restricciones de que no puede haber más de una reina en cada diagonal
DD = []
for i in NN:
    D1 = [((j+i) % N, j) for j in NN]
    for A in [D1[:N-i],D1[N-i:]]:
        if len(A) >= 2:
            DD.append(A)

for i in NN:
    D2 = [((N-1-j+i) % N, j) for j in NN]
    for A in [D2[:i],D2[i:]]:
        if len(A) >= 2:
            DD.append(A)

for D in DD:
    modelo.add_constraint(modelo.sum(X[i][j] for (i,j) in D) <= 1)

# Imprimimos información del modelo
modelo.print_information()

# Resolvemos el modelo y mostramos la solución
sol = modelo.solve(log_output=True)

# Si se encuentra una solución, la mostramos en pantalla
sol.display()