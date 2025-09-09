print("10. Calculadora de Números Decimais:\n")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))
escolha = input("Escolha uma operação (+, -, *, /): ")

if escolha == "*":
    resultado = num1 * num2
    print("Resultado: {}".format(resultado))
elif escolha == "/":
    resultado = num1 / num2
    print("Resultado: {}".format(resultado))
elif escolha == "+":
    resultado = num1 + num2
    print("Resultado: {}".format(resultado))
elif escolha == "-":
    resultado = num1 - num2
    print("Resultado: {}".format(resultado))
else:
    print("operacao inválida!\n")
