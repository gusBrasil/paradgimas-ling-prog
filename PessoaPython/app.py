# Proj1 - App
import os
from gato import Gato

# Cria Objetos p1, p2, p3 da Classe Gato
p1 = Gato('Naldo', 'M', 2, 7.8)
p2 = Gato('Maria Mole', 'F', 1, 3)
p3 = Gato('Rivotril', 'M', 4, 6)

# Limpa a Tela no Windows
os.system('CLS')
# Saída de Informações
print('Verificando os Objetos em Ação:\n')
p1.ExibirGato()
p1.Feliz()
print('\n')

p2.ExibirGato()
p2.Raiva()
print('\n')

p3.ExibirGato()
p3.Doente()
p3.Triste()
p3.Faminto()
print('\n')
