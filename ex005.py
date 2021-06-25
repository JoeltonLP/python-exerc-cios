#!/usr/bin/python3

# Faça um programa que leia um numero e mostre na tela seu sucessor e antecessor

number = int(input('Number: '))

back = number - 1
next = number + 1

print('back {}\nnext {}' .format(back, next))