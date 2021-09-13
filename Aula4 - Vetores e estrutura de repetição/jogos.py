#Crie uma lista com os preços dos jogos que você mais gosta.
#a) Imprima o preço mais caro;
#b) Imprima o preço mais barato.

n=int(input('informe quantos são os jogos preferidos: '))
preços_jogos=[ ]

for _ in range(n):
    preços_jogos.append(input('informe o preço de cada jogo: '))

print('o maior preço é: ', max(preços_jogos))
print('o menor preço é: ',min(preços_jogos))