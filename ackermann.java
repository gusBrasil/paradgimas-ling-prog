// Programa feito por Gustavo Medeiros Brasil
// Insira os parâmetros para a função

import java.util.Objects;
import java.util.Scanner;

class ackermann {

    static int ack(int m, int n) {
        if (m == 0) {
            return n + 1;
        } else if ((m > 0) && (n == 0)) {
            return ack(m - 1, 1);
        } else if ((m > 0) && (n > 0)) {
            return ack(m - 1, ack(m, n - 1));
        } else
            return n + 1;
    }

    // Driver code
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Insira o primeiro valor para a função: ");
        int m = sc.nextInt();
        System.out.println("Insira o segundo valor para a função: ");
        int n = sc.nextInt();
        System.out.println(ack(m, n));
    }
}