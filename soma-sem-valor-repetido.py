num1 = int( input("Digite primeiro número: ") )
num2 = int( input("Digite segundo número: ") )
num3 = int( input("Digite terceiro número: ") )

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
