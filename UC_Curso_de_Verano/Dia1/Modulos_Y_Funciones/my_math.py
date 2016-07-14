def media(*arg):
    """Calcula la media
    """
    n = len(arg)
    if n < 1:
        raise ValueError('La media requiere al menos 1 valor')
    return sum(arg) / len(arg)

def varianza(*arg):
    """Calcula la varianza
    """
    n = len(arg)
    if n < 2:
        raise ValueError('La varianza requiere al menos dos valores')
    return sum((media(*arg) - value) ** 2 for value in arg) / n

def desviacion_std(*arg):
    """Calcula la desviacion estandar
    """
    return varianza(*arg)**0.5

    