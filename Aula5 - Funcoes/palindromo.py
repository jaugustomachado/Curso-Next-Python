#Um palíndromo é uma palavra que se soletra da mesma forma nos dois sentidos,
#como “osso” e “reviver”. 
#Escreva um função que dado uma plavra verifique se ela é palindro.

def palindromo(palavra):
    if palavra == palavra[-1::-1]:
        print('é um palíndromo')
    else:
        print('não é palíndromo')
        
palindromo(input("informe uma palavra para verificação: ").lower())