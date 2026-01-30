nome = input("Digite seu nome: ")
idade = input("digite seu idade ")
idade = int(idade)
if idade < 18:
    print("=============================================================")
    print(f"Olá,{nome} voce não pode digirir porque tem {idade} anos !!!")
    
else:
    print("================================================")
    print(f"Olá {nome} voce pode dirigir por que tem {idade} anos")