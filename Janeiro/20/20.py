while True:
    primeiro_numero = input("Digite um numero inteiro! ").strip()
    if primeiro_numero.isdigit():
        inicio = int(primeiro_numero)
        break
    else:
        print("Numero incorreto, tente novamente !")
while True:
    segundo_numero = input("Digite o segundo numero! ").strip()
    if segundo_numero.isdigit():
        final = int(segundo_numero)
        if final > inicio:
            break
        else:
            print("Segundo numero é menor ou igual ao primeiro")
    else:
        print("Numero incorreto, tente novamente !")
par = 0 
impar = 0
soma_impar = 0
soma_par = 0

for i in range(inicio, final + 1):
    
    if i % 2 == 0:
        soma_par += i
        par += 1
     
        print(f"{i} é par")
    else:
        soma_impar += i
        impar += 1
        print(f"{i} é ímpar")
    
print(f"Total de pares: {par}")
print(f"Total de ímpares: {impar}")
print(f"Soma dos pares: {soma_par}")
print(f"Soma dos ímpares: {soma_impar}")