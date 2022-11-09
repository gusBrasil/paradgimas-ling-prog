// Programa feito por Gustavo Medeiros Brasil
// Insira os parâmetros para a função

#include <stdio.h>
int ack(int m, int n)

{
    if (m == 0)
    {
        return n + 1;
    }
    else if ((m > 0) && (n == 0))
    {
        return ack(m - 1, 1);
    }
    else if ((m > 0) && (n > 0))
    {
        return ack(m - 1, ack(m, n - 1));
    }
}

int main()
{
    int A, m, n;
    printf("Insira o primeiro valor: \n");
    scanf("%d", &m);
    printf("Insira o segundo valor: \n");
    scanf("%d", &n);
    A = ack(m, n);
    printf("%d", A);
    return 0;
}
