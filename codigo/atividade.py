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
def calculoMulta(qtd):
    multa = qtd * MULTAKG
    return multa


MULTAKG = 4.00
QUILOSPERMITIDOS = 100

pesoPescado = float(input("Digite o peso do pescado: "))

if pesoPescado > QUILOSPERMITIDOS:
    excedente = pesoPescado - QUILOSPERMITIDOS
    vlMulta = calculoMulta(excedente)
    print(f"o excedente foi: {excedente}kg e o valor da multa é R${vlMulta}")
else:
    print("Não houve excedente, portanto não há multa.")