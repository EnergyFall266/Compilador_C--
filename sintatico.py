

from xml.etree.ElementTree import ElementTree


pilha = []
pilhaOperandos = []
pilhaRotuloOperandos = []
global x
#variavel de controle (se permanecer em 0 não é possível empilhar ou reduzir com os simbolos analisados, entao ha um erro no codigo)
global reduzOrEmpilha 
#gramaticaItens = [qtd de itens a serem tirados da pilha, não terminal a ser colocado na pilha]
gramaticaItens = [[2, 'A'], [8, 'A'], [4, 'B'], [2, 'B'], [2, 'C'], [2, 'C'], [2, 'C'], [2, 'C'],
 [2, 'C'], [2, 'C'], [2, 'C'], [8, 'D'], [4, 'D'], [6, 'E'], [2, 'E'], [6, 'F'], [2, 'F'], [6, 'G'],
 [2, 'H'], [8, 'I'], [4, 'I'], [2, 'I'], [6, 'I'], [6, 'J'], [2, 'K'], [6, 'K'], [18, 'L'],
 [14, 'L'], [22, 'M'], [4, 'N'], [2, 'N'], [2, 'N'], [14, 'O'], [8, 'P'], [8, 'P'], [8, 'Q'], [2, 'R'], [2, 'R']]
 #lista de simbolos terminais da gramatica
listTerminais = ['main', '{', '}', 'tipo_dado', 'nome_variavel', '=', 'operando', 'operador_mul', 'operador_sum', 'op_relacional', 
'op_logicos', '!', 'if', '(', ')', 'else', 'for', ';', 'while', 'print', 'cadeia_print', 'scan', '$']
listaTipos = []

#listaToken = ['main', 'if']

def goTo():
    topo = pilha[-1]
    estado = pilha[-2]

    if(estado == 0 and topo == 'A'):
        pilha.append(19)
    elif(topo == 'B'):
        if(estado == 2):
            pilha.append(3)
        elif(estado == 5):
            pilha.append(6)
        elif(estado == 29):
            pilha.append(31)
        elif(estado == 45):
            pilha.append(47)
        elif(estado == 60):
            pilha.append(62)
        elif(estado == 67):
            pilha.append(69)
    elif(topo == 'C' and (estado == 2 or estado == 5 or estado == 29 or 
        estado == 45 or estado == 60 or estado == 67)):
        pilha.append(5)
    elif(topo == 'D' and (estado == 2 or estado == 5 or estado == 29 or 
        estado == 45 or estado == 60 or estado == 67)):
        pilha.append(7)
    elif(topo == 'E'):
        if(estado == 18 or estado == 23 or estado == 24 or estado == 54 or estado == 57 or estado == 61 or
         estado == 70 or estado == 76 or estado == 80):
            pilha.append(22)
        elif(estado == 28):
            pilha.append(30)
    elif(topo == 'F'):
        if(estado == 18):
            pilha.append(20)
        elif(estado == 24):
            pilha.append(84)
        elif(estado == 54 or estado == 23  or estado == 57 or estado == 70 or estado == 76):
            pilha.append(81)
        elif(estado == 61):
            pilha.append(63)
        elif(estado == 80):
            pilha.append(17)
    elif(topo == 'G'):
        if(estado == 23 or estado == 54 or estado == 70 or estado == 76):
            pilha.append(74)
        elif(estado == 57):
            pilha.append(59)
    elif(topo == 'H'):
        if(estado == 18 or estado == 23 or estado == 24 or estado == 28 or estado == 54 or estado == 57 or estado == 61 
         or estado == 70 or estado == 76 or estado == 80):
            pilha.append(86)
        elif(estado == 66):
            pilha.append(68)
    elif(topo == 'I'):
        if(estado == 23):
            pilha.append(25)
        elif(estado == 54):
            pilha.append(56)
        elif(estado == 70):
            pilha.append(72)
        elif(estado == 76):
            pilha.append(78)
    elif(topo == 'J'):
        if(estado == 2 or estado == 5 or estado == 29 or estado == 45 or estado == 60 or estado == 67):
            pilha.append(8)
        elif(estado == 53):
            pilha.append(77)
        elif(estado == 73):
            pilha.append(75)
    elif(topo == 'K' and estado == 35):
        pilha.append(37)
    elif(topo == 'L'):
        if(estado == 2 or estado == 5 or estado == 29 or estado == 45 or estado == 60 or estado == 67):
            pilha.append(10)
        elif(estado == 35):
            pilha.append(43)
    elif(topo == 'M' and 
     (estado == 2 or estado == 5 or estado == 29 or estado == 45 or estado == 60 or estado == 67)):
        pilha.append(9)
    elif(topo == 'N' and estado == 53):
        pilha.append(55)
    elif(topo == 'O' and 
     (estado == 2 or estado == 5 or estado == 29 or estado == 45 or estado == 60 or estado == 67)):
        pilha.append(12)
    elif(topo == 'P' and 
     (estado == 2 or estado == 5 or estado == 29 or estado == 45 or estado == 60 or estado == 67)):
        pilha.append(11)
    elif(topo == 'Q' and 
     (estado == 2 or estado == 5 or estado == 29 or estado == 45 or estado == 60 or estado == 67)):
        pilha.append(14)
    elif(topo == 'R' and (estado == 18 or estado == 23 or estado == 24 or estado == 28 or estado == 54 or estado == 57 or estado == 61 
         or estado == 70 or estado == 76 or estado == 80)):
        pilha.append(26)

def reducao(producao):
    global x
    global reduzOrEmpilha
    #retira o número de elementos da pilha, de acordo com a produção utilizada
    del pilha[len(pilha)-producao[0]:]
    #empilha o não terminal do lado esquerdo da produção
    pilha.append(producao[1])

    reduzOrEmpilha = 1
    x-= 1

    #desvio de acordo com os últimos dois elementos da pilha (estado e ultimo simbolo)
    goTo()

def bottom_up(listaToken, arq):
    global x
    global reduzOrEmpilha
    global listaTipos
    flagCondicaoIf = 0
    ultimoOperador = ""
    operador3end = ""
    tipo = ""
    ultimoLabel = 0

    #inicia a pilha com um 0
    pilha.append(0)
    
    x = 0
    while x < len(listaToken):
    #for token in listaToken:

        #pega a lista com token, conteudo e num linha
        tokenItem = listaToken[x]
        #pega só o token
        token = tokenItem[0]

        #analisa ultimo elemento na pilha
        topoPilha = pilha[-1]
        reduzOrEmpilha = 0
        print(pilha)
        print(token)

        x+= 1
        if(token == '$' and topoPilha == 19):
            #string aceita
            print(listaTipos)
            return 1
        elif(token == 'main' and topoPilha == 0):
            pilha.extend([token, 1])
            reduzOrEmpilha = 1
        elif(token == '{'):
            #verificar qual desses ifs é quando tem um token de if antes
            if(topoPilha == 1):
                pilha.extend([token, 2])
                reduzOrEmpilha = 1
            elif(topoPilha == 27):
                pilha.extend([token, 29])
                reduzOrEmpilha = 1
            elif(topoPilha == 35):
                pilha.extend([token, 45])
                reduzOrEmpilha = 1
            elif(topoPilha == 58):
                pilha.extend([token, 60])
                reduzOrEmpilha = 1
            elif(topoPilha == 65):
                pilha.extend([token, 67])
                reduzOrEmpilha = 1
        elif(token == '}'):
            if(topoPilha == 3):
                pilha.extend([token, 4])
                reduzOrEmpilha = 1
            elif(topoPilha == 31):
                pilha.extend([token, 33])
                arq.write("L"+str(ultimoLabel)+": ")
                ultimoLabel += 1
                reduzOrEmpilha = 1
            elif(topoPilha == 47):
                pilha.extend([token, 49])
                reduzOrEmpilha = 1
            elif(topoPilha == 62):
                pilha.extend([token, 64])
                reduzOrEmpilha = 1
            elif(topoPilha == 69):
                pilha.extend([token, 71])
                reduzOrEmpilha = 1
        elif(token == 'tipo_dado'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 
                or topoPilha == 45 or topoPilha == 60 or topoPilha == 67):
                pilha.extend([token, 13])
                ultimoTipo = tokenItem[1]
                reduzOrEmpilha = 1
            elif(topoPilha == 53):
                pilha.extend([token, 73])
                ultimoTipo = tokenItem[1]
                reduzOrEmpilha = 1
        elif(token == 'nome_variavel'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 
                or topoPilha == 45 or topoPilha == 60 or topoPilha == 67 or topoPilha == 73):
                #atribuicao
                pilha.extend([token, 16])
                ultimoNomeVar = tokenItem[1]
                reduzOrEmpilha = 1
            elif(topoPilha == 13):
                #declaracao sem atribuicao ou com
                pilha.extend([token, 15])
                ultimoNomeVar = tokenItem[1]
                reduzOrEmpilha = 1
            elif(topoPilha == 18 or topoPilha == 23 or topoPilha == 24 or topoPilha == 28 or topoPilha == 54 or topoPilha == 57 
            or topoPilha == 61 or topoPilha == 66 or topoPilha == 70 or topoPilha == 76 or topoPilha == 80):
                #declaracao sem atribuicao
                pilha.extend([token, 79])
                ultimoNomeVar = tokenItem[1]
                
                print(listaTipos)

                for elemento in listaTipos:
                    print(ultimoNomeVar)
                    if elemento[0] == ultimoNomeVar:
                        if elemento[1] == "int" and elemento[2] != '':
                            valor = int(elemento[2])
                            pilhaOperandos.append(valor)
                            pilhaRotuloOperandos.append(ultimoNomeVar)
                        elif elemento[1] == "float" and elemento[2] != '':
                            valor = float(elemento[2])
                            pilhaOperandos.append(valor)
                            pilhaRotuloOperandos.append(ultimoNomeVar)
                        elif elemento[1] == 'bool':
                            pilhaRotuloOperandos.append(ultimoNomeVar)
                            continue

                        else:
                            print('@@@@@@@@@@@@')
                            print(f'\n!!!ERRO!!!\nLinha {tokenItem[2]} -> Tipo da variável {elemento[0]} é incompatível    \n')
                            exit(0)
                print(pilhaOperandos)
                reduzOrEmpilha = 1
            elif(topoPilha == 53):
                # declaração operação
                pilha.extend([token, 83])
                ultimoNomeVar = tokenItem[1]
                reduzOrEmpilha = 1
            elif(topoPilha == 46):
                #scan
                pilha.extend([token, 48])
                ultimoNomeVar = tokenItem[1]
                reduzOrEmpilha = 1
            elif(topoPilha == 34):
                # print
                pilha.extend([token, 38])
                reduzOrEmpilha = 1
                ultimoPrint = tokenItem[1]
        elif(token == '='):
            if(topoPilha == 15):
                pilha.extend([token, 39])
                reduzOrEmpilha = 1
                linha = tokenItem[2]
            elif(topoPilha == 16 or topoPilha == 83):
                variavelAlterarValor = ultimoNomeVar
                pilha.extend([token, 18])
                linha = tokenItem[2]
                reduzOrEmpilha = 1
        elif(token == 'operando'):
            if(topoPilha == 24 or topoPilha == 23 or topoPilha == 18 or topoPilha == 28 or topoPilha == 54 
            or topoPilha == 57 or topoPilha == 61 or topoPilha == 70 or topoPilha == 76 or topoPilha == 80):
                pilha.extend([token, 85])
                ultimoOperando = tokenItem[1]
                if tokenItem[1].isnumeric():
                    tipoOperando = 'int'
                elif ('.' in tokenItem[1]):
                    tipoOperando = 'float'  
                elif tokenItem[1] == 'false' or tokenItem[1] == 'true':
                    tipoOperando = 'bool'      
                
                reduzOrEmpilha = 1
            elif(topoPilha == 39):
                print(tokenItem)
                pilha.extend([token, 41])
                ultimoOperando = tokenItem[1]
                if tokenItem[1].isnumeric():
                    tipoOperando = 'int'
                elif ('.' in tokenItem[1]):
                    tipoOperando = 'float'
                elif tokenItem[1] == 'false' or tokenItem[1] == 'true':
                    tipoOperando = 'bool'
                reduzOrEmpilha = 1

        elif(token == 'operador_mul'):
            if(topoPilha == 26):
                pilha.extend([token, 28])
                reduzOrEmpilha = 1
                linha = tokenItem[2]
                ultimoOperador = tokenItem[1]
        elif(token == 'operador_sum'):
            if(topoPilha == 22):               
                pilha.extend([token, 24])
                reduzOrEmpilha = 1
                linha = tokenItem[2]
                ultimoOperador = tokenItem[1]
        elif(token == 'op_relacional'):
            if(topoPilha == 81):
                pilha.extend([token, 80])
                reduzOrEmpilha = 1
                linha = tokenItem[2]
                ultimoOperadorRelacional = tokenItem[1]
        elif(token == 'op_logicos'):
            if(topoPilha == 74):
                pilha.extend([token, 76])
                reduzOrEmpilha = 1
                linha = tokenItem[2]
            elif(topoPilha == 68):
                pilha.extend([token, 70])
                reduzOrEmpilha = 1
        elif(token == '!'):
            if(topoPilha == 23 or topoPilha == 54 or topoPilha == 70 or topoPilha == 76):
                pilha.extend([token, 66])
                reduzOrEmpilha = 1
        elif(token == 'if'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 or topoPilha == 35 
            or topoPilha == 45 or topoPilha == 60 or topoPilha == 67):
                pilha.extend([token, 21])
                reduzOrEmpilha = 1
                arq.write("L"+str(ultimoLabel)+": IF ")
                ultimoLabel +=1
                flagCondicaoIf = 1
        elif(token == '('):
            if(topoPilha == 21):
                pilha.extend([token, 23])
                reduzOrEmpilha = 1
            elif(topoPilha == 32):
                pilha.extend([token, 34])
                reduzOrEmpilha = 1
            elif(topoPilha == 44):
                pilha.extend([token, 46])
                reduzOrEmpilha = 1
            elif(topoPilha == 51):
                pilha.extend([token, 53])
                reduzOrEmpilha = 1
            elif(topoPilha == 52):
                pilha.extend([token, 54])
                reduzOrEmpilha = 1
        elif(token == ')'):
            if(topoPilha == 25):
                pilha.extend([token, 27])
                reduzOrEmpilha = 1
            elif(topoPilha == 36):
                pilha.extend([token, 40])
                reduzOrEmpilha = 1
            elif(topoPilha == 38):
                pilha.extend([token, 42])
                reduzOrEmpilha = 1
            elif(topoPilha == 48):
                pilha.extend([token, 50])
                reduzOrEmpilha = 1
            elif(topoPilha == 56):
                pilha.extend([token, 58])
                reduzOrEmpilha = 1
            elif(topoPilha == 63):
                pilha.extend([token, 65])
                reduzOrEmpilha = 1
        elif(token == 'else'):
            if(topoPilha == 33):
                pilha.extend([token, 35])
                reduzOrEmpilha = 1
        elif(token == 'for'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 or topoPilha == 45
            or topoPilha == 60 or topoPilha == 67):
                pilha.extend([token, 51])
                reduzOrEmpilha = 1
                #3 endereços
                #criar um label
                arq.write("L"+str(ultimoLabel)+" IF ")
                ultimoLabel +=1
        elif(token == ';'):
            if(topoPilha == 55):
                pilha.extend([token, 57])
                reduzOrEmpilha = 1
            elif(topoPilha == 59):
                pilha.extend([token, 61])
                reduzOrEmpilha = 1
        elif(token == 'while'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 or topoPilha == 45
            or topoPilha == 60 or topoPilha == 67):
                pilha.extend([token, 52])
                reduzOrEmpilha = 1
                #3 endereços
                arq.write("L"+str(ultimoLabel)+": IF ")
                ultimoLabel +=1
        elif(token == 'print'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 or topoPilha == 45
            or topoPilha == 60 or topoPilha == 67):
                pilha.extend([token, 32])
                reduzOrEmpilha = 1
        elif(token == 'cadeia_print'):
            if(topoPilha == 34):
                pilha.extend([token, 36])
                reduzOrEmpilha = 1
                ultimoPrint = tokenItem[1]
        elif(token == 'scan'):
            if(topoPilha == 2 or topoPilha == 5 or topoPilha == 29 or topoPilha == 45
            or topoPilha == 60 or topoPilha == 67):
                pilha.extend([token, 44])
                reduzOrEmpilha = 1
        if(token in listTerminais and reduzOrEmpilha == 0):
            #se entrar nesse if, significa que nenhum simbolo foi empilhado e será feita a análise de reduções se for um simbolo terminal
            if(topoPilha == 4):
                reducao(gramaticaItens[1])
            elif(topoPilha == 5 and token != 'tipo_dado' and token != 'nome_variavel'):
                reducao(gramaticaItens[3])
            elif(topoPilha == 6):
                reducao(gramaticaItens[2])
            elif(topoPilha == 7):
                reducao(gramaticaItens[4])
            elif(topoPilha == 8):
                reducao(gramaticaItens[5])
            elif(topoPilha == 9):
                reducao(gramaticaItens[7])
            elif(topoPilha == 10):
                reducao(gramaticaItens[6])
            elif(topoPilha == 11):
                reducao(gramaticaItens[9])
            elif(topoPilha == 12):
                reducao(gramaticaItens[8])
            elif(topoPilha == 14):
                reducao(gramaticaItens[10])
            elif(topoPilha == 15 and token != '='):
                #declaracao variavel
                listaTipos.append([ultimoNomeVar, ultimoTipo, ""])
                reducao(gramaticaItens[12])
            elif(topoPilha == 17):
                #operacao relacional
                valor2 = pilhaOperandos.pop()
                nome2  = pilhaRotuloOperandos.pop()
                if len(pilhaOperandos) != 0:
                    
                    print(pilhaOperandos)
                    print(pilhaRotuloOperandos)

                    valor1 = pilhaOperandos.pop()
                    nome1  = pilhaRotuloOperandos.pop()

                    verificaTipos(type(valor1), type(valor2), linha)
                    if(ultimoOperadorRelacional == "=="):
                        operador3end = "!="
                    elif(ultimoOperadorRelacional == "!="):
                        operador3end = "=="
                    elif(ultimoOperadorRelacional == "<" or ultimoOperadorRelacional == "<="):
                        operador3end = ">"
                    elif(ultimoOperadorRelacional == ">" or ultimoOperadorRelacional == ">="):
                        operador3end = "<"

                    #3 endereços
                    if(nome1 == "operando"):
                        op1 = str(valor1)
                    else:
                        op1 = nome1
                    if(nome2 == "operando"):
                        op2 = str(valor2)
                    else:
                        op2 = nome2
                    arq.write(op1+" "+operador3end+" "+op2+" goto L"+str(ultimoLabel)+"\n")
                else:
                    verificaTiposLogicosUnico(valor2, linha)

                reducao(gramaticaItens[17])
            elif(topoPilha == 19):
                reducao(gramaticaItens[0])
            elif(topoPilha == 20):
                #atribuicao 
                print('atribuição ',ultimoNomeVar)
                print('operando ',ultimoOperando)
                print('linha ' ,linha)
                verificaTipos(type(ultimoNomeVar), type(ultimoOperando),linha)
                #3 endereços
                if(flagCondicaoIf == 0):
                    arq.write(ultimoNomeVar+" = "+ultimoOperando+"\n")
                flagCondicaoIf = 0
                reducao(gramaticaItens[23])
            elif(topoPilha == 22 and token != 'operador_sum'):
                reducao(gramaticaItens[16])
            elif(topoPilha == 26 and token != 'operador_mul'):
                reducao(gramaticaItens[14])
            elif(topoPilha == 30):
                #multiplicacao
                valor2 = pilhaOperandos.pop()
                nome2 = pilhaRotuloOperandos.pop()
                valor1 = pilhaOperandos.pop()
                nome1 = pilhaRotuloOperandos.pop()


                verificaTipos(type(valor1), type(valor2), linha)
                for elemento in listaTipos:
                    if elemento[0] == variavelAlterarValor:
                        elemento[2] = valor1 * valor2
                
                #3 endereços
                if(nome1 == "operando"):
                        op1 = str(valor1)
                else:
                    op1 = nome1
                if(nome2 == "operando"):
                    op2 = str(valor2)
                else:
                    op2 = nome2

                if(ultimoOperador == "*"):
                    arq.write(variavelAlterarValor+" = "+op1+" * "+op2+"\n")
                elif(ultimoOperador == "/"):
                    arq.write(variavelAlterarValor+" = "+str(valor1)+" / "+str(valor2)+"\n")
                flagCondicaoIf = 1

                reducao(gramaticaItens[13])
            elif(topoPilha == 33 and token != 'else'):
                #if sem else
                reducao(gramaticaItens[27])
            elif(topoPilha == 37):
                reducao(gramaticaItens[26])
            elif(topoPilha == 40):
                #print cadeia print
                reducao(gramaticaItens[34])
                #3 enderecos
                arq.write("PRINT \""+ultimoPrint+"\"\n")
            elif(topoPilha == 41):
                #declaracao da variavel com atribuicao
                if(tipoOperando == "str"):
                    tipoOperando = "char"
                if(ultimoTipo == tipoOperando):
                    listaTipos.append([ultimoNomeVar, ultimoTipo, ultimoOperando])
                    #3 endereços
                    arq.write(ultimoNomeVar+" = "+ultimoOperando+"\n")
                    reducao(gramaticaItens[11])
                else:
                    print('###################')
                    print(f'\n!!!ERRO!!!\nLinha {tokenItem[2]-1} -> Tipo da variável {ultimoNomeVar} é incompatível    \n')
                    exit(0)
            elif(topoPilha == 42):
                #print nome_variavel
                reducao(gramaticaItens[33])
                #3 enderecos
                arq.write("PRINT "+ultimoPrint+"\n")
            elif(topoPilha == 43):
                reducao(gramaticaItens[24])
            elif(topoPilha == 49):
                reducao(gramaticaItens[25])
            elif(topoPilha == 50):
                #scan
                reducao(gramaticaItens[35])
                #3 endereços
                arq.write("SCAN "+ultimoNomeVar+'\n')
            elif(topoPilha == 64):
                arq.write("L"+str(ultimoLabel)+": ")
                ultimoLabel += 1
                reducao(gramaticaItens[32])
            elif(topoPilha == 68 and token != 'op_logicos'):
                #not
                for elemento in listaTipos:
                    if(elemento[0] == ultimoNomeVar):
                        if(elemento[1] == "bool"):
                            reducao(gramaticaItens[20])
                            #3 enderecos
                            #arq.write("! "+ultimoNomeVar+"\n")
                        else:
                            print(f'\n!!!ERRO!!!\nLinha {tokenItem[2]} -> Tipo da variável {elemento[0]} é incompatível    \n')
                            exit(0)
            elif(topoPilha == 71):
                reducao(gramaticaItens[28])
            elif(topoPilha == 72):
                #operacao logica not (dois operandos)
                valor2 = pilhaOperandos.pop()
                valor1 = pilhaOperandos.pop()

                verificaTiposLogicos(type(valor1), type(valor2), linha)
                reducao(gramaticaItens[19])

            elif(topoPilha == 74 and token != 'op_logicos'):
                reducao(gramaticaItens[21])
            elif(topoPilha == 75):
                #declaracao variavel com atribuição de operação
                reducao(gramaticaItens[29])
            elif(topoPilha == 77):
                reducao(gramaticaItens[30])
            elif(topoPilha == 78):
                #operacao logica (dois operandos)
                valor2 = pilhaOperandos.pop()
                valor1 = pilhaOperandos.pop()

                verificaTiposLogicos(type(valor1), type(valor2), linha)
                reducao(gramaticaItens[22])
            elif(topoPilha == 79):                
                reducao(gramaticaItens[18])
            elif(topoPilha == 82):
                reducao(gramaticaItens[21])
            elif(topoPilha == 83 and token != '='):
                reducao(gramaticaItens[31])
            elif(topoPilha == 84):
                #soma
                valor2 = pilhaOperandos.pop()
                valor1 = pilhaOperandos.pop()
                verificaTipos(type(valor1), type(valor2), linha)
                for elemento in listaTipos:
                    if elemento[0] == variavelAlterarValor:
                        elemento[2] = valor1 + valor2
                #3 endereços
                if(ultimoOperador == "+"):
                    arq.write(variavelAlterarValor+" = "+str(valor1)+" + "+str(valor2)+"\n")
                elif(ultimoOperador == "-"):
                    arq.write(variavelAlterarValor+" = "+str(valor1)+" - "+str(valor2)+"\n")
                flagCondicaoIf = 1

                reducao(gramaticaItens[15])
            elif(topoPilha == 85):

                '''print(pilhaOperandos)
                valorX = pilhaOperandos.pop(0)
                valorY = pilhaOperandos.pop(0)

                print("VALOR1", valorY)
                print("VALOR2", valorX)'''

                if ultimoOperando.isnumeric():
                    valor = int(ultimoOperando)
                    pilhaOperandos.append(valor)
                    pilhaRotuloOperandos.append("operando")
                elif '.' in ultimoOperando: 
                    valor = float(ultimoOperando)
                    pilhaOperandos.append(valor)
                    pilhaRotuloOperandos.append("operando")
                elif ultimoOperando == 'false' or ultimoOperando == 'true':
                    valor1 = True
                    pilhaRotuloOperandos.append("operando")
                valor1 = valor
                # if len(pilhaOperandos) != 0:
                #     valor1 = pilhaOperandos.pop(0)
                print(pilhaOperandos)
                print("VALOR1", valor1)
                print("VALOR2", valor2)
                print(type(valor1))
                print(type(valor2))

                print("Primeiro verifica tipos")
                verificaTipos(type(valor1),type(valor2),linha)

                '''for tp in listaTipos:
                    if tp[0] == ultimoNomeVar:
                        valor2 = tp[1]
                        valor1 = tp[2]

                if type(valor1) is int:
                    tipo = 'int'
                elif type(valor1) is float:
                    tipo = 'float'
                elif type(valor1) is bool:
                    tipo = 'bool'
                
                verificaTipos(tipo,valor2,linha)
                print(pilhaOperandos)'''
                reducao(gramaticaItens[36])
            elif(topoPilha == 86):
                reducao(gramaticaItens[37])
        if(reduzOrEmpilha == 0):
            #erro
            print(f'\n!!!ERRO!!!\nLinha {tokenItem[2]} -> Termo não esperado {tokenItem[1]}     \n')
            exit(0)

            return 0

def verificaTipos(a, b, linha):
    
    if(a != b):
        print('a',a)
        print(b)
        print(f'\n!!!ERRO!!!\nLinha {linha} -> nao é possivel realizar operacao, tipos diferentes     \n')
        exit(0)

def verificaTiposLogicos(a, b, linha):
    if(a != 'bool' or b != 'bool'):
        print(f'\n!!!ERRO!!!\nLinha {linha} -> nao é possivel realizar operacao, tipos diferentes     \n')
        exit(0)
def verificaTiposLogicosUnico(a,linha):
    if a != 'bool':
        print(f'\n!!!ERRO!!!\nLinha {linha} -> nao é possivel realizar operacao, tipos diferentes     \n')
        exit(0)