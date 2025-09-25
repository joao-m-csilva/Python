# Funções em Python são blocos de códigos reutilizáveis que realizam uma tarefa específica.

def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo ao programa.")

print("\n Chamando a função saudacao: ")
saudacao("João")
saudacao("Maria")


# Retornando o quadrado de um número que eu receber 
def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("Chamando a função quadrado:")
print(quadrado(4))
print(quadrado(7))
resultado_quadrado = quadrado(5)
print(f"O quadrado de 5 é {resultado_quadrado}.")

# Recebendo mais do que 1 parâmetro na função (função com múltiplos parâmetros)

def soma(a, b):
    return a + b

print("Chamando a função soma:")
print(soma(3, 5))
print(soma(10, 20))

def soma(a, b):
    resultado = a + b
    return resultado

print("Chamando a função soma:")
resultado_soma = soma(3, 5)
print(f"A soma de 3 e 5 é {resultado_soma}.")
print(soma(10, 5))
print(soma(78, 20))


def soma(a, b):
    resultado = a + b
    return resultado
print("Chamando a função soma:")
numero1 = 20
numero2 = 30
resultado_soma = soma(numero1, numero2)
print("A soma do numero %s e o numero %s é %s." % (numero1, numero2, resultado_soma))