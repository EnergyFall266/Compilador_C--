#colocar as variaveis q vem dps do tipo dado
# fazer split dentro do 
# token = token.split(" ")
# vai ser recebido uma string que vai começar com letra
# passo1: identificar se tem operadores(+,*)
# passo2: dar replace nestes operadores e simbolos por espaço
# passo3: dar split nos espaços
# passo4: fazer verificação nos if

import string
from os import replace

token_lista = []
lista_variaveis = []

digitos = string.digits

def geraErro(caractere, numeroLinha):
    token_lista.append(['erro', caractere, numeroLinha])

def verificaNumero(numero, numeroLinha):
    valor=numero[0]
    for i in range(len(numero)):
        if(numero[i+1] in digitos):
            valor += numero[i+1]
            continue
        elif(numero[i+1] == '.'):
            valor += numero[i+1]
            if(numero[i+2] in digitos):
                temp = numero[i+2: ]
                
                print("temp", temp)
                print("valor", valor)
                for j in range(len(temp)):
                    print(j, temp[j])
                    if(temp[j] in digitos):
                        valor += temp[j]
                        continue
                    break 

                token_lista.append(['real', valor])
                print(valor)
                break
            else:
                #gerar token de erro (. sem um numero em seguida)
                token_lista.append(['erro', numero[i+2], numeroLinha])
                print("erro")
                break
        else:
            #gerar token numero inteiro
            token_lista.append(['inteiro', valor])
            print(valor)
            break

def tipo_dado(token):
    global token_lista, lista_variaveis
     
    if token[0] == 'int':
        token_lista.append(['tipo_dado', token[0]])
        del token[0]
        lista_variaveis.extend(token)
        del token[:]

    elif token[0] == 'float':
        token_lista.append(['tipo_dado', token[0]])
        del token[0]
        lista_variaveis.extend(token)
        del token[:]

    elif token[0] == 'double':
        token_lista.append(['tipo_dado', token[0]])
        del token[0]
        lista_variaveis.extend(token)
        del token[:]

    elif token[0] == 'char':
        token_lista.append(['tipo_dado', token[0]])
        del token[0]
        lista_variaveis.extend(token)
        del token[:]

    elif token[0] == 'bool':
        token_lista.append(['tipo_dado', token[0]])
        del token[0]
        lista_variaveis.extend(token)
        del token[:]
    if len(token)!=0:
       reservadas(token)

def simbolos(token):
    if token == ',':
        token=token.replace(",", " ")
    elif token == '(':
        token_lista.append(['abre_parenteses',token])
        token=token.replace("(", " ")
    elif token == ')':
        token_lista.append(['fecha_parenteses', token])
        token=token.replace(")", "")
    elif token == '{':
        token_lista.append(['abre_chaves',token])
        token=token.replace("{", " ")
    elif token == '}':
        token_lista.append(['fecha_chaves',token])
        token=token.replace("}", "")
    elif token == ':':
        token_lista.append(['dois_pontos',token])
        token=token.replace(":", " ")
    elif token == ';':
        token_lista.append(['ponto_virgula',token])
        token=token.replace(";", " ")

def operadorSimbolos(caracteres):   
    global token, token_lista
    
    token=caracteres
    for i in range(len(token)-1):
        if token[i] == '+':
            token_lista.append(['operador_sum', token[i]])
            token=token.replace("+", " ")
        elif token[i] == '-':
            token_lista.append(['operador_sum',token[i]])
            token=token.replace("-", " ")
        elif token[i] == '*':
            token_lista.append(['operador_mul',token[i]])
            token=token.replace("*", " ")
        elif token[i] == '/':
            token_lista.append(['operador_mul',token[i]])
            token=token.replace("/", " ")

        elif token[i] == '&':
            token_lista.append(['op_logicos',token[i]])
            token=token.replace("&", " ")
        elif token[i] == '|':
            token_lista.append(['op_logicos',token[i]])
            token=token.replace("|", " ")

        elif token[i] == ',':
            token=token.replace(",", " ")
        elif token[i] == '(':
            token=token.replace("(", " ")
        elif token[i] == ')':
            token=token.replace(")", "")
        elif token[i] == '{':
            token=token.replace("{", " ")
        elif token[i] == '}':
            token=token.replace("}", "")
        elif token[i] == ':':
            token=token.replace(":", " ")
        elif token[i] == ';':
            token=token.replace(";", " ")

        elif token[i] == '>':
            if token[i+1] == '=':
                token_lista.append(['op_relacional', token[i]+token[i+1]])
                token=token.replace(">=", " ")
            else:
                token_lista.append(['op_relacional', token[i]])
                token=token.replace(">", " ")
        elif token[i] == '<':
            if token[1+1] == '=':
                token_lista.append(['op_relacional', token[i]+token[i+1]])
                token=token.replace("<=", " ")
            elif token [i+1] == '>':
                token_lista.append(['op_relacional', token[i]+token[i+1]])
                token=token.replace("<>", " ")
            else:
                token_lista.append(['op_relacional', token[i]])
                token=token.replace("<", " ")

        elif token[i] == '=':
            if token[i+1] == '=':
                token_lista.append(['op_relacional', token[i]+token[i+1]])
                token=token.replace("==", " ")
                
            else:
                token_lista.append(['atribuicao', token[i]])
                token=token.replace("=", " ")
        elif token[i] == '!':
            token_lista.append(['operador_not', token[i]])
            token=token.replace("!", " ")
        
    token=token.split(" ")  
    exclui=0
    for iter in range(len(token)):
        if len(token[exclui])==0:
            token.pop(exclui)
        else:
            exclui+=1   
    print("opsimb")
    print(token)
    tipo_dado(token)
     
def char_string(token):
    global token_lista
    for i in range(len(token)):    
        if token[i][0] == '"' and token[i][-1] == '"':
            token_lista.append(['cadeia_print', token[i]])

        elif token[i][0] == "'" and token[i][-1] == "'":
           token_lista.append(['char', token[i]]) 
        elif token[i] == 'true':
            token_lista.append(['booleano', token[i]])
        elif token[i] == 'false':
            token_lista.append(['booleano', token[i]])

def operandos(token):
    global token_lista, lista_variaveis
    for k in range(len(token)):
        for indice in range(len(lista_variaveis)):
            if token[k] == lista_variaveis[indice]:
                token_lista.append(['operando', token[k]])

    char_string(token)

def reservadas(token):
    global token_lista
    # print(token)
    if token[0] == "if":
        token_lista.append(['palavra_reservada', token[0]])
        del token[0]
    elif token[0] == 'else':
        token_lista.append(['palavra_reservada', token[0]])
        del token[0]
    elif token[0] == 'for':
        token_lista.append(['palavra_reservada', token[0]])
        del token[0]
    elif token[0] == 'switch':
        token_lista.append(['palavra_reservada', token[0]])
        del token[0]
    elif token[0] == 'case':
        token_lista.append(['palavra_reservada', token[0]])
        del token[0]
    elif token[0] == 'while':
        token_lista.append(['palavra_reservada', token[0]])
        del token[0]
    elif token[0] == 'print':
        token_lista.append(['palavra_reservada', token[0]])
        del token[0]
    elif token[0] == 'scan':
        token_lista.append(['palavra_reservada', token[0]])
        del token[0]
    elif token[0] == 'break':
        token_lista.append(['palavra_reservada', token[0]])
        del token[0]
    elif token[0] == 'default':
        token_lista.append(['palavra_reservada', token[0]])
        del token[0]
    elif token[0] == 'null':
        token_lista.append(['palavra_reservada', token[0]])
        del token[0]
    
    operandos(token)
'''
if __name__ == '__main__':
    token = "if==('nota'+nota2\")"
    token_lista=[]
    lista_variaveis = ['nota2', 'nota']
    operando_simbolos()
    "sd s"'''