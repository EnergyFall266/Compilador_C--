import tokens as token
import sintatico as sintatico
import string

if __name__ == "__main__":
    f = open('exemploCodigo.txt', 'r', encoding="utf8")
    arq3end = open('arquivo3enderecos.txt', 'a', encoding="utf8")
    arq3end.truncate(0)

    numeroLinha = 0
    simbolos = [';', ':', '{','}','(',')', '+', '-', '*', '/', '&', '|']
    comparacao = ['=','<','>','!']
    pattern = string.ascii_letters+"_"+string.digits+"."

    for linha in f:
        numeroLinha+=1
        verificaCaractere = True
        
        if(linha[0] == "¬" and linha[1] != "¬"):
            #erro
            print("Termo não esperado: ", linha[1])
            print("Linha: ", numeroLinha)
            break
        elif((linha[0] == "¬" and linha[1] == "¬") or (linha[0] == "\n")):
            pass
        else:
            char = 0
           
            while char < len(linha):
                
                if(linha[char] in simbolos):
                    #enviar token de simbolo
                    token.simbolos(linha[char], numeroLinha)
                    verificaCaractere = True
                elif(linha[char] in comparacao):
                    move = token.comparacao(linha[char:char+2], numeroLinha)
                    char += (move-1)
                    verificaCaractere = True
                elif(linha[char] == "'"):
                    #enviar token char (vai ser enviado todos os caracteres após ')
                    move = token.char_string(linha[char:], numeroLinha)
                    char += (move-1)

                elif(linha[char] == "\""):
                    #enviar token string ou print
                    move=token.char_string(linha[char:-2], numeroLinha)
                    char += (move-1)
                elif(linha[char].isnumeric() and linha[char-1] not in pattern):
                    #verificar se é inteiro ou real e gera seu respectivo token
                    move = token.verificaNumero(linha[char:], numeroLinha)
                    char += (move-1)
                elif(linha[char].isalnum and verificaCaractere and not linha[char]==' '):
                    #verificar se é alguma palavra, operando ou operador
                    token.operadorSimbolos(linha[char:-1], numeroLinha)
                   
                    # colocar flag para quandor ler tipo e em seguida 
                    verificaCaractere = False
                    
                char += 1
    for i in token.token_lista:
        print(i) 

    #adiciona $ ao final da string a ser lida
    token.token_lista.append('$')

    #filtra apenas os tokens 
    #tokens = [x[0] for x in token.token_lista]

    #analiseSintatica = 0 -> erro; analiseSintatica = 1 -> string aceita
    analiseSintatica = sintatico.bottom_up(token.token_lista, arq3end)
    

                 