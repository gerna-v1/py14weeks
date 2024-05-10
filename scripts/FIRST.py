from tiempo import tiempoActual
from file import escribir, contar
from pathlib import Path
import os, logging, shutil

def primera(): #Funcion a ser usada cuando se inicia el codigo por primera vez
    try:
        try:
            Path(r'./data').mkdir()
            archivo = open('.\\data\\fecha.txt', 'x')
            archivo.close()
            escribir('fecha', True)
            archivo2 = open('.\\data\\ahorro.txt', 'w')
            archivo2.writelines(str(0))
            archivo2.close()
            contar('contar')
            archivo3 = open('.\\data\\tiempo.txt', 'x')
            escribir('tiempo', True)
            archivo3.close()


        except Exception as e:
            logging.error('Error at %s', exc_info=e)
            escribir('fecha', True)
        try:
            archivo2 = open('.\\data\\semanas.txt', 'x')
            archivo2.close()
        except:
            hola = 1
    except:
        return False

def segunda(eleccion, meta, modo):
    try:
        shutil.copy('cont.txt', '.\\data\\')
        os.remove('cont.txt')
        archivo2 = open('.\\data\\eleccion.txt', 'w')
        archivo2.writelines(eleccion)
        archivo2.close()

        archivo3 = open('.\\data\\meta.txt', 'w')
        archivo3.writelines(str(meta))
        archivo3.close()

        archivo4 = open('.\\data\\modo.txt', 'w')
        archivo4.writelines(str(modo))
        archivo4.close()
    except Exception as e:
        print(e)

def ultima():
    try:
        shutil.rmtree('.\\data')
        otravez = open('.\\cont.txt', 'w')
        otravez.writelines(str(-1))
        otravez.close()
    except Exception as e:
        otravez = open('.\\cont.txt', 'w')
        otravez.writelines(str(-1))
        otravez.close()
        print(e)

def chequeo():
    if os.path.exists('.\\data'):
        shutil.rmtree('.\\data')