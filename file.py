from tiempo import tiempoActual
# FALTA FUNCION PARA COMPROBAR LOS DIAS
def escribir(nomArchivo, t):
    variante = nomArchivo
    if nomArchivo.lower() == 'fecha' or nomArchivo.lower() == 'tiempo':
        if t:
            archivo = open(str(nomArchivo)+'.txt', 'w')
        else:
            archivo = open(str(nomArchivo)+'_temp'+'.txt', 'w')
        array = tiempoActual(str(variante))
        for i in range(0,3):
            if i == 3:
                archivo.write(str(array[i]))
            else:
                archivo.write(str(array[i]) + '\n')
        archivo.close()
    else:
        return None
def leer(nomArchivo, t):
    try:
        if t:
            archivo = open(str(nomArchivo)+'.txt', 'r')
        else:
            archivo = open(str(nomArchivo)+'_temp'+'.txt', 'r')
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
def contar(accion):
    if accion.lower() == 'contar':
        archivo = open('cont.txt', 'r')
        lectura = archivo.readlines()
        archivo.close

        cont = int(lectura[0]) + 1
        archivo = open('cont.txt', 'w')
        archivo.write(str(cont))
        archivo.close()
    elif accion.lower() == 'retornar':
        archivo = open('cont.txt', 'r')
        lectura = archivo.readlines()
        cont = int(lectura[0])
        archivo.close
        return cont
def ahorro(suma, accion):
    if accion.lower() == 'escritura':
        archivo = open('ahorro.txt', 'r')
        lectura = archivo.readlines()
        archivo.close

        ahorro = int(lectura[0]) + int(suma)
        archivo = open('ahorro.txt', 'w')
        archivo.write(str(ahorro))
        archivo.close()
    elif accion.lower() == 'lectura':
        archivo = open('ahorro.txt', 'r')
        lectura = archivo.readlines()
        cont = int(lectura[0])
        archivo.close
        return cont
''''def semanal():
    if accion.lower() =='''
'''seo = input('Variante(Fecha/Tiempo): ')
archivo = input('Nombre del archivo(Fecha/Tiempo): ')
tof = bool(input('Temporal? (Dejar en blanco si lo es): '))
escribir(archivo, tof)'''

'''array = leer(input('Nombre? (Fecha/Tiempo): '),bool(input('Temporal?')))
print(array)'''
