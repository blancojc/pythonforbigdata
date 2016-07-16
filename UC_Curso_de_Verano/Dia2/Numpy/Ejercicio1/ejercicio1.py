import numpy as np

#Apartado 1
array_D2 = np.arange(1,16).reshape(3,5).T
print( array_D2 )

#Apartado 2
print( np.array( [array_D2[1], array_D2[3]]) )
