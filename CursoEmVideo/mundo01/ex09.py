while True:
    entrada = input("Digite um numero para taboada: ")
    if entrada.isdigit():
        entrada = int(entrada)
        break
    else:
        print("Digite um numero inteiro para ver a taboada!!!")


for i in range(1, 11):
    print(f"{entrada:2} * {i:2} = {entrada*i:3}")