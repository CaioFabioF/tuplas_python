e = (int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')),int(input('Digite um valor: ')))
print(f'Você digitou os valores {e}')
print(f'O número 9 apareceu {e.count(9)} vezes.')
if 3 in e :
    print(f'O número 3 está na {e.index(3)} posição.')
else:
    print('O valor 3 não foi encontrado.')
print('Os valores pares foram: ',end=' ')
for c in e :
    if c % 2 == 0 :
        print(c,end=' ')

