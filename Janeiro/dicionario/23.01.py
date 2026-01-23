aluno = {
    "Nome": "Bob",
    "Idade": 19,
    "Cidade": "Maua",
    "Curso": "Analista de dados"
}

print (f"Nome do aluno {aluno.get("Nome")}")
#Trocando o nome
aluno["Nome"]="Romário"
print(f"Nome do novo aluno {aluno.get("Nome")}")

#Adicionando nova chave e valor
aluno["CPF"]=12344566
print(aluno)

