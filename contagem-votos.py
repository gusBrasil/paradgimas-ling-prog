# Programa elaborado por Gustavo Medeiros Brasil para a matéria de Paradigmas de Linguagens de Programação
# O seu objetivo é simular um ambiente de votações, com o programa recebendo e processando os dados de cada "cédula",
# em seguida emitindo um relatório com os resultados.
# Disponível também em: https://github.com/gusBrasil/paradgimas-ling-prog

a = 0
j = 0
m = 0
b = 0
n = 0


def calculaVenc(a, j, m):
    if a > m and a > j:
        print('O vencedor é Antônio!')
    elif m > a and m > j:
        print('O vencedor é Maria!')
    elif j > a and j > m:
        print('O vencedor é José!')


def calculaVotos(a, j, m, b, n):
    TotalVotos = a + j + m + b + n
    print('O número de eleitores que compareceram às urnas foi de: ' + str(TotalVotos))


def calculaEmpate(a, j, m):
    if a == m or a == j or m == j:
        print('Votação em Segundo Turno!')


while True:
    voto = input(
        'Vote em seu candidato. Antônio(1), José(2), Maria(3), Branco(4), nulo(*) ')
    confirmacao = input('confirma? (S/N) ')

    if voto in ('1', '2', '3', '4', '*'):

        if voto == '1':
            if confirmacao == 'S':
                a = a + 1
                print('Confirmado!')
            elif confirmacao == 'N':
                continue

        elif voto == '2':
            if confirmacao == 'S':
                j = j + 1
                print('Confirmado')
            elif confirmacao == 'N':
                continue

        elif voto == '3':
            if confirmacao == 'S':
                m = m + 1
                print('Confirmado')
            elif confirmacao == 'N':
                continue

        elif voto == '4':
            if confirmacao == 'S':
                b = b + 1
                print('Confirmado')
            elif confirmacao == 'N':
                continue

        else:
            if confirmacao == 'S':
                n = n + 1
                print('Confirmado')
            elif confirmacao == 'N':
                break

    if voto in ('0') == '0':
        print(a)
        print(j)
        print(m)
        calculaVenc(a, j, m)
        calculaEmpate(a, j, m)
        calculaVotos(a, j, m, b, n)
        break
