cadastro = {
    "Nome": "",
    "Idade": "",
    "CPF": ""
}

mercadoria = {
    "Iphone": 10000,
    "Tv": 2500,
    "Geladeira": 1500,
    "Cafeteira": 500
}

cupom_desconto = {
    "LOJA100": 10,
    "JANEIROU": 50,
    "NOVCLIENTE": 30
}

while True:
    print("1 - Cadastro")
    print("2 Lista de mercadoria")
    print("3 Lista de cupom de desconto")
    escolha = input("").strip()
    if escolha.isdigit() and int(escolha) > 0 and int(escolha) < 4:
        print(escolha)
        break
    else:
        print("Escolha uma das opções !")