while True:
    try:
        reais =  float(input("Digite um número: ").replace(",", "."))
        if reais < 0:
            print("O Valor não pode ser negativo. ")
            continue
        break
    except ValueError:
        print("Entrada inválida.")

print(f"Com o valor R${reais} consegue compara U${reais / 5.20:.2f}")