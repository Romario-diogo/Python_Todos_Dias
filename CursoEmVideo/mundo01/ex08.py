while True:
    entrada = input("Digite um numero em metros inteiro: ")
    if entrada.isdigit():
        entrada = int(entrada)
        break
    else:
        print("Digite um numero interio!!!")


print(f"Numero em KM {entrada / 1000}")
print(f"Numero em HM {entrada/ 100}")
print(f"Numero em dan {entrada / 10}")
print(f"Numero em metros {entrada}")
print(f"Numero em metros {entrada *10}")
print(f"Numero em metros {entrada * 100}")
print(f"Numero em metros {entrada * 1000}")