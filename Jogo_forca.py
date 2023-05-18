import random

palavras = ['gato', 'cachorro', 'elefante', 'leao', 'tigre', 'girafa']
palavra_secreta = random.choice(palavras)
letras_descobertas = ['_'] * len(palavra_secreta)
tentativas = 6

while True:
    print(''.join(letras_descobertas))

    if tentativas == 0:
        print('Você perdeu! A palavra secreta era:', palavra_secreta)
        break

    if '_' not in letras_descobertas:
        print('Parabéns! Você acertou a palavra secreta:', palavra_secreta)
        break

    letra = input('Digite uma letra: ')

    if letra in palavra_secreta:
        print('A letra está na palavra!')
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
    else:
        print('A letra não está na palavra.')
        tentativas -= 1
