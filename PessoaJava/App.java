// Projeto1 - App
//import Gato

public class App {
        public static void main(String[] args) throws Exception {

                // Criando o objeto Gato 1
                Gato p1 = new Gato();
                p1.nome = "Naldo";
                p1.sexo = "M";
                p1.idade = "2";
                p1.peso = "7,5";

                // Criando o objeto Gato 2
                Gato p2 = new Gato();
                p2.nome = "Maria Mole";
                p2.sexo = "F";
                p2.idade = "1";
                p2.peso = "3";

                // Criando o objeto Gato 3
                Gato p3 = new Gato();
                p3.nome = "Rivotril";
                p3.sexo = "M";
                p3.idade = "4";
                p3.peso = "6";

                // Limpa a tela no windows, no linux e no MacOS
                if (System.getProperty("os.name").contains("Windows"))
                        new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
                else
                        Runtime.getRuntime().exec("clear");

                // Saída de Informações
                System.out.println("Verificando os Objetos em Ação:\n");
                p1.exibirGato();
                p1.feliz();

                p2.exibirGato();
                p2.raiva();

                p3.exibirGato();
                p3.doente();
                p3.triste();
                p3.faminto();
        }
}
