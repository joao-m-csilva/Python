# Dicionário =  Coleção não ordenada de pares chave-valor

# Criando um dicionário de exemplo 

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Acessando valores do dicionário
print(pessoa["nome"])  # Saída: João
print(pessoa["idade"])  # Saída: 30
print(pessoa["cidade"])  # Saída: São Paulo

# Adicionando um novo par chave-valor
pessoa["profissão"] = "Engenheiro"
print(pessoa)

# Alterar ou atualizar um valor já existente 

pessoa["idade"] = 31
print("Idade Atualizada:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["idade"]
print(pessoa)

# Método keys = Retorna todas as chaves do dicionário em formato de lista

chaves = list(pessoa.keys())
print(chaves)
print(chaves[0])  # Acessando a primeira chave


# Método value = Retorna os valores do dicionário em formato de lista

valores = list(pessoa.values())
print(valores[0])  # Acessando o primeiro valor
print(valores)


# Método items = Retorna os valores do dicionário em formato de tupla

itens = list(pessoa.items())
print(itens)
print(itens[0][1])  # Acessando o primeiro item (tupla)
print("Primeira chave-valor: %s = %s" % (itens[0][0], itens[0][1]))  # Exibindo o primeiro item como chave-valor
