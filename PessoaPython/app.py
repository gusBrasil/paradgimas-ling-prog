# Proj1 - App
import os
from pessoa import Pessoa

# Cria Objetos p1, p2, p3 da Classe Pessoa
p1 = Pessoa('Ana', 'F', 20, 1.65)
p2 = Pessoa('Flavio', 'M', 24, 1.78)
p3 = Pessoa('Maria', 'F', 22, 1.70)

# Limpa a Tela no Windows
os.system('CLS')
# Saída de Informações
print('Verificando os Objetos em Ação:\n')
p1.ExibirPessoa()
p1.Feliz()
print('\n')

p2.ExibirPessoa()
p2.Raiva()
print('\n')

p3.ExibirPessoa()
p3.Doente()
p3.Triste()
p3.Choro()
print('\n')
