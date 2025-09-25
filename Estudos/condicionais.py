#if, elif e else 

#Exemplo de if

idade = 11
print("Exemplo de comando if")
if idade >= 18:
    print("Maior de idade")

if idade == 18:
    print("Idade é 18")

if idade < 18:
    print("Menor de idade")

if idade > 18:
    print("Maior de idade")

if idade <= 18:
    print("Menor de idade")

if idade != 18:
    print("Idade não é 18")

# Exemplo de else

if idade >= 18: 
    print("Maior de idade")
else:
    print("Menor de idade")

# Exemplo de elif

if idade > 18:
    print("Idade é maior que 18")
elif idade == 7:
    print("Idade é 18")
elif idade == 15:
    print("Idade é 15")
else:
    print("Idade é menor que 15")

# if e else em apenas 1 linha 

mensagem = "Você pode tirar a CNH" if idade >= 18 else "Você não pode tirar a CNH" 
print(mensagem)