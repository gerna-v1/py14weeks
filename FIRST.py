from tiempo import tiempoActual
from file import escribir, contar
def primera():
    try:
        try:
            archivo = open('fecha.txt', 'x')
            archivo.close()
            escribir('fecha', True)
            contar('contar')
        except:
            escribir('fecha', True)
        try:
            archivo2 = open('semanas.txt', 'x')
            archivo2.close()
        except:
            hola = 1
    except:
        return False