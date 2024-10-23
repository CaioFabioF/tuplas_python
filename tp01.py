c = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
a = -1
while True:
    a = int(input('Digite um número entre 0 e 10: '))
    if a >= 0 and a <= 10 :
        print(c[a])
    if a < 0 and a > 10:
        print('Tente novamente')
    b = str(input('Deseja continuar [S/N]: '))
    if b in 'Nn' :
        print('Fim')
        break
        