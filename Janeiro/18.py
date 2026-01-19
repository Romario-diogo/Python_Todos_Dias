while True:
    numero = input("Digite um numero inteiro ! ")

    if numero.isdigit():
        vlnumero = int(numero)
        break
    else:
        print("Entrada errada, tente novamente !")
cont = 0
for i in range(0, vlnumero + 1, 2):
    cont += 1
    print(i)
print(cont)