while True:
    entrada = input("Digite um numero inteiro :").strip()

    if entrada.isdigit():
        entrada_int = int(entrada)
        if entrada_int > 0:
            break
        else:
            print("Digite um numero positivo !")
    else:
        print("Digite novamente, campo digitado caracter ou branco, vaziu !")

cont_impar = 0
cont_par = 0
for i in range(1, entrada_int + 1):
    if i % 2 == 0:
        cont_par += 1
        print(f"Par {i}")
    else:
        cont_impar += 1
        print(f"Impar {i}")

print(f"Total de pares {cont_par}")
print(f"Total de impar {cont_impar}")