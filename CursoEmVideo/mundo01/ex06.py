while True:
    numero = input("Digite um numero inteiro: ")

    if numero.isdigit():
        numero = int(numero)
        break
    else:
        print("Digite um numero inteiro")
print(f"O dobro de {numero} vale {numero*2}")
print(f"O triplo de {numero} vale {numero *3}")
print(f"A raiz quadrada de {numero} é igual a {numero**0.5:.2f}.")