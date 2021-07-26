#!/usr/bin/python3

#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, 
# com 15% de aumento. 

salary =  float(input('Wage: '))

new_salary = salary + ((15/100)*salary)

print('New Salary {:.2f}' .format(new_salary))