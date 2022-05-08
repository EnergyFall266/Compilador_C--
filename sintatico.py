pilha = []
gramaticaItens = []

#listaToken = ['main', 'if']

def bottom_up(listaToken):
    pilha.append(0)

    for token in listaToken:
        topoPilha = pilha[-1]

        print(token)
        if(token == 'main'):
            if(topoPilha == 0):
                pilha.extend([token, 1])
        elif(token == '{'):
            if(topoPilha == 1):
                pilha.extend([token, 2])
        elif(token == '}'):
            if(topoPilha == 3):
                pilha.extend([token, 4])
        elif(token == 'tipo_dado'):
            if(topoPilha == 2):
                pilha.extend([token, 13])
        elif(token == 'nome_variavel'):
            if(topoPilha == 2):
                pilha.extend([token, 16])
        elif(token == '='):
            if(topoPilha == 15):
                pilha.extend([token, 39])
        elif(token == 'operando'):
            if(topoPilha == 18):
                pilha.extend([token, 26])
        elif(token == 'operador_mul'):
            if(topoPilha == 26):
                pilha.extend([token, 28])
        elif(token == 'operador_sum'):
            if(topoPilha == 22):
                pilha.extend([token, 24])
        elif(token == 'op_relacional'):
            if(topoPilha == 81):
                pilha.extend([token, 80])
        elif(token == 'op_logicos'):
            if(topoPilha == 74):
                pilha.extend([token, 76])
        elif(token == '!'):
            if(topoPilha == 23):
                pilha.extend([token, 66])
        elif(token == 'if'):
            if(topoPilha == 2):
                pilha.extend([token, 21])
        elif(token == '('):
            if(topoPilha == 21):
                pilha.extend([token, 23])
        elif(token == ')'):
            if(topoPilha == 25):
                pilha.extend([token, 27])
        elif(token == 'else'):
            if(topoPilha == 33):
                pilha.extend([token, 35])
        elif(token == 'for'):
            if(topoPilha == 2):
                pilha.extend([token, 51])
        elif(token == ';'):
            if(topoPilha == 55):
                pilha.extend([token, 57])
        
    print(pilha)

