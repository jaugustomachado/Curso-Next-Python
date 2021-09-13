#Faça um programa que receba do usuario uma string. O programa imprime a string sem suas vogais.
#(´,`,^,~).

nome=input('informe o texto para impressão: ')

print(nome.lower().replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
.replace('á','').replace('é','').replace('í','').replace('ó','').replace('ú','')
.replace('à','').replace('è','').replace('ì','').replace('ò','').replace('ù','')
.replace('â','').replace('ê','').replace('î','').replace('ô','').replace('û','')
.replace('ã','').replace('õ',''))


