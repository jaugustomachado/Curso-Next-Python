#Faça um programa que leia um arquivo texto contendo uma lista de endereços IP
#e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
#será considerado um IP válido quando nenhuma de suas partes ultrapassar o número 255.

'''O arquivo de entrada possui o seguinte formato:
        200.135.80.9
        192.168.1.1
        8.35.67.74
        257.32.4.5
        85.345.1.2
        1.2.3.4
        9.8.234.5
        192.168.0.256
  O arquivo de saída possui o seguinte formato:
        [Endereços válidos:]
        200.135.80.9
        192.168.1.1
        8.35.67.74
        1.2.3.4
        9.8.234.5

        [Endereços inválidos:]
        257.32.4.5
        85.345.1.2
        192.168.0.256'''

#Criando arquivo e inserindo ip's
ipsvalidos=[ ]
ipsinvalidos=[ ]
with open('listaip.txt', 'w+') as listaip:
    listaip.write('200.135.80.9\n')
    listaip.write('192.168.1.1\n')
    listaip.write('8.35.67.74\n')
    listaip.write('257.32.4.5\n')
    listaip.write('85.345.1.2\n')
    listaip.write('1.2.3.4\n')
    listaip.write('9.8.234.5\n')
    listaip.write('192.168.0.256\n')
#Analisando ip's, criando a novalista e direcionando os ips válidos e inválidos

with open('listaip.txt') as listaip:   
    for linha in listaip:
        if (int(linha.split('.')[0])<255) and (int(linha.split('.')[1])<255) and (int(linha.split('.')[2])<255) and (int(linha.split('.')[3])<255):
            ipsvalidos.append(linha[:-1])
        else:
            ipsinvalidos.append(linha[:-1])
with open('novalista.txt','w+') as novalista:
    novalista.write('[Endereços válidos:]\n')
    for i in range(len(ipsvalidos)) :
        novalista.write(f'{ipsvalidos[i]}\n')
    novalista.write('\n[Endereços inválidos:]\n')
    for i in range(len(ipsinvalidos)) :
        novalista.write(f'{ipsinvalidos[i]}\n')