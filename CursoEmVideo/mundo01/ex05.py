while True:
    numero = input("digite um numero inteiro: ")
    if numero.isdigit():
        numero = int(numero)
        break
    else:
        print("Digite um numero valido ")

print(f"Analisando o valor {numero}, seu antecessor é {numero-1} e seu sucessor é {numero + 1}")