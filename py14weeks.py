import os, sys, time, logging
from shutil import rmtree
sys.path.append('scripts')
from scripts.FIRST import primera, segunda, ultima, chequeo
from scripts.tiempo import tiempoActual
from scripts import file, horario

def limpiar(): #Me parece fea la funcion de limpiar pantalla en python
    os.system('cls')

def language(option):
    if option == '1' or option == '2':
        file = open('.\\scripts\\lang.txt', 'r')
        read = file.readlines()
        idioma = []
        file.close()
        mod = []

        cont = 1
        for line in read:
            if line not in idioma:
                idioma.append(line.strip())
        if option == '1':
            rango = 0
        elif option == '2':
            rango = 28
        else:
            rango = 0
        for i in range(rango, rango+28):
            mod.append(idioma[i])
        return mod

if file.contar('retornar') == -1:

    chequeo()

    while True:
        print('En qué idioma quiere utilizar el programa?\n')
        print('Which language would you prefer using the program in?\n')
        print('1.Español\n')
        print('2.Inglés\n')
        eleccion = input('1/2:')
        if eleccion == '1' or eleccion == '2':
            break
        else:
            limpiar()
            print('Por favor elija una opción\n')
            print('Please choose an option\n')


    primera()
    limpiar()
    if eleccion == '1':
        mensaje = 'Cual es tu monto a alcanzar en $?'
        error = 'Por favor ingrese un número mayor a 0'
        error2 = 'Por favor ingrese un número'
        salida = 'La aplicacion se ha configurado, por favor iniciela de nuevo'
    else:
        mensaje = "What's your goal to achieve in $?"
        error = 'Please enter a number greater than 0'
        error2 = 'Please enter a number'
        salida = 'The program has been configured, please re-open it'

    while True:
        try:
            while True:
                print(mensaje)
                meta = int(input())
                if meta >= 0:
                    break
                else:
                    print(error)
            break
        except ValueError:
            print(error2)
    print(salida)
    segunda(eleccion, meta)
    time.sleep(7)
    sys.exit()

# Todas las variables variantes se refieren
# a la variacion de fecha (d/m/a) u tiempo (h/m/s)

# funciones disponibles:
# tiempoActual(chequeo), leer(nombre, t), escribir(nombre, t)
# contar(accion), ahorro(suma, accion), primera(), comparacion(mes)

def convertir(precio, monto): #Bolivares a dolares
    dolares = monto // precio
    return dolares
def convertirReversa(precio, monto): #Dolares a bolivares
    dolares = precio * monto
    return dolares
def guia(idioma):
    file = open('.\\scripts\\guia.txt', 'r')
    read = file.readlines()
    file.close()
    mod = []
    for line in read:
        if line not in mod:
         mod.append(line.strip())
    if idioma == '1':
        rango = 0
    else:
        rango = 10
    for i in range (rango,rango+9):
        print(mod[i])
def matematica(diaActual, diaArchivo, mesActual, mesArchivo, mesRef, dolares, lenguaje, escribir=True): #Guarda una nueva semana si se accede una semana despues de la última carga

    if not (diaActual == diaArchivo and mesActual == mesArchivo):

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
        if mesActual != mesArchivo:
            diferenciaTemp = (int(diaArchivo) + 7)
            diferencia = (diferenciaTemp - referencia)
        else:
            diferencia = (int(diaArchivo) + 7)
            if (int(diaActual) - int(diaArchivo)) > 7:
                diferencia = diaActual
            hay = False

        if escribir==True:
            if (diferencia == diaActual) or (diferencia > diaActual):
                # SI EL DIA ACTUAL ESTA SEPARADO POR 7 DIAS DEL DIA GUARDADO, SE GUARDA UNA NUEVA SEMANA EN SEMANAS
                file.escribir('fecha', True) # Se sobreescribe la fecha guardada
                archivo = open('.\\data\\semanas.txt', 'r')
                temp = archivo.readlines()
                archivo.close()  #probablemente como detecta \n como un string mas dentro de la lista lo corre de mas en el bucle
                mod = []
                conttemp = len(temp)
                for i in range (0,conttemp):
                    if temp[i] != '\n':  #chequear si la ultima letra es \n para no agregar una newline de mas
                        mod.append(temp[i].strip() + '\n')
                cont = len(mod)
                fechaTemp = tiempoActual('tiempo')
                archivo = open('.\\data\\semanas.txt', 'w')
                for i in range (0, cont + 1):
                    if i == cont:
                        escribir = lenguaje[10] + ' ' + str(cont + 1) + ' (D:' + str(diaActual) + '/M:' + str(mesActual) + ')' + lenguaje[11] + ' ' + str(fechaTemp[0]) + ':' + str(fechaTemp[1]) + lenguaje[12] + ' ' +  str(dolares) + '$'
                        archivo.write(escribir)
                    else:
                        if temp[i] != '\n':
                            archivo.write(mod[i])
                archivo.close()
        else:
            if not (diferencia == diaActual):
                if hay:
                    mes = (lenguaje[23] + str(mesActual)) #MUESTRA EL MES MALO, ARREGLAR URGENTEMENTE
                else:
                    mes = lenguaje[24]
                limpiar()
                print(lenguaje[25] + ' ' + str(diferencia) + ' ' + mes)
                print(lenguaje[26] + '\n')
                for i in range (10,0,-1):
                    print(i,)
                    time.sleep(1)
                sys.exit()
    else:
        if file.contar('retornar') >= 1:
            limpiar()
            print(lenguaje[27] + '\n')
            print(lenguaje[26] + '\n')
            for i in range(10, 0, -1):
                print(i)
                time.sleep(1)
            sys.exit()

# empieza el algoritmo
try:
    opcion = 0

    temp1 = open('.\\data\\eleccion.txt')
    eleccion = temp1.readlines()
    texto = language(eleccion[0])
    temp1.close()

    while True:
        while True:  # NO LOGRE HACER QUE CORRIERA CON LA CONDICION DEL IF AQUI
            limpiar()
            print(texto[0])
            print(texto[1])
            print(texto[2])
            print(texto[3])
            print(texto[4])
            opcion = int(input(texto[5]))
            if (opcion >= 1 and opcion <= 5):
                break
            else:
                continue
        if opcion == 1:

            meta2 = open('.\\data\\meta.txt')
            stringmeta = meta2.readlines()
            meta2.close()
            final = int(stringmeta[0])

            temp = tiempoActual('fecha')
            temp2 = file.leer('fecha', True)
            tiemp = file.leer('tiempo', True)
            cont = 0

            matematica(temp[0], temp2[0], temp[1], temp2[1], horario.comparacion(temp2[1], temp2[2]), 0, texto, False)

            limpiar()
            ahorrado = file.ahorro(0, 'lectura')
            precio = int(input(texto[6]))
            monto = int(input(texto[7]))
            dolares = convertir(precio, monto)
            file.ahorro(dolares, 'escritura')
            conjunto = dolares + ahorrado
            print('\n' + texto[8], str(monto), texto[9], str(dolares), "$" + '\n')


            if file.contar('retornar') > 0:
                rotar = matematica(temp[0], temp2[0], temp[1], temp2[1], horario.comparacion(temp2[1], temp2[2]), dolares, texto, True)

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
                file.escribir('fecha', True)
                archivo0 = open('.\\data\\semanas.txt', 'w')
                archivo0.write(texto[10] + ' ' + str(1) + ' (D:' + str(int(temp[0])) + '/M:' + str(int(temp[1])) + ')' + texto[11] + ' ' + tiemp[0] + ':' + tiemp[1] + texto[12] + ' '+ str(dolares) + '$')
                archivo0.close()
                file.contar('contar')

        #implementar comparacion con el dia actual
            if conjunto < final:
                diferencia = final - (dolares + ahorrado)
                bolivares = convertirReversa(diferencia,precio)
                print (texto[13], diferencia,'$', texto[14],bolivares,'bs', texto[15], str(final), '$'+'\n' )
                input(texto[16])
            else:
                diferencia = (dolares + ahorrado) - final
                print (texto[17], final,texto[18], diferencia,'$'+'\n')
                input(texto[16])
        elif opcion == 2:
            limpiar()
            if file.contar('retornar') > 0:
                lineas = open('.\\data\\semanas.txt', 'r')
                array = lineas.readlines()
                lineas.close()
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
                print(texto[19])
        elif opcion == 3:
            limpiar()
            mensaje_de_advertencia =  texto[20] + '\n'
            mensaje_de_advertencia2 = texto[21] + '\n'
            mensaje_de_advertencia3 = texto[22]
            print(mensaje_de_advertencia, mensaje_de_advertencia2, mensaje_de_advertencia3)
            definitivo = input()
            if not ((definitivo.lower() == 'y' or definitivo.lower() == 's') or (definitivo.lower() == 'yes' or definitivo.lower() == 'si')):
                continue
            else:
                ultima()
                limpiar()
                time.sleep(3)
                break
        elif opcion == 4:
            limpiar()
            guia(eleccion[0])
            print('')
            print(texto[16])
            input()
        else:
            break
        time.sleep(5)
except Exception as e:
    logging.error('Error at %s', exc_info=e) #esto lo copie de stackoverflow
    time.sleep(7)
