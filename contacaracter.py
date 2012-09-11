def contaCaracter(s):
    caracteres = {}
    for c in s:
        if c in caracteres:
            caracteres[c] = caracteres[c] + 1
        else:
            caracteres[c] = 1
    return caracteres

if __name__ == '__main__':
  s = raw_input("Entre com a String:")
  print contaCaracter(s)