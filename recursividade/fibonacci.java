// Programa feito por Gustavo Medeiros Brasil
// Digite o valor que deseja, e verá a sequência correspondente a esse valor.

import java.util.Objects;
import java.util.Scanner;

public class fibonacci {
    static int fib(int n)
    {
        if (n <= 1)
            return n;
        return fib(n - 1) + fib(n - 2);
    }

    public static void main(String args[])
    {
        System.out.println("Qual número da sequência de Fibonacci você deseja?: ");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(fib(n));
    }
}
