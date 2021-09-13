#Faça um programa que leia um nome de usuário e a sua senha e não aceite
#a senha igual ao nome do usuário, mostrando uma mensagem de erro
#e voltando a pedir as informações.

usuario=input('informe o usuário: ')
senha= input('informe a senha: ')

while usuario == senha:
    print('usuário e senha não podem ser iguais, favor informar novamente os dados: ')
    
    usuario=input('informe o usuário: ')
    senha= input('informe a senha: ')

else:
    print('dados aceitos com sucesso')