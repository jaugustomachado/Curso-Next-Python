#Entre com um nome e imprima o nome somente se a primeira letra do nome for “a”
# (maiuscula ou minuscula).

nome=input('informe o texto para impressão: ')


if nome[0] =='A' or nome[0]=='a':
    print(nome)
else:
    print("o nome informado não começa com a letra 'a'")