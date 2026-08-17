print('Welcome to the tip calculator!')

totalbill = float(input('What was the total bill? $'))
give = int(input('How much tip would you like to give? 10, 12, or 15? '))
split = int(input('How many people to split the bill? '))

# Cálculo da gorjeta e do total geral
percentual_gorjeta = give / 100#  Porcentagem da gorjeta em dinheiro
total_gorjeta = totalbill * percentual_gorjeta # Soma da gorjeta
bill_com_gorjeta = totalbill + total_gorjeta # Dividindo o total em n/pessoas

# Divisão do total pelas pessoas
total = bill_com_gorjeta / split

# Exibição formatada com 2 casas decimais (:.2f)
print(f'Each person should pay: ${total:.2f}')