#!/usr/bin/python3

# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pinta-la, 
# sabendo que cada litro de tinta, pinta uma área de 2m²


base = float(input('Base: '))
height = float(input('Height: '))

area = base * height 

liter = area / 2

print('{:.2f} liter of  paints' .format(liter))