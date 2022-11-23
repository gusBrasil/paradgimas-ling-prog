// Programa feito por Gustavo Medeiros Brasil
// Digite o valor que deseja, e verá a sequência correspondente a esse valor.

#include <stdio.h>
int main() {

  int i, n;

  int t1 = 0, t2 = 1;
  int proxTermo = t1 + t2;


  printf("Qual número da sequência de Fibonacci você deseja?: ");
  scanf("%d", &n);

  printf("Sequência de Fibonacci: %d, %d, ", t1, t2);

  for (i = 3; i <= n; ++i) {
    printf("%d, ", proxTermo);
    t1 = t2;
    t2 = proxTermo;
    proxTermo = t1 + t2;
  }

  return 0;
}
