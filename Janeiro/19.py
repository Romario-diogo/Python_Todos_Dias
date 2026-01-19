while True:
    entrada = input("Digite um numero inteiro ! ")
    if entrada.isdigit():
        numero = int(entrada)
        break
    else:
        print("Numero incorreto, tetente novamente! ")

cont = 0
for i in range(0, numero + 1 , 2):
    print(i)