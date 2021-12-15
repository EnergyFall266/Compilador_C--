#colocar as variaveis q vem dps do tipo dado
# fazer split dentro do 
# token = token.split(" ")
# vai ser recebido uma string que vai começar com letra
# passo1: identificar se tem operadores(+,*)
# passo2: dar replace nestes operadores e simbolos por espaço
# passo3: dar split nos espaços
# passo4: fazer verificação nos if


from os import replace

def tipo_dado():
    global token, token_lista, lista_variaveis
     
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
    # print(token)
    # print(token_lista)
    # print(lista_variaveis)
    reservadas()

def operando_simbolos():   
    global token, token_lista
    
    for i in range(len(token)-1):
        print(token)
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
            token_lista.append(['abre_parenteses',token[i]])
            token=token.replace("(", " ")
        elif token[i] == ')':
            token_lista.append(['fecha_parenteses', token[i]])
            token=token.replace(")", "")
        elif token[i] == '{':
            token_lista.append(['abre_chaves',token[i]])
            token=token.replace("{", " ")
        elif token[i] == '}':
            token_lista.append(['fecha_chaves',token[i]])
            token=token.replace("}", "")
        elif token[i] == ':':
            token_lista.append(['dois_pontos',token[i]])
            token=token.replace(":", " ")
        elif token[i] == ';':
            token_lista.append(['ponto_virgula',token[i]])
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
    
    # print(token)
    token=token.split(" ")  
    # print(token)
    # print(len(token))
    exclui=0
    for iter in range(len(token)):
        # print(exclui)
        if len(token[exclui])==0:
            token.pop(exclui)
        else:
            exclui+=1    
    # print(token)
    # print(token_lista)
    
    tipo_dado()
    
    
def char_string():
    global token, token_lista
    for i in range(len(token)):    
        if token[i][0] == '"' and token[i][-1] == '"':
            token_lista.append(['cadeia_print', token[i]])

        elif token[i][0] == "'" and token[i][-1] == "'":
           token_lista.append(['char', token[i]]) 
        elif token[i] == 'true':
            token_lista.append(['booleano', token[i]])
        elif token[i] == 'false':
            token_lista.append(['booleano', token[i]])
    # print(token_lista)

def operandos():
    global token, token_lista, lista_variaveis
    for k in range(len(token)):
        for indice in range(len(lista_variaveis)):
            if token[k] == lista_variaveis[indice]:
                token_lista.append(['operando', token[k]])
                
    # print(token)
    # print(token_lista)

    char_string()
def reservadas():
    global token, token_lista
    if token[0] == 'if':
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
    
    # print(token)
    # print(token_lista)
    operandos()

def numeros():

    if token[1:].isnumeric():
        token_lista.append(['inteiro', token])

    elif float(token):
        token_lista.append(['real', token])



if __name__ == '__main__':
    token = "if==('nota'+nota2\")"
    token_lista=[]
    lista_variaveis = ['nota2', 'nota']
    operando_simbolos()
    "sd s"