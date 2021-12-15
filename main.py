import tokens as token
import string

if __name__ == "__main__":
    f = open('exemploCodigo.txt', 'r', encoding="utf8")
    numeroLinha = 0
    simbolos = [';', ':', '{','}','(',')']
    pattern = string.ascii_letters+"_"+string.digits+"."

    for linha in f:
        numeroLinha+=1
        verificaCaractere = True
        
        if(linha[0] == "¬" and linha[1] != "¬"):
            #enviar token de erro, com a respectiva linha
            token.geraErro(linha[1], numeroLinha)
        elif((linha[0] == "¬" and linha[1] == "¬") or (linha[0] == "\n")):
            pass
        else:
            for char in range(len(linha)):
                
                if(linha[char] in simbolos):
                    #enviar token de simbolo
                    token.simbolos(linha[char])
                elif(linha[char] == "'"):
                    #enviar token char (vai ser enviado todos os caracteres após ')
                    print(linha[char:])
                    break
                elif(linha[char] == "\""):
                    #enviar token string ou print
                    print(linha[char:-2])
                    break
                elif(linha[char].isnumeric() and linha[char-1] not in pattern):
                    #verificar se é inteiro ou real e gera seu respectivo token
                    token.verificaNumero(linha[char:], numeroLinha)
                elif(linha[char].isalnum and verificaCaractere):
                    #verificar se é alguma palavra reservada, operando ou operador
                    token.operadorSimbolos(linha[char:])
                    print(linha[char:])
                    verificaCaractere = False 

    print(token.token_lista)              