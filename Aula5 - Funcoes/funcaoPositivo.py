#Crie um programa que receba um valor inteiro e avalie se ele é positivo ou negativo. 
#Essa avaliação deve ocorrer dentro de uma função que retorna um valor booleano.

def positivo(numero):
    if numero>=0:
        return True
    else:
        return False

positivo(int(input('informe o número para verificar se o mesmo é positivo: ')))