lista_entrada = []
while True:
    entrada = input("Digite um numero inteiros, caso deseja sair digite SAIR: ")
    if entrada.isdigit():
        lista_entrada.append(int(entrada))
    elif entrada.upper() == "SAIR":
        break
    else:
        print("Digite um numero inteiro válido ou Sair")
cont_par = 0
cont_impar = 0
soamr_numeros = 0
menor = lista_entrada[0]
maior = lista_entrada[0]
for numero in lista_entrada:
    if numero < menor:
        menor = numero
    if numero > maior:
        maior = numero


print(lista_entrada)
print(f"Quantidade de numeros válidos {len(lista_entrada)}")

for i in lista_entrada:
    if i % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
print(f"Quantidade de Numeros pares são: {cont_par}")
print(f"Quantidade de Numeros impares são: {cont_impar}")
print(f"Soma total dos número {sum(lista_entrada)}")
print(f"Maior Numero da lisra é {maior}")
print(f"Menor Numero da lista é {menor}")
