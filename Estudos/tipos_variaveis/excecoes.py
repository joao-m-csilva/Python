# Exceções são eventos que ocorrem durante a execução do código, e podem interromper o programa caso não sejam tratadas adequadamente

# Captura de exceções
print("Exemplo de captura de exceções")
try:
        numero = int(input("Digite um número inteiro: "))
        resultado = 10 / numero
        print(f"Resultado: {resultado}")
except Exception as e:
        print(f"Erro: {e}")
        raise ValueError("Tipo de variáveis incompatíveis.")