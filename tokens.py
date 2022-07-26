#colocar as variaveis q vem dps do tipo dado
# fazer split dentro do 
# token = token.split(" ")
# vai ser recebido uma string que vai começar com letra
# passo1: identificar se tem operadores(+,*)
# passo2: dar replace nestes operadores e simbolos por espaço
# passo3: dar split nos espaços
# passo4: fazer verificação nos if

from posixpath import split
import string
from os import replace

token_lista = []
lista_variaveis = []

digitos = string.digits

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

                for j in range(len(temp)):
                    if(temp[j] in digitos):
                        valor += temp[j]
                        continue
                    break 

                token_lista.append(['operando', valor, numeroLinha])
                break
            else:
                #gerar token de erro (. sem um numero em seguida)
                print("Termo não esperado: ", valor)
                print("Linha: ", numeroLinha)
                break
        else:
            #gerar token numero inteiro
            token_lista.append(['operando', valor, numeroLinha])
            break
    return len(valor)

def tipo_dado(token, numeroLinha):
    global token_lista, lista_variaveis
     
    if token[0] == 'int':
        token_lista.append(['tipo_dado', token[0], numeroLinha])
        del token[0]
        lista_variaveis.extend(token)
        # del token[:]

    elif token[0] == 'float':
        token_lista.append(['tipo_dado', token[0], numeroLinha])
        del token[0]
        lista_variaveis.extend(token)
        # del token[:]

    elif token[0] == 'char':
        token_lista.append(['tipo_dado', token[0], numeroLinha])
        del token[0]
        lista_variaveis.extend(token)
        # del token[:]

    elif token[0] == 'bool':
        token_lista.append(['tipo_dado', token[0], numeroLinha])
        del token[0]
        lista_variaveis.extend(token)
        # del token[:]
    if len(token)!=0:
       reservadas(token, numeroLinha)
        
def comparacao(token, numeroLinha):
    for i in range(len(token)):    
        if token[i] == '>':
            if token[i+1] == '=':
                token_lista.append(['op_relacional', token[i]+token[i+1], numeroLinha])
                # token=token.replace(">=", " ")
                return 2
            else:
                token_lista.append(['op_relacional', token[i], numeroLinha])
                # token=token.replace(">", " ")
                return 1
        elif token[i] == '<':
            if token[i+1] == '=':
                token_lista.append(['op_relacional', token[i]+token[i+1], numeroLinha])
                # token=token.replace("<=", " ")
                return 2
            elif token [i+1] == '>':
                token_lista.append(['op_relacional', token[i]+token[i+1], numeroLinha])
                # token=token.replace("<>", " ")
                return 2
            else:
            #     token_lista.append(['op_relacional', token[i], numeroLinha])
            #     # token=token.replace("<", " ")
                return 1

        elif token[i] == '=':
            if token[i+1] == '=':
                token_lista.append(['op_relacional', token[i]+token[i+1], numeroLinha])
                # token=token.replace("==", " ")
                return 2
                
            else:
                # token_lista.append(['=', token[i], numeroLinha])
                # token=token.replace("=", " ")
                return 1
        elif token[i] == '!':
            token_lista.append(['!', token[i], numeroLinha])
            # token=token.replace("!", " ")
            return 1

def simbolos(token, numeroLinha):
    if token == ',':
        token=token.replace(",", " ")
    elif token == '(':
        token_lista.append(['(',token, numeroLinha])
        # token=token.replace("(", " ")
    elif token == ')':
        token_lista.append([')', token, numeroLinha])
        # token=token.replace(")", "")
    elif token == '{':
        token_lista.append(['{',token, numeroLinha])
        # token=token.replace("{", " ")
    elif token == '}':
        token_lista.append(['}',token, numeroLinha])
        # token=token.replace("}", "")
    elif token == ':':
        token_lista.append([':',token, numeroLinha])
        # token=token.replace(":", " ")
    elif token == ';':
        token_lista.append([';',token, numeroLinha])
        # token=token.replace(";", " ")
    elif token == '+':
        token_lista.append(['operador_sum', token, numeroLinha])
    elif token == '-':
        token_lista.append(['operador_sum', token, numeroLinha])
    elif token == '*':
        token_lista.append(['operador_mul',token, numeroLinha])
    elif token == '/':
        token_lista.append(['operador_mul',token, numeroLinha])
    elif token == '&':
        token_lista.append(['op_logicos',token, numeroLinha])
    elif token == '|':
        token_lista.append(['op_logicos',token, numeroLinha])

def operadorSimbolos(caracteres, numeroLinha):   
    global token, token_lista,tam
    
    token=caracteres
    #print(f"token:{token}")
    if token == 'false' or token == 'true':
        if token_lista[-1][1] == 'true' or token_lista[-1][1] == 'false':
            return
    for i in range(len(token)):
        #print(f"token[i]:{token[i]}, i={i}, token={token}")
        if i == 1:
            vav=token.split(" ")  
            for indice in range(len(lista_variaveis)):
                if vav[0] == lista_variaveis[indice]:
                    token_lista.append(['nome_variavel', vav[0], numeroLinha])
                    token = '#'+token[1:]
                    if vav[0] != vav[-1]:
                        if vav[1] == '=' and vav[1] !='':
                            token_lista.append(['=', vav[1], numeroLinha])
                    # del vav[0]
                    return
        if token[i] == '+':
            token=token.replace("+", " ")
        elif token[i] == '-':
            token=token.replace("-", " ")
        elif token[i] == '*':
            token=token.replace("*", " ")
        elif token[i] == '/':
            token=token.replace("/", " ")
        elif token[i] == '&':
            token=token.replace("&", " ")
        elif token[i] == '|':
            token=token.replace("|", " ")

        elif token[i] == ',':
            token=token.replace(",", " ")
        elif token[i] == '(':
            token=token.replace("(", " ")
        elif token[i] == ')':
            token=token.replace(")", " ")
        elif token[i] == '{':
            token=token.replace("{", " ")
        elif token[i] == '}':
            token=token.replace("}", " ")
        elif token[i] == ':':
            token=token.replace(":", " ")
        elif token[i] == ';':
            token=token.replace(";", " ")
        # elif token[i] == '=':
        #     token=token.replace("=", " ")
        elif token[i] == '!':
            token=token.replace("!", " ")
        
        
        
    token=token.split(" ")  
    exclui=0
    for iter in range(len(token)):
        if len(token[exclui])==0:
            token.pop(exclui)
        else:
            exclui+=1   

    if len(token)!=0:
        tipo_dado(token, numeroLinha)
        
       
     
def char_string(caracteres, numeroLinha):
    global token, token_lista
    verificaAspas = True
    ret = len(token)
    token = caracteres
    for i in range(len(token)):
        if token[i] == '"' and token[-1] == '"' and verificaAspas:
            token_lista.append(['cadeia_print', token[1:-1], numeroLinha])
            verificaAspas = False
            ret = len(token)

        elif token[i] == "'" and token[i+2] == "'" and verificaAspas:
            token_lista.append(['operando', token[1], numeroLinha]) 
            verificaAspas = False
            ret = 3
            break
    return ret

def operandos(token, numeroLinha):
    global token_lista, lista_variaveis
    
    for k in range(len(token)):
        print('token[k] ',token[k])
        if "\'" in token[k]:
            continue
        elif token[k] == 'true' or token[k] == 'false':
            reservadas(token[k], numeroLinha)
            continue
        elif token[k] == '=':
            token_lista.append(['=', token[k], numeroLinha])
            
            
        elif token[k] in lista_variaveis and not token[k].isnumeric() and '.' not in token[k]:
            token_lista.append(['nome_variavel', token[k], numeroLinha])
            
        elif token[k] not in lista_variaveis and not token[k].isnumeric():
            print(f'\nLinha {numeroLinha} -> variavel {token[k]} nao declarada\n')
            exit(0)
    
    
        
def reservadas(token, numeroLinha):
    global token_lista

    if token[0] == "if":
        token_lista.append(['if', token[0], numeroLinha])
        del token[:]
    elif token[0] == 'else':
        token_lista.append(['else', token[0], numeroLinha])
        del token[:]
    elif token[0] == 'for':
        token_lista.append(['for', token[0], numeroLinha])
        del token[:]
    elif token[0] == 'while':
        token_lista.append(['while', token[0], numeroLinha])
        del token[:]
    elif token[0] == 'print':
        token_lista.append(['print', token[0], numeroLinha])
        del token[:]
    elif token[0] == 'scan':
        token_lista.append(['scan', token[0], numeroLinha])
        del token[:]
    elif token[0] == 'true':
        token_lista.append(['operando', token[0], numeroLinha])
        del token[:]
    elif token[0] == 'false':
        token_lista.append(['operando', token[0], numeroLinha])
        del token[:]
    elif token[0] == 'main':
        token_lista.append(['main', token[0], numeroLinha])
        del token[:]
    elif token == 'true':
        token_lista.append(['operando', token, numeroLinha])
        del token
        return
    elif token == 'false':
        token_lista.append(['operando', token, numeroLinha])
        del token
        return
    
    if len(token)!=0:
         operandos(token, numeroLinha)
        