print("11. Reajuste Salarial\n")

salario = float(input('Insira o salário do funcionário: '))
porcentagem = float(input('Insira a porcentagem do reajuste em decimal, (ex: 10% = 0.10) '))
reajuste = salario + (salario * porcentagem)
print ("O salário reajustado é {}\n".format(reajuste))


