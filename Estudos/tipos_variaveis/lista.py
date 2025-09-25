# Lista = coleção de elementos ordenados e mutáveis

minha_lista = [1, 2, 3, 4, 5,]

print("Minha lista de exemplo:", minha_lista)

#Acessando elementos da lista

print("Primeiro elemento:", minha_lista[0])
print("Segundo elemento:", minha_lista[1])
print("Último elemento:", minha_lista[-1])

# Fatiamento de lista

print("Fatiamento da lista:")
print("Elementos do índice 1 ao 3:", minha_lista[1:4])
print("Elementos do início até o índice 2:", minha_lista[:3])
print("Elementos do índice 5 até o final:", minha_lista[3:])

# Substituição de elementos
minha_lista[0] = 112
print("Lista após substituição:", minha_lista)

# Métodos de lista

# Append = adiciona elemento no final da lista

minha_lista.append(6)
minha_lista.append(7)
minha_lista.append(8)
minha_lista.append(9)
print("Lista após append:", minha_lista)

# Index = retorna a posição de um elemento na lista

indice = minha_lista.index(4)
print("Índice do elemento 'rockseat':", indice)

# Insert = insere um elemento em um índice específico

minha_lista.insert(1, 3)
print("Lista após insert:", minha_lista)

minha_lista.insert(0, 565)
print("Lista após insert no início:", minha_lista)

#Método POP

minha_lista.pop(2)
print("Lista após pop:", minha_lista)   


#Método REMOVE

minha_lista.remove(9)
print("Lista após remove:", minha_lista)

#Método SORT = aceita apenas elementos do mesmo tipo

minha_lista.sort()
print("Lista após sort:", minha_lista)


