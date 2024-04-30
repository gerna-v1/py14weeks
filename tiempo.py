import datetime

def tiempoActual(chequeo): #Regresa una lista con la fecha o hora actual

    ahora = str(datetime.datetime.now())
    ahora2 = ahora.split(sep='-',maxsplit=3)
    separacion = ahora2[2].split(maxsplit=1)
    ano = ahora2[0]
    mes = ahora2[1]
    dia = separacion[0]
    tiemp = separacion[1].split(sep=':')

    tiempo = [tiemp[0], tiemp[1], round(float(tiemp[2]))]
    dias = [dia,mes,ano]

    if chequeo.lower() == 'tiempo':
        return tiempo
    elif chequeo.lower() == 'fecha':
        return dias
    else:
        return None
