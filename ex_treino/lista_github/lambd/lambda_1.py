# Desenvolva um programa que leia o seu nome completo e que apresente somente o seu primeiro e último nomes
full_name = input('Write down your full name: ')
first_name = lambda name:   name.split()[0]
second_name = lambda name:  name.split()[1]

print(f'Your first name is {first_name(full_name)} and your second name is {second_name(full_name)}')