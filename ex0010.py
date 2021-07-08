#!/usr/bin/python3

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre 
# quantos Dólares ela pode comprar

real = float(input('money R$: '))
dolar_value = 5.28
value = real/dolar_value

print('R$ {} = $ {:.2f}' .format(real, value) )