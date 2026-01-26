cadasto = {
    "cpf":{
            "nome": "",
            "idade":""
            }
}

duplicados = []
invalidos = []

def verificacao():

    if cpf_int == cadasto[cpf]:
        duplicados.append(cpf_int, nome, idade_int)

    elif not nome.isalpha() or not idade_int.isdigit() or not cpf_int.isdigit():
        invalidos.append(cpf_int, nome, idade_int)

    else:
        cadasto[cpf_int]={"nome":nome, "idade": idade_int}

    return cadasto, duplicados, invalidos
while True:

    entrada = input("Digite o nome, idade e cpf separado por virgula ou SAIR ").strip()
    
    if entrada.upper() == "SAIR":
        break
    partes = [p.strip() for p in entrada.split(",")]

    if len(partes) != 3:
        print("Formato incorreto. Use: Nome,Idade,cpf")
    else:
        nome, idade_str, cpf_str = partes
        print(type(idade_str))
        print(type(cpf_str))
        #idade_int = int(idade_str)
        #cpf_int = int(cpf_str)
        
        print(nome, idade_str, cpf_str)
        verificacao()
print(cadasto)
print(duplicados)
print(invalidos)