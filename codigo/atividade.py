# def calculo(n1):

#     dobro = n1 * 2
#     print(f"O dobro do número é: {dobro:.2f}")

#     triplo = n1 * 3
#     print(f"O triplo do número é: {triplo:.2f}")

#     quadrado = n1 * n1
#     print(f"O número ao quadrado é: {quadrado:.2f}")


# n1 = float(input("Digite um número: "))

# calculo(n1)

############################################################


def peixes():
    if pesoPeixes > 100:

        excesso = pesoPeixes - 100
        multa = excesso * 4

        print(f"Peso excedente: {excesso} kg")
        print(f"Valor da multa: R$ {multa:.2f}")
    else:
        print("Peso dentro do limite permitido, não há multa a ser paga.")


pesoPeixes = float(input("Digite o Peso(kg) total dos peixes pescados: "))

peixes()

