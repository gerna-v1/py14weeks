import os, sys, time, file, horario, logging
from tiempo import tiempoActual
from FIRST import primera
# Todas las variables variantes se refieren
# a la variacion de fecha (d/m/a) u tiempo (h/m/s)

# funciones disponibles:
# tiempoActual(chequeo), leer(nombre, t), escribir(nombre, t)
# contar(accion), ahorro(suma, accion), primera(), comparacion(mes)
def limpiar(): #Me parece fea la funcion de limpiar pantalla en python
    os.system('cls')
def convertir(precio, monto): #Bolivares a dolares
    dolares = monto // precio
    return dolares
def convertirReversa(precio, monto): #Dolares a bolivares
    dolares = precio * monto
    return dolares
def guia():
    file = open('guia.txt', 'r')
    read = file.readlines()
    mod = []
    for line in read:
        if line not in mod:
         mod.append(line.strip())

    for i in range (0,7):
        print(mod[i])
def matematica(diaActual, diaArchivo, mesActual, mesArchivo, mesRef, dolares, escribir=True): #Guarda una nueva semana si se accede una semana despues de la última carga

    if not (diaActual == diaArchivo and mesActual == mesArchivo):
        if mesActual != mesArchivo:
            if mesRef == 1:
                referencia = 31
                hay = True
            elif mesRef == 2:
                referencia = 30
                hay = True
            elif mesRef == 3:
                referencia = 29
                hay = True
            elif mesRef == 4:
                referencia = 28
                hay = True
            else:
                referencia = 0
            diferenciaTemp = (int(diaArchivo) + 7)
            diferencia = (diferenciaTemp - referencia)
        else:
            diferencia = (int(diaArchivo) + 7)
            hay = False
        if escribir==True:
            if diferencia == diaActual:
                # SI EL DIA ACTUAL ESTA SEPARADO POR 7 DIAS DEL DIA GUARDADO, SE GUARDA UNA NUEVA SEMANA EN SEMANAS
                file.escribir('fecha',True) # Se sobreescribe la fecha guardada
                archivo = open('semanas.txt', 'r')
                temp = archivo.readlines()
                archivo.close()  #probablemente como detecta \n como un string mas dentro de la lista lo corre de mas en el bucle
                mod = []
                conttemp = len(temp)
                for i in range (0,conttemp):
                    if temp[i] != '\n':  #chequear si la ultima letra es \n para no agregar una newline de mas
                        mod.append(temp[i].strip() + '\n')
                cont = len(mod)
                fechaTemp = tiempoActual('tiempo')
                archivo = open('semanas.txt', 'w')
                for i in range (0, cont + 1):
                    if i == cont:
                        escribir = 'En la semana ' + str(cont + 1) + ' (D' + str(diaActual) + '/M' + str(mesActual) + ')' + ', cargado a las ' + str(fechaTemp[0]) + ':' + str(fechaTemp[1]) + ', ahorraste ' + str(dolares) + '$'
                        archivo.write(escribir)
                    else:
                        if temp[i] != '\n':
                            archivo.write(mod[i])
                archivo.close()
        else:
            if not (diferencia == diaActual):
                if hay:
                    mes = (' del mes ' + str(mesActual)) #MUESTRA EL MES MALO, ARREGLAR URGENTEMENTE
                else:
                    mes = ' de este mes'
                limpiar()
                print('Por favor inicie el programa el día ' + str(diferencia) + mes)
                print('El programa se cerrará en\n')
                for i in range (10,0,-1):
                    print(i,)
                    time.sleep(1)
                sys.exit()
    else:
        if file.contar('retornar') >= 1:
            limpiar()
            print('Por favor espere una semana para volver a cargar el ahorro\n')
            print('El programa se cerrará en\n')
            for i in range(10, 0, -1):
                print(i, )
                time.sleep(1)
            sys.exit()

# empieza el algoritmo
try:
    if file.contar('retornar') == -1:
        primera()
        print('La aplicacion se ha configurado, por favor iniciela de nuevo')
        time.sleep(7)
        sys.exit()
    opcion = 0
    while True: # NO LOGRE HACER QUE CORRIERA CON LA CONDICION DEL IF AQUI
        limpiar()
        print('1. Subir el ahorro')
        print('2. Ver el registro semanal')
        print('3. Guia')
        print('4. Salir')
        opcion = int(input('Que desea hacer?: '))
        if (opcion >= 1 and opcion <= 4):
            break
        else:
            continue
    if opcion == 1:
        final = 60

        temp = tiempoActual('fecha')
        temp2 = file.leer('fecha', True)
        tiemp = file.leer('tiempo', True)
        cont = 0

        matematica(temp[0], temp2[0], temp[1], temp2[1], horario.comparacion(temp2[1],temp2[2]), 0, False)

        ahorrado = file.ahorro(0,'lectura')
        precio = int(input("Ingrese el precio del dolar: "))
        monto = int(input("Ingrese el monto en bs: "))
        dolares = convertir(precio, monto)
        file.ahorro(dolares,'escritura')
        conjunto = dolares + ahorrado
        print("Sus", str(monto), "bs tambien son aproximadamente", str(dolares), "$")


        if file.contar('retornar') > 0:
            rotar = matematica(temp[0],temp2[0],temp[1],temp2[1],horario.comparacion(temp2[1]),dolares)
            if rotar:
                sys.exit()
            for i in range(0,2):
                if temp2[-1] == '\n':
                    temp2.append(temp2[:-1])
                    print(temp2[i])
                else:
                    temp2.append(temp2[i])
            file.contar('contar')
        else:
            file.escribir('fecha',True)
            archivo0 = open('semanas.txt', 'w')
            archivo0.write('En la semana ' + str(1) + ' (D' + str(int(temp[0])) + '/M' + str(int(temp[1])) + ')' + ', cargado a las ' + tiemp[0] + ':' + tiemp[1] + ', ahorraste ' + str(dolares) + '$')
            archivo0.close()
            file.contar('contar')

    #implementar comparacion con el dia actual
        if conjunto < final:
            diferencia = final - (dolares + ahorrado)
            bolivares = convertirReversa(diferencia,precio)
            print ('Te faltan', diferencia,'$', ' o ',bolivares,'bs', 'para llegar a los', str(final), '$'+'\n' )
            input('Presione cualquier tecla para salir')
        else:
            diferencia = (dolares + ahorrado) - final
            print ('Felicidades! Ya sobrepaso los', final,'$ con un extra de ', diferencia,'$'+'\n')
            input('Presione cualquier tecla para salir')
    elif opcion == 2:
        limpiar()
        if file.contar('retornar') > 0:
            lineas = open('semanas.txt', 'r')
            array = lineas.readlines()
            mod = []
            cont = 0
            for line in array:
                if line[-1] == '\n':
                    mod.append(line[:-1])
                    print(mod[cont])
                    cont = cont + 1
                else:
                    mod.append(line)
                    print(mod[cont])
                    cont = cont + 1
        else:
            print('No ha cargado ningun ahorro')
    elif opcion == 3:
        limpiar()
        guia()
    time.sleep(7)
except Exception as e:
    logging.error('Error at %s', exc_info=e) #esto lo copie de stackoverflow
    time.sleep(7)
