while True:
    num1 = input("Digite um numero inteiro ! ")
    if num1.isdigit():
        num1 = int(num1)
        print("Passou !!!")
        break
    else:
        print("Digite um numero valido inteiro ")
while True:
    num2 = input("Digite um numero inteiro ! ")
    if num2.isdigit():
        num2 = int(num2)
        print("Passou !!!")
        break
    else:
        print("Segundo numero incorreto, digite novamente!!")

print(f"A soma entre {num1} e {num2} é igual a {num1+num2}")
