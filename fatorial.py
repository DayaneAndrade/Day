def fatorial(numero):
  if numero <= 1:
    return 1
  else:
    return numero * fatorial(numero - 1)

if __name__ == '__main__':
  numero = input("Entre com o numero:")
  print "%d! = %d" % (numero, fatorial(numero))
