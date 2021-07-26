#!/usr/bin/python3

#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
# com 5% de desconto. #15

price = float(input('Product Price: '))

new_price = price-((5/100)*15)

print('New Price {:.2f}' .format(new_price))

