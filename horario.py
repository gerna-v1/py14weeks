def meses31(mes):
    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        return True
    else:
        return False
def meses30(mes):
    if (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        return True
    else:
        return False

def comparacion(mes):
    if meses31(mes):
        resultado = 1 #resultado es 1 si el mes termina en 31
        return resultado
    elif meses30(mes):
        resultado = 2 #resultado es 2 si el mes termina en 30
        return resultado
    else:
        return None
