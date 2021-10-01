'''Neste desafio, você tem a tarefa de criar um script Python para analisar os registros financeiros 
de sua empresa. Você trabalhará um conjunto de dados financeiros chamado dados_financeiros.txt. 
O conjunto de dados é composto por duas colunas: Data e Lucros/Perdas, separados por virgula. 
(Felizmente, sua empresa tem padrões bastante flexíveis para a contabilidade, então os registros são simples.)

Sua tarefa é criar um script Python que analise os registros para calcular cada um das seguintes informações:
    O número total de meses incluídos no conjunto de dados
    O valor total líquido de "Lucros / Perdas" durante todo o período
    A média dos "Lucros / Perdas" durante todo o período
    A média das mudanças em "Lucros / Perdas" durante todo o período
    O maior aumento nos lucros (data e valor) durante todo o período
    A maior redução nas perdas (data e valor) ao longo de todo o período

Por exemplo, sua análise deve ser semelhante a esta abaixo:

Analise financeira
----------------------------
Total de meses: 86
Total: $ 38382578
Média: $ 446309,04
Variação da média: $ -2315,12
Maior aumento nos lucros: fevereiro de 2012 ($ 1926159)
Maior redução nos lucros: setembro de 2013 ($ -2196167)

Além disso, seu script final deve imprimir a análise no terminal e exportar um arquivo de 
texto relatório.txt com os resultados.'''

import math as m
meses=[ ]
resultado=[ ]
maior_aumento=[]
maior_redução=[]
variacao=[]
with open('dados_financeiro.txt') as dados:
    dados.seek(19)
    for linha in dados:
        meses.append(linha.split(',')[0])
        resultado.append(int(linha.split(',')[1]))
    for n in range(85):
        variacao.append(resultado[n+1]-resultado[n])
  
with open('relatorio.txt' ,'w+') as relatorio:
    relatorio.write('Analise financeira \n')
    relatorio.write('----------------------------')
    relatorio.write(f'\nTotal de meses: {len(meses)} \n')
    relatorio.write(f'Total: $ {sum(resultado)} \n')
    relatorio.write(f'Média: $ {"{0:.8}".format(sum(resultado)/len(meses))} \n')
    relatorio.write(f'Variação da Média: $ {"{0:.6}".format(sum(variacao)/len(variacao))} \n')
    relatorio.write(f'Maior Aumento nos lucros: {meses[variacao.index(max(variacao))+1]} ($ {max(variacao)}) \n')
    relatorio.write(f'Maior Aumento nos lucros: {meses[variacao.index(min(variacao))+1]} ($ {min(variacao)}) \n')