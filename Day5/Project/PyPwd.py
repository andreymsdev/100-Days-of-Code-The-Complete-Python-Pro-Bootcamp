import random
import string

# Letras, números e símbolos
caracteres = string.ascii_letters + string.digits + string.punctuation

# Define o tamanho da senha
tamanho = 12

# Cria a senha usando range dentro de uma compreensão de lista
senha_lista = [random.choice(caracteres) for _ in range(tamanho)]

# Junta tudo
senha_final = "".join(senha_lista)

print("Sua senha forte:", senha_final)


