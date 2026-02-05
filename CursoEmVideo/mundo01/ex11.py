while True:
    try:
        largura = float(input("Digite a largura da parede: "))
        altura = float(input("Digite a altura da parede: "))
        if largura < 0:
            print("A Largura não pode ser negativo.")
            continue
        if altura < 0:
            print("A Altura não pode ser negativo.")
            continue
        break
    
    except ValueError:
        print("valor incorreto!")

print(f"Largura {largura} * Altura {altura} = metros quadrados {largura*altura:.2f}")
print(f"Vamos precisar de {(largura*altura) / 2:.2f} litros de tinta!")