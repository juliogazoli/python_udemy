nome = 'Julio Gazoli'
altura = 1.75
peso = 75
imc = peso / (altura * altura)

# Julio Gazoli tem 1.80 de altura,
# pesa 75 quilos e seu IMC é
# 24.489795918367346

# f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'

print(linha_1)
print(linha_2)
