from random import choice
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
[2] Jogar jokempô''')
    escolha_usuario = str(input('Escolha: '))
    if escolha_usuario not in '012':
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
        escolha_usuario = str(input('Faça a sua escolha: ')).strip().capitalize()
        while escolha_usuario not in escolhas_possiveis:
            escolha_usuario = str(input('Resposta inválida. Faça a sua escolha: ')).strip().capitalize()
        print('JO')
        sleep(0.3)
        print('KEM')
        sleep(0.3)
        print('PÔ')
        sleep(0.3)
        escolha_computador = choice(escolhas_possiveis)
        if (escolha_usuario == 'Papel' and escolha_computador == 'Tesoura') or (escolha_usuario == 'Tesoura' and escolha_computador  == 'Pedra') or (escolha_usuario == 'Pedra' and escolha_computador == 'Papel'):
            print(f'Jogador: {escolha_usuario} x Computador: {escolha_computador}')
            print('Você perdeu. :o')
        elif (escolha_usuario == 'Tesoura' and escolha_computador == 'Papel') or (escolha_usuario == 'Papel' and escolha_computador  == 'Pedra') or (escolha_usuario == 'Pedra' and escolha_computador == 'Tesoura'):
            print(f'Jogador: {escolha_usuario} x Computador: {escolha_computador}')
            print('Você VENCEU!')
        elif escolha_usuario == escolha_computador:
            print(f'Jogador: {escolha_usuario} x Computador: {escolha_computador}')
            print('Houve um EMPATE')
