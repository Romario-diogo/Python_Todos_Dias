cadasto = {
    cpf:{
            "nome": "",
            "idade":""
            }
}

duplicados = []
invalidos = []

def verificacao():

    if cpf_str == cadasto[cpf]:
        duplicados.append(cpf_str, nome, idade_str)


while True:

    entrada = input("Digite o nome, idade e cpf separado por virgula ou SAIR ").strip()
    
    if entrada.upper() == "SAIR":
        break
    partes = [p.strip() for p in entrada.split(",")]

    if len(partes) != 3:
        print("Formato incorreto. Use: Nome,Idade,cpf")
    else:
        nome, idade_str, cpf_str = partes
        print(nome, idade_str, cpf_str)

