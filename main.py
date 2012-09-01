def calculaPingPong(numero):
    imprime = ''
    if (numero%3 == 0) or (numero%5 == 0):
        if (numero%5 ==0):
            imprime =  'pong'
        if (numero%3 ==0):
            imprime= 'ping' + imprime
        print imprime
        return imprime
    else:
        print numero
        return numero

for numero in range(1,101):
    calculaPingPong(numero)


    