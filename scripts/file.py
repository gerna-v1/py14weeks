from tiempo import tiempoActual
import os
def escribir(nomArchivo, t): #Sobreescribe o crea el contenedor de la fecha
    variante = nomArchivo
    if nomArchivo.lower() == 'fecha' or nomArchivo.lower() == 'tiempo':
        if t:
            archivo = open('.\\data\\' + str(nomArchivo) + '.txt', 'w')
        else:
            archivo = open('.\\data\\' + str(nomArchivo)+'_temp'+'.txt', 'w')
        array = tiempoActual(str(variante))
        for i in range(0,3):
            if i == 3:
                archivo.write(str(array[i]))
            else:
                archivo.write(str(array[i]) + '\n')
        archivo.close()
    else:
        return None
def leer(nomArchivo, t): #Lee y retorna los contenidos del archivo de fecha
    try:
        if t:
            archivo = open('.\\data\\' + str(nomArchivo)+'.txt', 'r')
        else:
            archivo = open('.\\data\\' + str(nomArchivo)+'_temp'+'.txt', 'r')
        lectura = archivo.readlines()
        mod = []

        for line in lectura:
            if line[-1] == '\n':
                mod.append(line[:-1])
            else:
                mod.append(line)
        archivo.close()
        return mod
        #FALTA FUNCION PARA COMPARAR CON UN HORARIO
    except FileNotFoundError:
        print('Error: Archivo inexistente')
def contar(accion): #Agrega uno al contador global o retorna el valor actual

    try:
        temp = open('cont.txt', 'r')
        comprobacion = temp.readlines()
        if int(comprobacion[0]) == -1:
            camino = ''
            camino2 = '.\\data\\'
        else:
            camino = '.\\data\\'
        temp.close()
    except:
        camino = '.\\data\\'

    while True:
        if accion.lower() == 'contar':
            archivo = open(camino + 'cont.txt', 'r')
            lectura = archivo.readlines()
            archivo.close()

            cont = int(lectura[0]) + 1
            archivo = open(camino + 'cont.txt', 'w')
            archivo.write(str(cont))
            archivo.close()
            break
        elif accion.lower() == 'retornar':
            archivo = open(camino + 'cont.txt', 'r')
            lectura = archivo.readlines()
            cont = int(lectura[0])
            archivo.close()
            if camino == '':
                if os.path.exists('.\\data\\') and os.path.exists('.\\data\\cont.txt'):
                    sobresc = open('.\\data\\cont.txt', 'w')
                    cont = 0
                    sobresc.write(str(cont))
                    sobresc.close()
            return cont
def ahorro(suma, accion): #Va sumando al archivo de ahorro o lee lo que se lleva
    if accion.lower() == 'escritura':
        archivo = open('.\\data\\ahorro.txt', 'r')
        lectura = archivo.readlines()
        archivo.close()

        ahorro = int(lectura[0]) + int(suma)
        archivo = open('.\\data\\ahorro.txt', 'w')
        archivo.write(str(ahorro))
        archivo.close()
    elif accion.lower() == 'lectura':
        archivo = open('.\\data\\ahorro.txt', 'r')
        lectura = archivo.readlines()
        cont = int(lectura[0])
        archivo.close()
        return cont
''''def semanal():
    if accion.lower() =='''
'''seo = input('Variante(Fecha/Tiempo): ')
archivo = input('Nombre del archivo(Fecha/Tiempo): ')
tof = bool(input('Temporal? (Dejar en blanco si lo es): '))
escribir(archivo, tof)'''

'''array = leer(input('Nombre? (Fecha/Tiempo): '),bool(input('Temporal?')))
print(array)'''
