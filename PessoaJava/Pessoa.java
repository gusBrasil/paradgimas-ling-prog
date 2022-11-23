// Classe Pessoa
//package classe;

public class Pessoa {
    // Atributos da Classe Pessoa
    public String nome;
    public String sexo;
    public String idade;
    public String altura;

    // Métodos da Classe Pessoa
    public void feliz(){
        System.out.println("Estado: feliz!\n");
    }

    public void triste(){
        System.out.print("Estado: triste!\n");
    }

    public void doente(){
    System.out.print("Estado: doente!\n");
    }

    public void choro(){
        System.out.println("Estado: choro!\n");
    }

    public void raiva(){
        System.out.println("Estado: raiva!\n");
    }

    public void exibirpessoa(){
        System.out.println("Pessoa: " + nome + " " + sexo + " " + idade + " " + altura);
    }
}
