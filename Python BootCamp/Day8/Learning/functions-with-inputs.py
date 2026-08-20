def greet():
    print('Hello!') #algo
    print('How do you do?') 
    print('Isnt the weather nice?') # tutorial

greet()

# Basicmaente usamos as instruções dentro do def, assim não precisamos escrever linhas repetidas e gigantes de código

def conversation(): # define a string
    texto = input('Digite: bom dia, ou boa noite: ').strip().lower() 

    if texto == 'bom dia':
        print('Bom dia! Como você está? ')
    elif texto == 'boa noite':
        print('Boa noite, está meio tarde né?')
    else:
        print('OK...')

conversation()

name = input('Digite seu nome: ').strip().lower()

def greet_with_name(name):
    print(f'Hello, {name}!')
    print(f'How do you do, {name}?')

greet_with_name(name)