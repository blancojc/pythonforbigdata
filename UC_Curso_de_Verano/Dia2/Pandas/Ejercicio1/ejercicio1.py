import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Leemos los datos
estaciones = pd.read_csv( 'estaciones.csv', skipinitialspace = True, na_values=np.nan )
precip = pd.read_csv( 'precipitaciones.csv', skipinitialspace = True, na_values=np.nan )

# 1. Apartado
# Creamos una serie con las fechas
fechas = pd.DatetimeIndex( precip['YYYYMMDD'] )

# Creamos un nuevo dataset anhadiendo years y months
tmp_precip = precip.copy().drop( 'YYYYMMDD', axis = 1 )
tmp_precip['year'] = fechas.year
tmp_precip['month'] = fechas.month

# Calculamos las medias por estacion y anhio y mes
media_x_anhio_y_estacion = tmp_precip.drop( 'month', axis = 1 ).groupby( 'year' ).mean()
media_x_month_y_estacion = tmp_precip.groupby( [ 'year', 'month'] ).mean()

# Media por anhio 
media_anhio = media_x_anhio_y_estacion.mean( axis = 1 )

# Media por mes
media_mes = media_x_month_y_estacion.mean( axis = 1 )

# Graficas
plt.figure()
plt.plot( media_anhio )
plt.title( "Precipitacion media anual" )
plt.show()

plt.figure()
plt.plot( media_mes )
plt.title( "Precipitacion media mensual" )
plt.show()

# 2. Apartado
# Distribucion espacial de las estaciones

plt.figure()
plt.scatter( estaciones['longitude'], estaciones['latitude'] )
plt.title( "Estaciones meteorologicas" )
plt.show()

# 3. Apartado

# Eliminamos del dataset YYYYMMDD
tmp_precip = precip.copy().drop( 'YYYYMMDD', axis = 1 )

# Mayores de 10, suma y media
frecuencia_mayores_10 = tmp_precip.gt(10).sum().mean() 
print("La frencuencia de dias con precipitaciones > 10 mm : %f" % frecuencia_mayores_10 )
