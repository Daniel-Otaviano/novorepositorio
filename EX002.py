#Exercicio sobre input e .format

"""nome = input('Digite o seu nome: ')
print('Prazer em te conhecer,', nome, '!')

#Posso utilizar a formatação " {} " para colocar a variável dentro da frase.
#Exemplo:

msg = input('Digite um nome: ')
print('Prazer em te conhecer, {}!'.format(msg))"""


n = input("Nome: ")

def autenticacao(n):
    if (n == "daniel"):
        print("Bem vindo")
    else:
        print("Denied")

autenticacao(n)
