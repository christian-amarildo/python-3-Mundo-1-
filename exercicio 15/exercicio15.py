# Escreva um programa que pergunte a quantidade de Km percorridos 
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 
# R$0,15 por Km rodado.

km = float(input("escreva a distancia em km: "))
dias = int(input("escreva a quantidade de dias que ele foi alugado: "))
precodia= 60 * dias
precokm = 0.15 * km
preco = precodia + precokm
print("o preço total a pagar é: ", preco)