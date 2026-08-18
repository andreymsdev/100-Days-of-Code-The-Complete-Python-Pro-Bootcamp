'''len('hello')

e_error-checking-and-conversion.py", line 1, in <module>
    len(12345)
    ~~~^^^^^^^
TypeError: object of type 'int' has no len()

print(type('hello'))
print(type(123))
print(type(3.14))
print(type(True))'''

# print(int('123') + int('456'))

# Challenge

# print('number of letters in your name' + len(input('Enter your name')))


'''
 nome_do_usuario = input('Seu nome: ')
tamanho_do_nome = len(nome_do_usuario)
print('Número de letras no seu nome: ' + str(tamanho_do_nome)) 
'''
nome_do_usuario = input('Seu nome: ')
tamanho_do_nome = len(nome_do_usuario)
print(f'Número de letras no seu nome: {tamanho_do_nome} ') # particularmente 


'''
nome_do_usuario = input('Seu nome: ')

# Dá para calcular direto dentro das chaves {}!
print(f'Número de letras no seu nome: {len(nome_do_usuario)}')
'''