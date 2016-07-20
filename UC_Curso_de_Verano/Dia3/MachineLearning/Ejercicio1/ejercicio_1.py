import numpy as np
import matplotlib.pyplot as plt
from my_machine_learning import gradient_descent 

# Leemos el  dataset
data = np.loadtxt( 'ex1data1.txt', delimiter=',' )

X = data[:, 0]
y = data[:, 1]

# Ejercicio 1
# Representamos los datos 
plt.figure()
plt.scatter( X, y, marker = 'o', c = 'b' )
plt.xlabel( 'Poblacion de la ciudad' )
plt.ylabel( 'Beneficios')
plt.show()

# Ejercicio 2
# Numero de ejemplos del training
m = y.size

# Anhiadimos una columnas de 1
it = np.concatenate( (np.ones( (m, 1) ) , X.reshape(m, 1) ) , axis = 1 )

# Parametros 
theta = np.zeros(shape=(2, 1))
iterations = 1500
alpha = 0.01

theta, J_history = gradient_descent(it, y, theta, alpha, iterations)

# Valores de theta1 y theta2
print("Los valores theta1 y theta2 son:\n")
print(theta)

# Representamos los resultados 
plt.figure()
plt.scatter( X, y, marker='o', c = 'b' )
plt.xlabel( 'Poblacion de la ciudad' )
plt.ylabel( 'Beneficios')
result = it.dot(theta).flatten()
plt.plot(X, result, c = 'g' )
plt.show()
