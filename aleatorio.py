# Valores aleatórios com random
import random

print(random.random()) #gera um valor 0.0 a 1.0

print(random.uniform(4, 10)) #Gera um valor decimal de valor minimo ao valor maximo

print(random.randint(4, 10)) #gera um valor inteiro de valor minimo ao valor maximo

cores = ['verde', 'vermelho', 'azul'] # Escolher opção aleatória
print(random.choices(cores, k=2))


carta_baralho = ['carta1', 'carta2', 'carta3','carta4'] # Embaralhar uma lista

print(random.shuffle(carta_baralho))
print(carta_baralho)

# Desafio1
## Você quer simular a opção de jogar uma moeda e resultar em cara ou coroa. jogue as opções dentro de uma lista
##e depois crie um orgrama qua imprime "cara" ou "coroa" na tela

moeda = ['cara', 'coroa']
print(random.choice(moeda))

# Desafio 2 
## Você quer fazer um sorteio entre 5 nomes em uma lista de nomes. Crie uma lista de 5 nomes e sorteie um nome de dentro dessa lista e exiba na tela.

nomes = ['marcio', 'greice', 'aurora', 'lindinha','paçoca']
print(random.choice(nomes))

# Desafio 3
## Você quer escolher aleatóriamente um número de 10-100. imprima na tela um valor aleatório de 10-100. 
print(random.randint(10, 100))

