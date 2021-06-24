#!/usr/bin/python3

# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo
#primitivo e todas as informacoes possiveis sobre ele.

something = input('Type something: ')

print('which type primitive value? {}' .format(type(something)))
print('only have space? {}' .format(something.isspace()))
print('is a number? {}' .format(something.isdecimal()))
print('is a alphanumeric? {}' .format(something.isnumeric()))
print('is a alpha? {}' .format(something.isalpha()))
print('is all upercase? {}' .format(something.isupper()))
print('is all lowercase? {}' .format(something.islower()))
