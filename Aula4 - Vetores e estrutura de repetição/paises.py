#Crie uma lista de locais que você gostaria de conhecer no mundo, 
# na ordem do local que você dá mais prioridade pra o local que você dá menos prioridade. 
# Exiba a lista nas seguintes configurações:

#a) ordem original
#b) ordem alfabética
#c) ordem de prioridades inversa
#d) quantidade de itens

n=int(input('quantos lugares você gostaria de conhecer: '))
países=[ ]

for numero in range(n):
    países.append(input('informe o país na ordem de preferência: '))

print(países)

países.sort()
print(países)

países.reverse()
print(países)

print(len(países))