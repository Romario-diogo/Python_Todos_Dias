

def inicio_final():
        while True:
            inicio = input("Digite um numero inteiro ! ").strip()
            if inicio.isdigit():
                inicio_int = int(inicio)
                break
            else:
                print("Digite um numero inteiro !")
        while True:
            final = input("Digite um numero final !").strip()
            if final.isdigit():
                final_int = int(final)
                if final_int > inicio_int:
                    break
                else:
                    print("Numero final é menor ou igual ao do inicio")
            else:
                print("Numero final incorreeto, digite novamente !")
        return inicio_int, final_int 

def mostrar():
    par = 0 
    impar = 0
    soma_impar = 0
    soma_par = 0
    for i in range(inicio_int, final_int + 1):
        
        if i % 2 == 0:
            soma_par += i
            par += 1
        
            print(f"{i} é par")
        else:
            soma_impar += i
            impar += 1
            print(f"{i} é ímpar")
        
    print(f"Total de pares: {par}")
    print(f"Total de ímpares: {impar}")
    print(f"Soma dos pares: {soma_par}")
    print(f"Soma dos ímpares: {soma_impar}")
    print(f"Menor valor {inicio_int}")
    print(f"Maior valor {final_int}")

tem_intervalo = False

while True:
    print("1 - Digite intervalo (início e final)")
    print("2 - Mostre resumno do último intervalo")
    print("3 - Sair")
    escolha = input(" ")
    if escolha.isdigit():
        entrada = int(escolha)  
        if entrada == 1:
            inicio_int, final_int = inicio_final()
            tem_intervalo = True
        elif entrada == 2:
            if not tem_intervalo:
                print("Nenhum intervalo cadastrado ainda.")
            else:
                mostrar()
            
        elif entrada == 3:
            break
        else:
            print("Escolha uma das opções")

