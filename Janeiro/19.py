while True:
    entrada = input("Digite um numero inteiro ! ")
    if entrada.isdigit():
        numero = int(entrada)
        break
    else:
        print("Numero incorreto, tetente novamente! ")
cont1 = 0
cont = 0
for i in range(0, numero + 1 , 2):
    cont += i
    cont1 += 1
    print(i)
print(f"Soma dos pares: {cont}")
print(f"Total de pares: {cont1}")