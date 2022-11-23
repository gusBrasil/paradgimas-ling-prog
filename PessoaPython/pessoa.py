# CLASSE Pessoa
class Pessoa:

# Atributos da Classe Pessoa
    def __init__(self, nome, sexo, idade, altura):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.altura = altura

    # Métodos da Classe Pessoa
    def Feliz(self):
        print('Estado: feliz!')

    def Triste(self):
        print('Estado: triste!')

    def Doente(self):
        print('Estado: doente!')
    
    def Choro(self):
        print('Estado: chorando!')

    def Raiva(self):
        print('Estado: raiva!')

    def ExibirPessoa(self):
        print('Pessoa:', self.nome, self.sexo, self.idade, self.altura)
