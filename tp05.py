a = ('Caderno',20.0,'Borracha',2.0,'Lápis',1.50,'Estojo/Bolsinha',8.0,'Caneta',2.0,'Chamex',30.0,'Portifólio',40.0)
print('-='*50)
print(f'{"LISTAGEM DE PREÇOS":^90}')
print('-='*50)
for c in range(0, len(a)) :
    if c % 2 == 0 :
        print(f'{a[c]:.<30}',end='')
    else :
        print(f'R${a[c]:>.2f}')


