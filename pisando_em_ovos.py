dictConfig = {}
matriz = []
listEspaços = [1, 2, 3, 4, 5]


def validarEntrada(texto, lista):
    res = int(input(texto))
    while res not in lista:
        res = int(input(f'[ERRO DE ENTRADA]. {texto}'))
    return res


def criarMatriz():
    global matriz
    matriz.clear()
    for linha in range(5):
        matriz.append([])
        for coluna in range(5):
            matriz[linha].append('A')


def matrizInicial():
    print(f''' 
                0 1 2 3 4 5 
                1 {matriz[0][0]} {matriz[0][1]} {matriz[0][2]} {matriz[0][3]} {matriz[0][4]}  
                2 {matriz[1][0]} {matriz[1][1]} {matriz[1][2]} {matriz[1][3]} {matriz[1][4]} 
                3 {matriz[2][0]} {matriz[2][1]} {matriz[2][2]} {matriz[2][3]} {matriz[2][4]} 
                4 {matriz[3][0]} {matriz[3][1]} {matriz[3][2]} {matriz[3][3]} {matriz[3][4]} 
                5 {matriz[4][0]} {matriz[4][1]} {matriz[4][2]} {matriz[4][3]} {matriz[4][4]} 
                            ''')


def plantarArmadilha():
    global matriz
    print(f'Jogador {dictConfig["armador"]} você pode esconder até 3 ovos podres por linha do terreno.')
    criarMatriz()
    matrizInicial()
    for c in range(1, 6):
        for i in range(1, 4):
            perg = validarEntrada(f'Em qual coluna da linha {c} você quer esconder ovos podres? [1 a 5]', [1, 2, 3, 4, 5])
            matriz[c - 1][perg - 1] = 'O'
            if i != 3:
                continuar = validarEntrada('Você quer continuar na mesma linha? 1-SIM 2-NÃO ', [1, 2])
                if continuar == 2:
                    break
                    
    matrizInicial()
    perg = validarEntrada('Redefinir campo? [1]- SIM  [2]- NÃO ', [1, 2])
    if perg == 1:
        plantarArmadilha()
        

def posicaoValida(escolha):
    global listEspaços
    listEspaços.clear()
    if escolha == 1:
        listEspaços = [1, 2]
    elif escolha == 5:
        listEspaços = [5, 4]
    else:
        listEspaços.append(escolha-1)
        listEspaços.append(escolha)
        listEspaços.append(escolha+1)
    return listEspaços


def movimentoAndarilho():
    global listEspaços
    
    cont_andarilho = cont_armador = 0

    for c in range(0, 5):
        if c == 0:
            print(f'São válidos os espaços {listEspaços}')
            escolha = validarEntrada('Escolha sabiamente um dos espaços válidos: ', listEspaços)
            if matriz[c][escolha - 1] == 'O':
                print('Eca! Você pisou em um ovo podre e perdeu')
                cont_armador += 1
                dictConfig['ponto_armador'] = cont_armador
                break
            posicaoValida(escolha)

        print(f'São válidos os espaços {listEspaços}')
        escolha = validarEntrada('Escolha sabiamente um dos espaços válidos: ', listEspaços)
        if matriz[c][escolha - 1] == 'O':
            print('Eca! Você pisou em um ovo podre e perdeu')
            break
        posicaoValida(escolha)
        if c == 4:
            print('Você atravessou o terreno sem cair em nenhuma armadilha. Parabéns!!!')
            cont_andarilho += 1
            dictConfig['ponto_andarilho'] = cont_andarilho
            break


def menu():
    print('''
    Opções:
    1 - Definir Armador
    2 - Plantar Armadilhas
    3 - Iniciar com Andarilho
    4 - Mostrar o placar
    0 - Finalizar o Jogo''')
    perg = validarEntrada('Escolha uma opção: ', [0, 1, 2, 3, 4,])
    match perg:
        case 0:
            return False
        case 1:
            escolha = validarEntrada('Qual jogador plantará as armadilhas? [1 ou 2] ', [1, 2])
            if escolha == 1:
                dictConfig['armador'] = 1
                dictConfig['andarilho'] = 2
                print(f'O armador é o jogador: {dictConfig["armador"]}')
                print(f'O andarilho é o jogador: {dictConfig["andarilho"]}')     
                
            elif escolha == 2:
                dictConfig['armador'] = 2
                dictConfig['andarilho'] = 1
                print(f'O armador é o jogador: {dictConfig["armador"]}')
                print(f'O andarilho é o jogador: {dictConfig["andarilho"]}')       
        case 2:
            if 'armador' and 'andarilho' not in dictConfig:
                print('Primeiro você deve definir quem vai montar as armadilhas! Digite 1 para escolher quem será o armador.')
                menu()
            else:
                plantarArmadilha()
        case 3:
            for c in range(0, 101):
                print('=' * c)
            movimentoAndarilho()
        case 4:
            if 'armador' and 'andarilho' not in dictConfig:
                print('Primeiro você deve definir quem vai montar as armadilhas! Digite 1 para escolher quem será o armador.')
                menu()
            print(f'Pontuação do armador: {dictConfig["armador"]}')
            print(f'Pontuação do armador: {dictConfig["andarilho"]}')
    return True


rodar = True
while rodar:
    rodar = menu()
    