#!/usr/bin/python3


# Escreva um programa que converta uma temperatura digitada em °C e converta para °F. 

celsius = float(input('celsius: '))
converted_value_fahrenheit = ((celsius * 9) / 5) + 32 

print(f' {celsius}° celcius = {converted_value_fahrenheit}° fahrenheit')
