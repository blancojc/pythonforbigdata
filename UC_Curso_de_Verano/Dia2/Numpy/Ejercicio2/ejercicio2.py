# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Leemos el fichero con loadtxt 
data = np.loadtxt('poblaciones.txt')

# Diferenciamos los datos
anhios     = data[:,0]
liebres    = data[:,1]
linces     = data[:,2]
zanahorias = data[:,3]

# 1. Representamos los datos
print( "1." )
plt.figure()
plt.plot( anhios, liebres)
plt.plot( anhios, linces)
plt.plot( anhios, zanahorias)
plt.legend( ['Liebres', 'Linces', 'Zanahorias'] ) 
plt.show()

# 2. Media y desviacion estandar
print( "2." )
print( "Liebres: media %f, std %f" % ( liebres.mean(), liebres.std() ) )
print( "Linces: media %f, std %f" % ( linces.mean(), linces.std() ) )
print( "Zanahorias: media %f, std %f" % ( zanahorias.mean(), zanahorias.std() ) )

# 3. Anhios de mayor poblacion
print( "3." )
print( "Anhio de mayor poblacion liebres %d" % anhios[np.argmax(liebres)] )
print( "Anhio de mayor poblacion linces %d" % anhios[np.argmax(linces)] )
print( "Anhio de mayor poblacion zanahorias %d" % anhios[np.argmax(zanahorias)] )

# 4. Mayor poblacion por anhio
especies  = np.array(['Liebres', 'Linces', 'Zanahorias'])
poblacion = data[:,1:]
print( "4." )
print( "Poblacion por anhio:\n")  
print( np.array( [ anhios, especies[ poblacion.argsort( )[:,-1] ] ] ).T )

#5. Anhio con mayor poblacion de 60000
print( "5." )
print( "Anhios con poblaciones superiores a 60000 ejemplares:\n") 
print( anhios[ np.any( poblacion > 60000, axis = 1 )  ] )

#6. Gradiente de liebres y número de linces
print( "6." )
grad_liebres = np.gradient( liebres )
plt.figure()
plt.plot( anhios, grad_liebres )
plt.plot( anhios, linces)
plt.legend( ['Gradiente de liebres', 'Linces'] )
plt.show()

print( "Correlacion entre el cambio de poblacion de liebres y linces:\n" )
print( np.corrcoef( grad_liebres, linces ) )

