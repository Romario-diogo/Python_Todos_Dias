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

def cadastro_cliente():
# Validação Nome
    while True:
        nome = input("Digite o nome do Cliente: ")
        if nome.isalpha():
            cadastro["Nome"]=nome
            break
        else:
            print("Nome digitado para cadastro incorreto, tente novamente!")
# Validação Idade 
    while True:
        idade = input("Digite a idade do cliente: ").strip()
        if idade.isdigit():
            cadastro["Idade"]=int(idade)
            break
        else:
            print("Idade digitada incorreta, tente novamente")
    return


while True:
    print("1 - Cadastro")
    print("2 - Ver cadastro")
    print("3 - Lista de mercadoria")
    print("4 - Adicionar mercadoria")
    print("5 - Finalizar compra")
    escolha = input("").strip()
    if escolha.isdigit() and int(escolha) > 0 and int(escolha) < 6:

        match int(escolha):
            case 1:
                cadastro_cliente()
            case 2:
                print(cadastro)
            case 3:
                for i in mercadoria:
                    print(i)

    else:
        print("Escolha uma das opções !")