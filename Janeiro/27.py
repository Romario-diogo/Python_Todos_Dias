"""
menu de entrada com opções
digite (Usuario; acao; tempo)
Entrada 
verificar entra 
se entrada == sair 
    se entrada tem logs (dicionario e lista incorretos)?
        sim, apresentação em tupla ordenado por tempo total do usuário
        função (somar tempo total)
        salvar na tupla
        imprimir a tupla 
        break
    se não 
        mensagem(Não podemos encerrar sem logs armazenados)
    
se nao se 
    funcao para separação de entradas 
    nome, acao, tempo = entrada

    se nome é apenas letras ?
        sim
        se nome ja existe ?
            sim, não armazenar 
        se não
            crie um novo usuario
    se não:
        armazenar nas incorretas (lista de diconario)
        break
        
    se ação esta na lista de comparação (EM MAIUSCULO)?
        sim
        se ação ja existe ?
            sim, armazena e proximo
        se não:
            cria e armazena e proximo
    se não:
        armazenar nas incorretas (lista de diconario)
        break
        
    se tempo é um numero enteiro ?
        sim, armazenar em validos 
    se não 
        armazena nas incorretas (lista de diconario)


"""