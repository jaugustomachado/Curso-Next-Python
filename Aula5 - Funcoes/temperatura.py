#Implemente um programa que possa receber do usuário a temperatura em graus
# Celsius ou Fahrenheit. Antes de receber a temperatura, 
# pergunte ao usuário se ele deseja inserir em Celsius ou em Fahrenheit. 
# Se a entrada for em graus Celsius, o programa deverá retornar a temperatura em Fahrenheit. 
# Se a entrada for em Fahrenheit o programa deverá retornar a temperatura em Celsius.

temp=(input('a temperatura que será informada é em celsius (C) ou farenheit (F)? ').upper())
if temp ==  'C':
    def celsiuspfarenheit (T):
        print('a temperatura em Farenheit é: ', T*1.8+32, '°F')
    
    celsiuspfarenheit(float(input('informe a temperatura:')))
elif temp ==  'F':
    def farenheitpcelsius (T):
        print('a temperatura em celsius é: ', (T-32)/1.8, '°C')
    
    farenheitpcelsius(float(input('informe a temperatura:')))

else:
    print('escolha informada incorretamente')