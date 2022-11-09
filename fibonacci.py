# Programa feito por Gustavo Medeiros Brasil
# Digite o valor que deseja, e verá a sequência correspondente a esse valor.

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

termo = int(input("Qual número da sequência de Fibonacci você deseja? "))

# Teste para ver se o valor é válido
if termo <= 0:
   print("Insira um valor positivo inteiro")
else:
   print("Sequência de Fibonacci:")
   for i in range(termo):
       print(fibo(i))