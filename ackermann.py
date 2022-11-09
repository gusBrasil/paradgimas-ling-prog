# Programa feito por Gustavo Medeiros Brasil
# Insira os parâmetros para a função

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1,1)
    else:
        return ackermann(m-1, ackermann(m, n-1))

def main():
 
    num1 = float(input("Insira o primeiro valor: "))
    num2 = float(input("Insira o segundo valor: "))
    print(ackermann(num1, num2))

main()
