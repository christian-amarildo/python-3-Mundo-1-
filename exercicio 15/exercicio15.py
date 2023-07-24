# Escreva um programa que pergunte a quantidade de Km percorridos 
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 
# R$0,15 por Km rodado.

# Solicitar ao usuário a quantidade de Km percorridos pelo carro alugado.
km = float(input("Digite a quantidade de quilômetros percorridos: "))

# Solicitar ao usuário a quantidade de dias que o carro foi alugado.
dias = int(input("Digite a quantidade de dias de aluguel: "))

# Calcular o preço do aluguel baseado no número de dias e no valor por dia (R$60).
precodia = 60 * dias

# Calcular o preço do aluguel baseado no número de quilômetros e no valor por quilômetro rodado (R$0,15).
precokm = 0.15 * km

# Calcular o preço total a pagar somando o valor do aluguel por dia e o valor do aluguel por quilômetro rodado.
preco = precodia + precokm

# Exibir o preço total a pagar ao usuário.
print("O preço total a pagar é: R$", preco)
