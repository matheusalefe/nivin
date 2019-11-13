import random, math, datetime
gost_identificar = str(input('Gostaria de se identificar? [S/N]: ')).strip().upper()[0]
if gost_identificar in 'S':
    nome = str(input('Certo, qual é o seu nome? ')).strip().capitalize()
    genero = str(input('E o seu gênero? [M/F/O]: ')).strip().upper()[0]
elif gost_identificar in 'N':
    print('Okay, vamos lá')
else:
    gost_identificar = str(input('Resposta inválida. Responda se gostaria ou não de se identificar [S/N]: '))
print('='*50)
print('''O que eu poderia fazer por você?
[0] Finalizar o programa
[1] Mostrar a tabuada de um número''')
escolha_usuario = str(input('Escolha: '))
if escolha_usuario not in '01':
    escolha_usuario = str(input('Resposta inválida, escolha uma opção existente: '))
