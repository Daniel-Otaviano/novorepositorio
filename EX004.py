#Exercicio de tipo primitivo

v = input('Digite algo: ')
print('O tipo primito é: {}'.format(type(v)))
print('A informação é alfanumérica?: {}'.format(v.isalnum()))
print('A informação é numérica?: {}'.format(v.isnumeric()))
print('A informação é alfabética?: {}'.format(v.isalpha()))
print('Está com letra minúscula?: {}'.format(v.islower()))
print('Está com letra maiúscula?: {}'.format(v.isupper()))
print('Está apenas com espaços?: {}'.format(v.isspace()))
print('Está capitalizada?: {}'.format(v.istitle()))# .istitle é letra maiuscula com minuscula.,/n
#  começa com Maiuscula em tudo após o espaço.
