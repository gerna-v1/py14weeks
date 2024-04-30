from tiempo import tiempoActual
from file import escribir, contar
def primera(): #Funcion a ser usada cuando se inicia el codigo por primera vez
    try:
        try:
            archivo = open('fecha.txt', 'x')
            archivo.close()
            escribir('fecha', True)
            contar('contar')
            archivo3 = open('tiempo.txt', 'x')
            escribir('tiempo', True)
            archivo3.close
        except:
            escribir('fecha', True)
        try:
            archivo2 = open('semanas.txt', 'x')
            archivo2.close()
        except:
            hola = 1
    except:
        return False