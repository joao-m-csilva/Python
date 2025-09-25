# Loop é um estrutura que permite repetir um bloco de código enquanto uma condição for verdadeira 

lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

tupla = (1, 2, 3, 4, 5)
for elemento in tupla:
    print(elemento)

pessoa = {"Nome": "João", "Idade": 30, "Cidade": "São Paulo"}
for chave in pessoa:
    print(chave, ":", pessoa[chave])

for chave in pessoa.keys():
    print(chave)
for chave in list(pessoa.keys()):
    print("\n", chave)

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, ":", valor)

# range = retorna um intervalo númerico em formato de lista 

print(list(range(0,11)))

for numero in range(0,11):
    print("Número: ", numero)  

print("\n Utilizando a função range () com len()")
lista = [1, 2 , 3 , 4, 5]
for indice in range(0, len(lista)):
   print("Índice:", indice)
   print("Elemento:", lista[indice])
   if indice == 3:
       lista[indice] = 5
print(lista)

# enumerate 

lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
   print("Índice:", indice)
   print("Elemento:", valor)    
   print(f"{indice}: {valor}")
