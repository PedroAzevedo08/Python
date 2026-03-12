achei = False
a = int(input('insira o valor de a: '))
b = int(input('Insira o valor de b: '))

while b < a:
    print('Insira um valor de b valido')
    b = int(input('Insira o valor de b: '))

z = int(input('Insira o valor de z: '))
while z < b:
    print('Insira um valor de z valido')
    z = int(input('Insira o valor de z: ')) 

y = b
while y >= a:
    for x in range(a, b + 1): 
        if x + y == z:
            achei = True
            print(f'{x} + {y} = {z}')
    y -= 1

if not achei:
    print('Não existe par de números que atenda ao especificado')
