from random import randint #importando a biblioteca que vai randomizar a escolha do pc
from time import sleep #importando uma biblioteca apenas para dar mais realidade ao jogo com um timer

#estabelecendo o valor inicial das vitorias para contagem das rodadas
vitoriasMaquina = vitoriasJogador = 0 
#opcoes de jogadas para o programa randomizar e o jogador escolher
opcoesDeJogadas = ('PEDRA', 'PAPEL', 'TESOURA')
jogadaComputador = randint(0, 2)

print('-=' * 13)
print('\033[1:31:40mπ π βοΈ  JOKENPO\033[m π π βοΈ ')
print('-=' * 13)
sleep(1)
print()
resp = 's'
while resp == 's':
    nRodadas = int(input('Quantas rodadas gostaria de ter? '))
    sleep(1)
    print()
    print(f'Sua partida serΓ‘ uma melhor de {nRodadas}!')
    print()
    for g in range(nRodadas):
        jogadaDoJogador = int(input('DIGITE UM VALOR DENTRE ESSES PARA JOGAR:\n [0] PEDRA\n [1] PAPEL\n [2] TESOURA\n'))
        while jogadaDoJogador not in range(0, 3):
            jogadaDoJogador = int(input('Jogada invΓ‘lida! DIGITE UM VALOR DENTRE ESSES PARA JOGAR:\n [0] PEDRA\n [1] PAPEL\n [2] TESOURA\n'))
        else:
            pass
        print()
        print('JO π')
        sleep(1)
        print('KEN π')
        sleep(1)
        print('PO βοΈ')
        print()
        sleep(0.5)
        print('-=' * 14)
        print('O computador jogou {}!'.format(opcoesDeJogadas[jogadaComputador]))
        print('O jogador jogou {}!'.format(opcoesDeJogadas[jogadaDoJogador])) 
        print('-=' * 14)     
        print()
        if jogadaComputador == 0: #computador jogou PEDRA
            if jogadaDoJogador == 0:
                vitoriasMaquina += 1
                vitoriasJogador += 1
                print(f'EMPATOU!\n π₯οΈ  Computador {vitoriasMaquina} x {vitoriasJogador} Jogador π§')
            elif jogadaDoJogador == 1:
                vitoriasJogador += 1
                print(f'JOGADOR VENCEU!\n π₯οΈ  Computador {vitoriasMaquina} x {vitoriasJogador} Jogador π§')
            elif jogadaDoJogador == 2:
                vitoriasMaquina += 1
                print(f'COMPUTADOR VENCEU!\n π₯οΈ  Computador {vitoriasMaquina} x {vitoriasJogador} Jogador π§')
            else:   
                print('JOGADA INVΓLIDA') 
        elif jogadaComputador == 1: #computador jogou PAPEL
            if jogadaDoJogador == 0:
                vitoriasMaquina += 1
                print(f'COMPUTADOR VENCEU!\n π₯οΈ  Computador {vitoriasMaquina} x {vitoriasJogador} Jogador π§')
            elif jogadaDoJogador == 1:
                vitoriasMaquina += 1
                vitoriasJogador += 1
                print(f'EMPATOU!\n π₯οΈ  Computador {vitoriasMaquina} x {vitoriasJogador} Jogador π§')
            elif jogadaDoJogador == 2:
                vitoriasJogador += 1
                print(f'JOGADOR VENCEU!\n π₯οΈ  Computador {vitoriasMaquina} x {vitoriasJogador} Jogador π§')
            else:    
                print('JOGADA INVΓLIDA!')
        elif jogadaComputador == 2: #computador jogou TESOURA
            if jogadaDoJogador == 0:
                vitoriasJogador += 1
                print(f'JOGADOR VENCEU!\n π₯οΈ  Computador {vitoriasMaquina} x {vitoriasJogador} Jogador π§')
            elif jogadaDoJogador == 1:
                vitoriasMaquina += 1
                print(f'COMPUTADOR VENCEU!\n π₯οΈ  Computador {vitoriasMaquina} x {vitoriasJogador} Jogador π§')
            elif jogadaDoJogador == 2:
                vitoriasMaquina += 1
                vitoriasJogador += 1
                print(f'EMPATOU!\n π₯οΈ  Computador {vitoriasMaquina} x {vitoriasJogador} Jogador π§')
            else:    
                print('JOGADA INVΓLIDA!')
    if vitoriasJogador > vitoriasMaquina:
        print(f'O jogador foi o grande campeΓ£o com um total de {vitoriasJogador} rodadas!')
    elif vitoriasMaquina > vitoriasJogador:
        print(f'O computador foi a grande vencedora com um total de {vitoriasMaquina} rodadas!') 
    elif vitoriasJogador == vitoriasMaquina:
        print('Eita rapaz... Deu empate! Tente novamente, vocΓͺ consegue!')   
    resp = input('VocΓͺ gostaria de jogar de novo? [s/n] ').lower()  
    while resp not in 'sn':
        resp = (input('Resposta invΓ‘lida! VocΓͺ gostaria de jogar novamente? [s/n]')).lower()
    if resp == 's':
        vitoriasMaquina = vitoriasJogador = 0
print()
print('Obrigado pela jogatina!')        