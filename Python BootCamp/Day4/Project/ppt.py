import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______
         _______
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
          ________
      (____)
---.__(___)
'''

# Agrupa as artes em uma lista para facilitar a exibição
imagens_jogo = [pedra, papel, tesoura]

user = int(input('O que você escolhe? Pedra(0), Papel(1), Tesoura(2):\n'))

# 1. Validação inicial: Checa se o usuário digitou algo fora das opções válidas
if user >= 3 or user < 0:
    print('Você digitou um número inválido. Você perdeu por W.O.!')
else:
    # Mostra a jogada do usuário
    print("\nSua escolha:")
    print(imagens_jogo[user])

    # Gera e mostra a jogada do PC
    pc = random.randint(0, 2)
    print("Escolha do computador:")
    print(imagens_jogo[pc])

    # 2. Lógica das regras do jogo
    if user == 0 and pc == 2:
        print('Você venceu! (Pedra quebra Tesoura)')
    elif pc == 0 and user == 2:
        print('Você perdeu! (Pedra quebra Tesoura)')
    elif user > pc:
        print('Você venceu!')
    elif pc > user:
        print('Você perdeu!')
    elif pc == user:
        print('É um empate!')
