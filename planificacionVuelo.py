
'''
Pabo Sao
21/08/2016
'''

from pronostico import habraTormenta

def imprime_espacio():
    print("\n")

def imprime_mensaje(msj):
    '''
    Impresion de mensajes
    :param msj: mensaje deseado a imprimir
    :return: n/a
    '''
    mensaje = "~~~ " + msj + " ~~~"
    print(mensaje.center(tamanio_mensaje))

def valida_mayor(valor_menor=0, valor_comparar=0):
    '''
    Verifica que el valor a comparar sea mayor al
    valor menor
    :param valor_menor: valor minimo de comparacion
    :param valor_comparar: valor de comparacion
    :return: Boolean
    '''

    respuesta = False
    if valor_menor <= valor_comparar:
        respuesta = True

    return respuesta

def valida_menor(valor_menor=100, valor_comparar=0):
    '''
    Verifica que el valor a comparar sea menor al
    valor menor
    :param valor_menor: valor minimo de comparacion
    :param valor_comparar: valor de comparacion
    :return: Boolean
    '''

    respuesta = False
    if valor_menor >= valor_comparar:
        respuesta = True

    return respuesta

def valida_salida(respuesta):
    '''
    Metodo encargado de verificar si el usuario desea salir del programa
    :param respuesta: string. Acepta valor yes, y, no, n con todas sus variantes
    :return:
    '''
    try:

        if respuesta[0].upper() == "Y":
            return False
        return True
    except:
        return True

def ingreso_registros(mensaje):
    '''
    Maneja el ingreso de valores por parte del usuario. Verifica que los valores sean
    mayores a 0
    :param mensaje: String. Mensaje de peticion de ingreso para el usuario
    :return: Float.
    '''
    control = True
    registro = 0.00
    while control:
        try:
            registro = int(input(str(mensaje)))

            if(not valida_menor(valor_menor=100,valor_comparar=registro)):
                imprime_espacio()
                imprime_mensaje("++++++ Debe ingresar un numero menor o igual a 100 ++++++")
            elif (valida_mayor(valor_comparar=registro)):
                control = False  # saliendo del loop
            else:
                imprime_espacio()
                imprime_mensaje("++++++ Debe ingresar un numero mayor a 0 ++++++")


        except ValueError:
            imprime_espacio()
            imprime_mensaje("++++++ Debe ingresar un dato numerico ++++++")
            pass

    return registro

#Variables
control = True
tamanio_mensaje = 70 #valor de caracteres para centrar
minTormenta = 80 #criterio minimo para indicar que hay tormenta

while control:

    #variables temporal para los 5 metereologos
    metereologos = [0]*5

    imprime_espacio()
    imprime_mensaje("Planificador de vuelos")
    imprime_mensaje("Melisa Rosales")
    imprime_espacio()

    imprime_mensaje("Ingreso de Registro de Meteorologos")

    #ingreso de los valores para los 5 metereologos
    for ingreso in range(0,len(metereologos)):
        metereologos[ingreso]= ingreso_registros('Valor del meteorologo {}: '.format(ingreso + 1))

    #verifica si se debe de cancelar la tormenta
    if habraTormenta(metereologos) == 1:
        imprime_espacio()
        imprime_mensaje("El vuelo debe ser cancelado")
    else:
        imprime_espacio()
        imprime_mensaje("El vuelo NO debe ser cancelado")

    # verificando si desea realizar otro calculo
    imprime_espacio()
    control = valida_salida(input('Desea desea salir del planificador de vuelo? (y/n): '))
    imprime_mensaje("Saliendo. Gracias por utilizar el Planificador de Vuelo")

    imprime_espacio()
    imprime_espacio()
