# CLASSE Gato
# Trabalho de Gustavo Medeiros Brasil para a matéria Paradigmas de Linguagens de Programação
# Código disponível em https://github.com/gusBrasil/paradgimas-ling-prog

class Gato:

# Atributos da Classe Gato
    def __init__(self, nome, sexo, idade, peso):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.peso = peso

    # Métodos da Classe Gato
    def Feliz(self):
        print('Estado: feliz!')

    def Triste(self):
        print('Estado: triste!')

    def Doente(self):
        print('Estado: doente!')
    
    def Faminto(self):
        print('Estado: faminto!')

    def Raiva(self):
        print('Estado: raiva!')

    def ExibirGato(self):
        print('Gato:', self.nome, self.sexo, self.idade, self.peso)
