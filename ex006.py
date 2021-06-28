#!/usr/bin/python3

# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt


number = int(input('Number: '))

doublo = number * 2
triple = number * 3
square_root = sqrt(number)

print('\nDoublo: {}\nTriple: {}\nSquare Root: {:.0f}' .format(doublo, triple, square_root))
