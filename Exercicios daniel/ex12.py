print("12. Índice de Massa Corporal (IMC)\n")

peso = float(input('Insira o peso da pessoa em kg: '))
altura = float(input('Insira a altura da pessoa em metros: '))
imc = peso / (altura ** 2)
print("O IMC da pessoa é: {}\n".format(imc))
