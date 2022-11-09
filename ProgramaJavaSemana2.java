// Cálculo do IMC - Índice de Massa Corporal​

package programaJavaSemana2;

import java.util.Scanner;

public class ProgramaJavaSemana2 {

  /**
   * @param args
   */
  public static void main(String[ ] args) {

    Scanner entrada = new Scanner(System.in);

    System.out.print("Digite seu peso em Kg: ");
    
    double peso = Double.parseDouble(entrada.nextLine());

    System.out.print("Digite sua altura em metros: ");

    double altura = Double.parseDouble(entrada.nextLine());
// vamos calcular o IMC​

    double imc = peso / (altura * altura);

    System.out.println("Seu IMC é: " + imc);


    if(imc < 16){

      System.out.println("Magreza grave");

    }

    else if(imc < 17){

      System.out.println("Magreza moderada");

    }

    else if(imc < 18.5){

      System.out.println("Magreza leve");

    }

    else if(imc < 25){

      System.out.println("Saudável");

    }

else if(imc < 30){

      System.out.println("Sobrepeso"); 

    }

    else if(imc < 35){

      System.out.println("Obesidade Grau I (acentuada)"); 

    }

    else if(imc < 40){

      System.out.println("Obesidade Grau II (severa)");

    }


 else{

      System.out.println("Obesidade Grau III (mórbida)");

       }

      System.out.println("\n");
  }
}
