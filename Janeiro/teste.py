invalidos = []
duplicados = []
cadastros = {}
def verificacao():

    if not len(cpf_int) == 11:
        invalidos.append((nome, idade_int, cpf_int))
    
    if not nome.isalpha():
        invalidos.append((nome, idade_int, cpf_int))
    
    if not idade_int >= 0 and idade_int <= 120:
        invalidos.append((nome, idade_int, cpf_int))

    if cpf_int in cadastros:
        duplicados.append({"cpf": cpf_int, "nome":nome, "idade": idade_int})
    else:
        cadastros[cpf_int]={"nome": nome, "idade": idade_int}

    return invalidos, cadastros, duplicados

while True:
    print("Digite o nome, idade e cpf separado por virgula ou SAIR ")
    entrada = input("").strip()


    if entrada.upper() == "SAIR":
        break
    else:
        print("Continuando o código ...")
        print("========================")

    partes = [p.strip() for p in entrada.split(",")]

    if len(partes) != 3:
        print("Formato incorreto, Use Nome, Idade, CPF")
    else:
        nome, idade_str, cpf_str = partes
        cpf_int = cpf_str.replace("-","").replace(".","")
        idade_int = int(idade_str)
       #print(nome, cpf_int, idade_int)
        verificacao()
print("Lista")
print(invalidos)
print("Dicionário")
print(cadastros)