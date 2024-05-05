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
def meses29(mes,ano):
    if mes == 2:
        if (int(ano) % 4 == 0 and int(ano) % 100 != 0) or (int(ano) % 4 != 0 and int(ano) % 400 == 0):
            return '1'
        else:
            return '2'

def comparacion(mes,ano='2024'):
    if meses31(int(mes)):
        resultado = 1 #resultado es 1 si el mes termina en 31
        return resultado
    elif meses30(int(mes)):
        resultado = 2 #resultado es 2 si el mes termina en 30
        return resultado
    elif meses29(int(mes),ano) == '1':
        resultado = 3 #resultado es 3 si el mes febrero termina en 29
        return resultado
    elif meses29(int(mes),ano) == '2':
        resultado = 4 #resultado es 4 si el mes febrero termina en 28
        return resultado
    else:
        return None
