'''Construa um dicionário para mapear o número do CEP dos seus colegas 
para o endereço da casa de cada um. Faça também um programa no qual o 
usuário insere o número do CEP e recebe como resposta o endereço. '''

dic={'11222333' : 'av. arco íris', '44455666':'av. vale do rio doce'}
#primeiro programa

cep=input('informe o cep para obter o endereço: ')
print('o endereço correspondente ao Cep inserido é: ', dic[cep])

#segundo programa
entrada = ''
ceps = {}

while entrada != '3':
  entrada = input('1 - para inserir\n2 - para buscar\n3 - para sair\n')

  if entrada == '1':
    cep = input('Digite o CEP: ')
    endereco = input('Digite o endereço: ')
    ceps[cep] = endereco
  elif entrada == '2':
    cep = input('Digite o CEP que você está buscando: ')
    print(ceps[cep])