# Funções em python inicia com a palavra 
# reservada "def"
# Funções são rotinas em seu conceito
# São blocos de código que só serão executados quando chamados

############################################

def saudacao():
    print("Olá Mundo")


# Chama a função
saudacao()
############################################


def linha():
    print("-" * 30)


linha()
print("MODULO 01")
linha()
print("ALGORITMOS")
linha()
print("ANALISE DE DADOS")
linha()

##########################################


def saudacao(nome):
    print(f"Olá {nome}!")


nome = input("Digite seu nome: ")
saudacao(nome)

##########################################


def soma(n1, n2):
    somar = n1 + n2
    print(f"A soma de {n1} + {n2} é igual a {somar}")


def subtracao(n1, n2):
    subtrair = n1 - n2
    print(f"A subtração de {n1} - {n2} é igual a {subtrair}")


def multiplicacao(n1, n2):
    multiplicar = n1 * n2
    print(f"A multiplicação de {n1} * {n2} é igual a {multiplicar}")


def divisao(n1, n2):
    if n2 == 0:
        print("Não é possível dividir por zero")
    else:
        dividir = n1 / n2
        print(f"A divisão de {n1} / {n2} é igual a {dividir}")


n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma(n1, n2)
subtracao(n1, n2)
multiplicacao(n1, n2)
divisao(n1, n2)

###########################################


def somar_numeros(x, y):
    s = x + y
    return s


for i in range(3):
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

soma = somar_numeros(n1, n2)
print(soma)