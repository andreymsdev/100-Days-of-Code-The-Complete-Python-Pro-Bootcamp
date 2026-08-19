import random

word_list = ['aardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input('Guess a Letter: ').strip().lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        print('RIght')
    else: 
        print('Wrong')
