// Projeto1 - App
//import Pessoa

public class App {
    public static void main(String[] args) throws Exception {
 
        // Criando o objeto Pessoa 1
        Pessoa p1 = new Pessoa();
        p1.nome = "Ana";
        p1.sexo = "F";
        p1.idade = "20";
        p1.altura = "1,65";

        // Criando o objeto Pessoa 2
        Pessoa p2 = new Pessoa();
        p2.nome = "Flavio";
        p2.sexo = "M";
        p2.idade = "24";
        p2.altura = "1,78";

        // Criando o objeto Pessoa 3
        Pessoa p3 = new Pessoa();
        p3.nome = "Maria";
        p3.sexo = "F";
        p3.idade = "22";
        p3.altura = "1,70";

//Limpa a tela no windows, no linux e no MacOS
        if (System.getProperty("os.name").contains("Windows"))
        new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        else
        Runtime.getRuntime().exec("clear");

        // Saída de Informações
        System.out.println("Verificando os Objetos em Ação:\n");
        p1.exibirpessoa();
        p1.feliz();

        p2.exibirpessoa();
        p2.raiva();

        p3.exibirpessoa();
        p3.doente();
        p3.triste();
        p3.choro();
        }
}
