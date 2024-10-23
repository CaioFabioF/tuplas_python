palavras = ('faca','tricolor','palmeiras','carro','cachorro','egua','horario','socrates')
for p in palavras :
    print(f'\n Na palavra {p.upper()} temos ',end=' ')
    for f in p :
        if f.lower() in 'aeiou' :
            print(f'{f}',end=' ')