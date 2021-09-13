#Leia uma cadeia de caracteres e converta todos os caracteres para maiuscula. 
# Dica: subtraia 32 dos caracteres cujo codigo ASCII esta entre 97 e 122.

palavra = input('Digite uma palavra: ')

for x in (palavra):  
    if 97<=ord(x)<=122:
        print(chr(ord(x)-32), end='')
    else:
      print(x, end='')