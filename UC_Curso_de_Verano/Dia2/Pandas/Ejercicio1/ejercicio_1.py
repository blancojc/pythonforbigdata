nucleos_de_poblacion = pd.read_csv( "https://raw.githubusercontent.com/blancojc/pythonforbigdata/master/UC_Curso_de_Verano/Dia2/Pandas/Ejercicio1/Centroides_NucleosPoblacion.csv" )

# Municipios con memos de 11000 habitantes
nucleos_de_poblacion[ nucleos_de_poblacion[ 'Poblacion' ] < 11000 ][ 'Municipio' ]
# O
nucleos_de_poblacion[ nucleos_de_poblacion[ 'Poblacion' ].lt( 11000 ) ][ 'Municipio' ]

# Quinto municipio mas poblado
nucleos_de_poblacion.sort_values( 'Poblacion' ).iloc[ -5  ]

# 5 municipios de menor poblacion
nucleos_de_poblacion.sort_values( 'Poblacion' ).iloc[ 0 : 5 ]
