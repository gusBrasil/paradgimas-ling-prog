#include <stdio.h>

/* standard input-output header - Possui definições de subrotinas relativas às operações de entrada/saída, como leitura de dados digitados no teclado e exibição de informações na tela do programa de computador. Também possui numerosas definições de constantes, variáveis e tipos. É um dos cabeçalhos mais populares da linguagem de programação C, intensivamente utilizado tanto por programadores iniciantes como por experientes. */


int main()

{
    int peso;
    float imc=0, altura=0;
    printf("Digite seu peso em Kg: ");
    scanf("%d",&peso);
    printf(" Digite sua altura em metros: ");
    scanf("%f",&altura);

    imc=peso/(altura*altura);
   
if (imc < 16) 
       printf("Magreza grave\n");
    else if (imc < 17)

       printf("Magreza moderada\n");

    else if (imc < 18.5)

       printf("Magreza leve");

    else if (imc < 25) 

       printf("Saudavel\n");

    else if (imc < 30) 

       printf("Sobrepeso\n");

    else if (imc < 35)

       printf("Obesidade Grau I (acentuada)");

    else if (imc < 40)

       printf("Obesidade Grau II (severa)");

    else  printf("Obesidade Grau III (mórbida)");

//Dá uma pausa no sistema. Pode ser trocado por system("pause");​

}
