
'''
Pabo Sao
21/08/2016
'''

def habraTormenta(metereologo):
    '''
    verifica la cantidad de metereologos que pronostican tormenta
    :param metereologo: lista con los valores de los metereologos
    :return: valor del metodo cancelaVuelo
    '''
    valor = 0
    for cantidad in metereologo:
        if cantidad >= 80:
            valor = valor + 1
    print("\n\tMeteorologos que pronostican tormenta: {} de {}".format(valor,len(metereologo)))
    return cancelaVuelo(valor)

def cancelaVuelo(cantidad):
    '''
    Verifica si son mas o igual a tres los metereologos que pronostican tormenta
    cancela el vuelo
    :param cantidad: valor calculado de metereologos que calculan tormenta
    :return: 1 si se debe cancelar, -1 si no debe de ser cancelado
    '''
    if cantidad >= 3:
        return 1

    return -1
