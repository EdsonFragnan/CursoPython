def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    x = n % (m + 1)
    is_computer_turn = True
    if x != 0:
        is_computer_turn = True
        print("O computador começa!")
    if x == 0:
        is_computer_turn = False
        print("Você começa!")

    while n > 0:

        if is_computer_turn:
            jogada = computador_escolhe_jogada(n, m)
            is_computer_turn = False
            print("Computador retirou", jogada, "peças.")
        else:
            jogada = usuario_escolhe_jogada(n, m)

            is_computer_turn = True
            print("Você retirou", jogada, "peças.")

        n = n - jogada

        print("Restam apenas", n, "peças em jogo.\n")

    if is_computer_turn:
        print("Você ganhou!")
        return 1
    else:
        print("O computador ganhou!")
        return 0

def usuario_escolhe_jogada(n, m):

    print('Sua vez!\n')
    jogada = 0

    while jogada == 0:

        jogada = int(input('Quantas peças irá tirar? '))
        if jogada > n or jogada < 1 or jogada > m:
            print('Oops! Jogada inválida! Tente de novo.')
            jogada = 0

    return jogada

def computador_escolhe_jogada(n, m):
    print('Vez do computador!')
    if n <= m:
        return n
    else:
        quantia = n % (m+1)
        if quantia > 0:
            return quantia
        return m

def campeonato():
    usuario = 0
    computador = 0
    for _ in range(3):
        vencedor = partida()
        if vencedor == 1:
            usuario = usuario + 1
        else:
            computador = computador + 1

    print('Placar: Você', usuario, 'x', computador, 'Computador')


tipo_jogo = 0
while tipo_jogo == 0:
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - Para jogar uma partida isolada")
    print("2 - Para jogar um campeonato")

    tipo_jogo = int(input("Sua opção: "))
    if tipo_jogo == 1:
        print("Voce escolheu partida isolada!")
        partida()
        break
    elif tipo_jogo == 2:
        print("Voce escolheu um campeonato!")
        campeonato()
        break
    else:
        print("Opção inválida!")
        tipo_jogo = 0
