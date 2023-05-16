nome = input('Insira a palavra da forca:')
forca = list(nome)
chances = 6
certas = []
utl = []
escondida = ['_'] * len(forca)

while True:
    letra = input('Insira a letra que você acha que a palavra tem:')
    if letra in utl:
        print(f'A letra "{letra}" já foi utilizada:')
    if letra in forca:
        if letra in utl:
            chances -= 1
            print('Palavra:', ' '.join(escondida))
        else:
            certas += letra
            utl += letra
            print(f'A letra "{letra}" está na palavra, letras já utilizadas: {utl}')
            for i in range(len(forca)):
                if forca[i] == letra:
                    escondida[i] = letra
            print('Palavra:', ' '.join(escondida))
    else:
        if letra in utl:
            print(f'A letra "{letra}" já foi utilizada')
            print('Palavra:', ' '.join(escondida))
        else:
            print(f'A letra "{letra}" não está na palavra:')
            utl += letra
            print(f'Letras já utilizadas: {utl}')
            chances -= 1
            print('Palavra:', ' '.join(escondida))
    if len(certas) == len(forca):
        print(f'VOCÊ GANHOU: A palavra da forca era {nome} e te restaram {chances} chances.')
        break
    if chances == 0:
        print(
            '____\n'
            '|   O\n'
            '|  /|\ \n'
            '|  / \ \n'
        )
        print(f'Você perdeu, a palavra era {nome}')
        break
    if chances == 6:
        print(
            '____\n'
            '|\n'
            '|\n'
            '|\n'
        )
    elif chances == 5:
        print(
            '____\n'
            '|   O\n'
            '|\n'
            '|\n'
        )
    elif chances == 4:
        print(
            '____\n'
            '|   O\n'
            '|   |\n'
            '|\n'
        )
    elif chances == 3:
        print(
            '____\n'
            '|   O\n'
            '|  /|\n'
            '|\n'
        )
    elif chances == 2:
        print(
            '____\n'
            '|   O\n'
            '|  /|\ \n'
            '|\n'
        )
    else:
        print(
            '____\n'
            '|   O\n'
            '|  /|\ \n'
            '|  /\n'
        )