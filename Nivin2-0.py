from random import choice, randint
from time import sleep
gost_identificar = str(input('Gostaria de se identificar? [S/N]: ')).strip().upper()[0]
if gost_identificar in 'S':
    nome = str(input('Certo, qual é o seu nome? ')).strip().capitalize()
    genero = str(input('E o seu gênero? [M/F/O]: ')).strip().upper()[0]
elif gost_identificar in 'N':
    print('Okay, vamos lá')
else:
    gost_identificar = str(input('Resposta inválida. Responda se gostaria ou não de se identificar [S/N]: '))
print('='*50)
print('O que eu poderia fazer por você?')
while True:
    print('''[0] Finalizar o programa
[1] Mostrar a tabuada de um número
[2] Jogar jokempô
[3] Jogos de adivinhação''')
    escolha_usuario = str(input('Escolha: '))
    if escolha_usuario not in '[0][1][2][3]':
        escolha_usuario = str(input('Resposta inválida, escolha uma opção existente: '))
    if escolha_usuario == '0':
        break
    elif escolha_usuario == '1':
        numero = float(input('Digite o número do qual gostaria da tabuáda: '))
        for c in range(1, 11):
            print(f'{numero} x {c} = {numero * c}')
            c += 1
    elif escolha_usuario == '2':
        escolhas_possiveis = ['Pedra', 'Papel', 'Tesoura']
        for item in escolhas_possiveis:
            print(f'[{item}]')
        escolha_jogador = str(input('Faça a sua escolha: ')).strip().capitalize()
        while escolha_jogador not in escolhas_possiveis:
            escolha_jogador = str(input('Resposta inválida. Faça a sua escolha: ')).strip().capitalize()
        print('JO')
        sleep(0.3)
        print('KEM')
        sleep(0.3)
        print('PÔ')
        sleep(0.3)
        escolha_computador = choice(escolhas_possiveis)
        if (escolha_jogador == 'Papel' and escolha_computador == 'Tesoura') or (escolha_jogador == 'Tesoura' and escolha_computador  == 'Pedra') or (escolha_jogador == 'Pedra' and escolha_computador == 'Papel'):
            print(f'Jogador: {escolha_jogador} x Computador: {escolha_computador}')
            print('Você perdeu. :o')
        elif (escolha_jogador == 'Tesoura' and escolha_computador == 'Papel') or (escolha_jogador == 'Papel' and escolha_computador  == 'Pedra') or (escolha_jogador == 'Pedra' and escolha_computador == 'Tesoura'):
            print(f'Jogador: {escolha_jogador} x Computador: {escolha_computador}')
            print('Você VENCEU!')
        elif escolha_jogador == escolha_computador:
            print(f'Jogador: {escolha_jogador} x Computador: {escolha_computador}')
            print('Houve um EMPATE')
    elif escolha_usuario == '3':
        print('''Escolha um dos modos de jogo:
[1] Jogo de adivinhação clássico (Adivinhe o número)
[2] Jogo de adivinhação reverso (Pense em um número)''')
        modo_de_jogo = input('Faça a sua escolha: ').strip()[0]
        while modo_de_jogo not in '[1][2]':
            modo_de_jogo = input('Resposta inválida. Escolha o modo de jogo [1] ou [2]: ').strip()[0]
        if modo_de_jogo in '[1]':
            print('-'*50)
            print('''Adivinhe o número entre 1 e 10 que eu pensei.
A cada resposta incorreta você perde 1 ponto e eu ganho 1.
Você inicia a partida com 10 pontos, quem tiver mais pontos no final ganha!''')
            pontos_j = 10
            pontos_m = 0
            resposta_correta = randint(1, 10)
            resposta_jogador = int(input('Sua tentativa: '))
            while resposta_jogador != resposta_correta:
                pontos_j -= 1
                pontos_m += 1
                resposta_jogador = int(input('Tente novamente: '))
            print('-'*50)
            if pontos_m > pontos_j:
                print(f'''Você perdeu! Placar final:
Jogador: {pontos_j}
Máquina: {pontos_m}''')
            elif pontos_m < pontos_j:
                print(f'''Você venceu! Placar final:
Jogador: {pontos_j}
Máquina: {pontos_m}''')
            else:
                print(f'''Houve um empate! Placar final:
Jogador: {pontos_j}
Máquina: {pontos_m}''')
            print('='*50)
