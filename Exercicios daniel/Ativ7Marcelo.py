def contar(num, dig):
    return str(num).count(str(dig))


num = int(input("Insira o numero desejado: "))
while num < 0:
    print('Numero invalido\n')
    num = int(input("Insira o numero desejado: "))
dig = int(input('Insira o digito'))

quantidade = contar(num, dig)
print(f"Resposta: o Número {dig} ocorre {quantidade} vezes")
