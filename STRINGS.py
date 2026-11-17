# 01

# palavra = "Python" 
# print(palavra[0]) 
# print(palavra[5]) 
# print(len(palavra)) 
# notas = [7.5, 8.0, 6.0] 
# print(notas[1]) 
# print(len(notas)) 

# 02

# palavra = "logica"
# def inverter_string(palavra):
#     return palavra[::-1]

# def escrever_string(palavra):
#     return palavra

# print(inverter_string(palavra))
# print(escrever_string(palavra))

# 03

# nome = "Guilherme" 
# print("Olá, " + nome + "!") 
# print("-" * 20) 
# print("ha" * 3) 

# 04

# nome = input("Digite seu nome: ")
# print("=" * 10)
# print("Olá, " + nome + "!")
# print("=" * 10)
# print('seu nome tem ' + str(len(nome)) + ' letras.')

# 05

# palavra = input("Digite uma palavra: ") 
# indice = 0 
# while indice < len(palavra): 
#     print(indice, palavra[indice]) 
#     indice = indice + 1 

# 06

# frase = input("Digite uma frase: ")
# vogais = "aeiouAEIOU"
# contador = 0
# for caractere in frase:
#     if caractere in vogais:
#         contador += 1
# print(f"A frase '{frase}' tem {contador} vogais.")

# 07

# palavra = input("Digite uma palavra: ")
# print("A palavra invertida é:", palavra[::-1])

# 08

# texto = "eu gosto de python"
# print(texto.upper(texto))
# print(texto.lower(texto))
# print(texto.title(texto))
# print(texto.count("o"))
# print(texto.replace("python", "c"))
# print(texto.split(" "))
# print(texto.find("gosto"))
# print(texto.startswith("eu"))
# print('oi' .strip(texto))

# 09

# texto = "Programacao" 
# print(texto[0:3]) 
# print(texto[3:7]) 
# print(texto[:4]) 
# print(texto[7:]) 
# print(texto[::2]) 
# print(texto[::-1])

# 10

# frase = input("Digite uma frase: ")
# frase_invertida = frase[::-1]
# # frase = frase.replace(" ", "")
# if frase == frase_invertida:
#     print("A frase é um palíndromo.")
# else:
#     print("A frase não é um palíndromo.")

# 11

# palavra = "gato"
# palavra = "p" + palavra[1:]
# print(palavra)  # Saída: "pato"

# 12

# frutas = ["maçã", "banana", "uva"] 
# print(frutas[0]) 
# frutas[1] = "manga"       # troca o item da posição 1 
# frutas.append("caju")     # append: adiciona no final 
# print(frutas) 
# print(len(frutas))
# print(frutas)

# 13

# itens = []
# n = int(input('quantos itens você quer? '))
# contador = 0 

# while contador < n:
#     item = input('digite um item: ')
#     itens.append(item)
#     contador += 1

# print('\nlistas de compras: ')

# contador = 0
# while contador < n:
#     print(f'{contador + 1} - {itens[contador]}')
#     contador += 1

# 14

# notas = [7.0, 5.5, 9.0, 8.5] 
# soma = 0 
# indice = 0 
# while indice < len(notas): 
#     soma = soma + notas[indice] 
#     indice = indice + 1 
# print("Média:", soma / len(notas)) 

# 15

# notas = [7.0, 5.5, 9.0, 8.5] 
# soma = 0 
# indice = 0 
# while indice < len(notas): 
#     soma = soma + notas[indice] 
#     indice = indice + 1 
# print("Média:", soma / len(notas)) 
# print('maior nota: ' + str(max(notas)))
# print('menor nota: ' + str(min(notas)))
# print('soma das notas: ' + str(sum(notas)))

# 16

# nums = [5, 2, 8, 2]
# nums.insert(0, 1) 
# print(nums)  # Saída: [1, 5, 2, 8, 2]
# nums.remove(2) 
# print(nums)  # Saída: [1, 5, 8, 2]
# nums.pop()
# print(nums)  # Saída: [1, 5, 8]
# nums.sort()
# print(nums)  # Saída: [1, 5, 8]
# nums.reverse()
# print(nums)  # Saída: [8, 5, 1]
# nums.index(5)
# print(nums)  # Saída: [8, 5, 1]
# 8 in nums
# print(nums)  # Saída: [8, 5, 1]

# 17

# cores = ["azul", "verde", "roxo"] 
# print(cores[3]) 

# 18

# frase = "estudar python todo dia" 
# palavras = frase.split() 
# print(palavras) 
# print(len(palavras)) 
# print("-".join(palavras)) 
# print("1,2,3".split(","))

#  19

# palavra = "casa" 
# for letra in palavra: 
#     print(letra) 
 
# notas = [7.0, 5.5, 9.0] 
# for nota in notas: 
#     print(nota) 

# 20

# frase = input("Digite uma frase: ")
# contador = 0

# print(len(frase))

# palavras = frase.split()

# print(len(palavras))
# print(frase.upper())

# for letra in frase:
#     if letra.lower() in "aeiou":
#         contador += 1

# print('total de vogais:', contador)
# print('maior palavra: ' + str(max(palavras)))

# 21

# n = int(input('quantos nomes serão digitados? '))
# contador = 0
# lista = []
# while contador < n:
#     nomes = input('digite o nome: ')
#     if nomes not in lista:
#         lista.append(nomes)
#     contador += 1
# print(lista)