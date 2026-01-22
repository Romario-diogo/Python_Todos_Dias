#def add_carrinho():


carrinho = {}
while True:
    print("1 Adicionar item ao carrinho")
    print("2 Remover item do carrinho")
    print("3 Ver carrinho (itens + subtotal)")
    print("4 Aplicar cupom de desconto")
    print("5 Finalizar compra (checkout)")
    print("6 Sair")
    escolha_menu = input("")

    if escolha_menu.isdigit():
        escolha_menu_int = int(escolha_menu)
        if escolha_menu_int > 0 and escolha_menu_int <= 6:    
            match escolha_menu_int:
                case 1:
                    produto = input("Digite o nome do produto: ")
                    preco = input("Digite o valor do produto: ")
                    qtd = input("Digite a quantidade do produto: ")
                    print("=====================================")
                    carrinho = {
                        produto: {
                            "Preco": preco,
                            "Quantidade": qtd

                            
                        }
                    }

                case 2:
                    print("Opção 02")
                case 3:
                    for produto, detalhes in carrinho.items():
                        print(f"Produto {produto}")
                        print(f"Valor {detalhes['Preco']}")
                        print(f"Quantidade {detalhes['Quantidade']}")
                case 4:
                    print("Opção 04")
                case 5: 
                    print("Opção 05")
                case 6:
                    print("opção 06")
        else:
            print("Digite um numero entre as opções")
            print("================================")
    else:
        print("Digite um numero válido !")
        print("=========================")