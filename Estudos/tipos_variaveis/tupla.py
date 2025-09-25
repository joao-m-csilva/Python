# Tupla = Coleção ordenada e imutável de elementos

#Criando uma tupla de exemplo

minha_tupla = (1,2,3,4)
print(minha_tupla)
# Acessando elementos da tupla
print(minha_tupla[0])  # Primeiro elemento
print(minha_tupla[1])  # Segundo elemento
print(minha_tupla[-1])  # Último elemento

# Método Count = Retorna a 'quantidade de vezes que um elemento aparece na tupla

contagem = minha_tupla.count(2) 
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

# índice = Retorna o índice da primeira ocorrência do elemento na tupla

indice = minha_tupla.index(3)   
print("Índice do elemento 3:", indice)