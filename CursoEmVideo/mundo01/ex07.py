while True:
    nome = input("Digite o nome do aluno: ")
    if nome.isalpha():
        break
    else:
        print("Digite um nome apenas com letras ")

nota01 = float(input("Digite a nota do aluno: "))
nota02 = float(input("Digite o segunda nota do aluno "))

print(f"O aluno {nome} tem a nota {nota01} e {nota02} e a média é igual a {(nota01+nota02)/2}")