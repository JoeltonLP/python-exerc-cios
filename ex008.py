#!/usr/bin/python3

# Escreva um programa que leia um valor em metros e o exiba convertido 
#em centímetros e milímetros

measure = float(input('measure in meter: '))

meter = measure
centimeter = meter * 100
milimeter = centimeter * (100 /10)

print('m:{:.1f}\ncm:{}\nmm:{}' .format(meter, centimeter, milimeter))




