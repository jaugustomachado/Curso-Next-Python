# Faça um programa com uma função chamada somaImposto. 
# A função possui dois parâmetros formais: taxaImposto, 
# que é a quantia de imposto sobre vendas expressa em porcentagem e custo, 
# que é o custo de um item antes do imposto. 
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaimposto, custo):
    
    soma = custo*(1+(taxaimposto/100))
    print('o valor do produto com o imposto é: R$', soma)

somaImposto(float(input(' informe a taxa do imposto em porcentagem: ')),float(input('informe o custo do produto: ')))