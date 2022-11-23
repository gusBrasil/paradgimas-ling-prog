// Classe Gato
//package classe;

public class Gato {
    // Atributos da Classe Gato
    public String nome;
    public String sexo;
    public String idade;
    public String peso;

    // Métodos da Classe Gato
    public void feliz() {
        System.out.println("Estado: feliz!\n");
    }

    public void triste() {
        System.out.print("Estado: triste!\n");
    }

    public void doente() {
        System.out.print("Estado: doente!\n");
    }

    public void faminto() {
        System.out.println("Estado: faminto!\n");
    }

    public void raiva() {
        System.out.println("Estado: raiva!\n");
    }

    public void exibirGato() {
        System.out.println("Gato: " + nome + " " + sexo + " " + idade + " " + peso);
    }
}
