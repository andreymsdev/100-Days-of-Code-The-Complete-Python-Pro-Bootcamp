# hangman q eu pensei
import random

print('bem-vindo ao jogo da forca! ')

WORDS = ("python", "forca", "facilidade", "dificuldade", "resposta",  "telefone")
word = random.choice(WORDS)

# Oculta com _
oculta = ['_' for letra in word]
chances = 6

# While 
while chances > 0 and '_' in oculta:
    print('\nPalavra:', ' '.join(oculta))
    palpite = input('Digite uma letra: ').lower()

    if palpite in word:
        for index, letra in enumerate(word):
            if letra == palpite:
                oculta[index] = palpite
    else:  # Palpites
        chances -= 1
        print(f'Você errou! Você ainda tem {chances} chances!')

# Final
if '_' not in oculta:
    print(f'\nParabéns! Você venceu! A palavra era: {word}')
else:
    print(f'\nVocê Perdeu! A palavra era: {word}')  # Mudado de WORDS para word

