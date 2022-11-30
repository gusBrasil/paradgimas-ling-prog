# Programa elaborado por Gustavo Medeiros Brasil para a matéria de Paradigmas de Linguagens de Programação
# Seu objetivo é receber o valor de três números do usuário e somá-los, caso sejam números diferentes entre si.Se houverem números repetidos,
# serão desconsiderados pela conta.
# Disponível também em: https://github.com/gusBrasil/paradgimas-ling-prog



num1 = int( input("Digite o primeiro número: ") )
num2 = int( input("Digite o segundo número: ") )
num3 = int( input("Digite o terceiro número: ") )

soma = 0

if num1 != num2:
    if num1 != num3: 
        soma = soma + num1
        if num2 != num3: 
            soma = soma + num2 + num3
    else: 
        soma = soma + num2
else:
    if num1 != num3:
        soma = soma + num3
print(soma)
