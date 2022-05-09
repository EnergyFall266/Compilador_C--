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
            elif(topoPilha == 27):
                pilha.extend([token, 29])
            elif(topoPilha == 35):
                pilha.extend([token, 45])
            elif(topoPilha == 58):
                pilha.extend([token, 60])
            elif(topoPilha == 65):
                pilha.extend([token, 67])
        elif(token == '}'):
            if(topoPilha == 3):
                pilha.extend([token, 4])
            elif(topoPilha == 31):
                pilha.extend([token, 33])
            elif(topoPilha == 47):
                pilha.extend([token, 49])
            elif(topoPilha == 62):
                pilha.extend([token, 64])
            elif(topoPilha == 69):
                pilha.extend([token, 71])
        elif(token == 'tipo_dado'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 
                or topoPilha == 45 or topoPilha == 60 or topoPilha == 67):
                pilha.extend([token, 13])
            elif(topoPilha == 53):
                pilha.extend([token, 73])
        elif(token == 'nome_variavel'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 
                or topoPilha == 45 or topoPilha == 60 or topoPilha == 67 or topoPilha == 73):
                pilha.extend([token, 16])
            elif(topoPilha == 13):
                pilha.extend([token, 15])
            elif(topoPilha == 53):
                pilha.extend([token, 83])
            elif(topoPilha == 54 or topoPilha == 76):
                pilha.extend([token, 79])
        elif(token == '='):
            if(topoPilha == 15):
                pilha.extend([token, 39])
            elif(topoPilha == 16 or topoPilha == 83):
                pilha.extend([token, 18])
        elif(token == 'operando'):
            if(topoPilha == 18 or topoPilha == 54 or topoPilha == 57 or topoPilha == 61
            or topoPilha == 70 or topoPilha == 76 or topoPilha == 80):
                pilha.extend([token, 26])
            elif(topoPilha == 34):
                pilha.extend([token, 38])
            elif(topoPilha == 39):
                pilha.extend([token, 41])
            elif(topoPilha == 46):
                pilha.extend([token, 48])
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
            if(topoPilha == 23 or topoPilha == 54 or topoPilha == 70 or topoPilha == 76):
                pilha.extend([token, 66])
        elif(token == 'if'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 or topoPilha == 35 
            or topoPilha == 45 or topoPilha == 60 or topoPilha == 67):
                pilha.extend([token, 21])
        elif(token == '('):
            if(topoPilha == 21):
                pilha.extend([token, 23])
            elif(topoPilha == 32):
                pilha.extend([token, 34])
            elif(topoPilha == 44):
                pilha.extend([token, 46])
            elif(topoPilha == 51):
                pilha.extend([token, 53])
            elif(topoPilha == 52):
                pilha.extend([token, 54])
        elif(token == ')'):
            if(topoPilha == 25):
                pilha.extend([token, 27])
            elif(topoPilha == 36):
                pilha.extend([token, 40])
            elif(topoPilha == 38):
                pilha.extend([token, 42])
            elif(topoPilha == 48):
                pilha.extend([token, 50])
            elif(topoPilha == 56):
                pilha.extend([token, 58])
            elif(topoPilha == 63):
                pilha.extend([token, 65])
        elif(token == 'else'):
            if(topoPilha == 33):
                pilha.extend([token, 35])
        elif(token == 'for'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 or topoPilha == 45
            or topoPilha == 60 or topoPilha == 67):
                pilha.extend([token, 51])
        elif(token == ';'):
            if(topoPilha == 55):
                pilha.extend([token, 57])
            elif(topoPilha == 59):
                pilha.extend([token, 61])
        elif(token == 'while'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 or topoPilha == 45
            or topoPilha == 60 or topoPilha == 67):
                pilha.extend([token, 52])
        elif(token == 'print'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 or topoPilha == 45
            or topoPilha == 60 or topoPilha == 67):
                pilha.extend([token, 32])
        elif(token == 'cadeia_print'):
            if(topoPilha == 34):
                pilha.extend([token, 36])
        elif(token == 'scan'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 or topoPilha == 45
            or topoPilha == 60 or topoPilha == 67):
                pilha.extend([token, 44])
    print(pilha)

