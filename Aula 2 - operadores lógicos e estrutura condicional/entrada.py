#Crie um programa para um circo, no qual dada a idade de uma pessoa, seja indicado 
# o valor do ingresso segundo as regras:

#a) A entrada para qualquer pessoa com menos de 4 anos ou maior que 60 é gratuita;
#b) a entrada para qualquer pessoa com idade entre 4 e 18 custa 20 reais;
#c) a entrada para qualquer pessoa com 18 ou mais custa 30 reais;
#d) estudantes e professores pagam meia-entrada.

idade = int(input('informe a idade de uma pessoa: '))

if idade<4 or idade>60:
    print('entrada gratuita')
else:
    meia_entrada = input('a pessoa é estudante ou professor: (S/N): ')
    meia_entrada = meia_entrada.upper()
    if 4<=idade<18 and meia_entrada=='N':
        print('a entrada custa 20 reais')
    elif 18<=idade and meia_entrada=='N':
        print('a entrada custa 30 reais')
    elif meia_entrada=='S':
        if 4<=idade<18:
            print('meia entrada - 10 reais')
        if  18<=idade:
            print('meia entrada - 15 reais')