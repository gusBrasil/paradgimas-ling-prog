# Programa elaborado por Gustavo Medeiros Brasil para a matéria de Paradigmas de Linguagens de Programação
# Seu objetivo é determinar se um número digitado pelo usuário se qualifica como um número perfeito.
# Disponível também em: https://github.com/gusBrasil/paradgimas-ling-prog

n = int(input("Digite qualquer número inteiro positivo: "))
soma1 = 0
for i in range(1, n):
    if(n % i == 0):
        soma1 = soma1 + i
if (soma1 == n):
    print("O número é um número perfeito!")
else:
    print("O número não é um número perfeito!")
    