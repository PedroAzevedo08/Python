print ("Exercício 1 Saudação Personalizada\n")
nome = input("Digite seu nome: ")
print  ("Olá, {}! Bem-vindo(a)! \n".format( nome ))


print ("Exercício 2 Cadastro Simples: \n ")
nome = input("insira seu nome: ")
idade  = input("insira sua idade:")
cidade = input("insira sua cidade: ")
print ("Seu nome é {},você tem {} anos e mora em {}\n.".format (nome, idade, cidade))


print ("Exercício 3 Etiqueta de Endereço: \n ")
nome = input("digite seu nome completo: ")
end = input("digite seu endereço: ")
tel = input("digite seu tel ")
print("seu nome completo é {},\n seu endereço é {}\n e seu telefone é {}\n".format(nome, end, tel))


print ("4. União de Palavras: \n ")
string1 = input ("digite a primeira palavra: ")
string2 = input ("digite a segunda palavra: ")
frase = (string1 + string2).upper()
print ("{}\n".format(frase))


print ("5. Conversor de Medidas: \n ")
metros = float(input("insira o valor a ser convertido em metros: "))
cent = (metros*100)
mili = (metros*1000)
print ("Conversao para centimetros: {} \n conervsao para milimetros: {}\n".format(cent, mili))


print ("6. Cálculos Simples: \n ")
num = float(input('insira o primeiro valor: '))
dobro = (num*2)
terco = (num/3)
print ("O dobro do numero é: {} \n o terço é: {}\n".format(dobro, terco))


print ("7. Calculadora de Quatro Operações: \n ")
a = float(input("Insira o primeiro valor: "))
b = float (input("Insira o segundo valor: "))
soma = ( a + b)
sub = ( a - b)
mul = ( a*b)
div = ( a/b)
print ("Soma: {} \n Subtração: {} \n Multiplicação: {} \n Divisão: {}\n".format(soma, sub, mul, div))


print ("8. Cálculo de Média Escolar: \n ")
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a seugnda nota: "))
nota3 = float(input("digite a terceira nota: "))
media = ((nota1 + nota2 + nota3) /3)
print ("a média é {}\n".format(media))


print ("9. Cálculo de Área: \n ")
base = float(input("Digite o tamanho da base: "))
altura = float(input("Digite o tamanho da altura: "))
area = ( base*altura)
print ("A area é igual a : {}\n".format(area))


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
print ("\n")

print("11. Reajuste Salarial\n")
salario = float(input('Insira o salário do funcionário: '))
porcentagem = float(input('Insira a porcentagem do reajuste em decimal, (ex: 10% = 0.10) '))
reajuste = salario + (salario * porcentagem)
print ("O salário reajustado é {}\n".format(reajuste))


print("12. Índice de Massa Corporal (IMC)\n")
peso = float(input('Insira o peso da pessoa em kg: '))
altura = float(input('Insira a altura da pessoa em metros: '))
imc = peso / (altura ** 2)
print("O IMC da pessoa é: {}\n".format(imc))

