import random
from os import system, name

#Função para limpar tela em windows ou mac/linux
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else :
        _ = system('clear')

def game():

    limpa_tela()
    print('\nBoas vindas ao jogo da forca!')
    print('Escolha um tema:\n')
    print('1 - Capitais\n')
    print('2 - Frutas\n')
    print('3 - Animais\n')
    print('4 - Esportes\n')

        #Lista de palavras para o jogo
    capitais = [
        'PARIS',
                'LONDRES', 
                'ROMA',
                'HAVANA',
                'BOGOTA',
                'QUITO',
                'BERLIM',
                'LIMA',
                'CARACAS',
                'OSLO',
                'AMSTERDA',
                'LISBOA',
                'PEQUIM',
                'MANILA',
                'JACARTA',
                'BEIRUTE',
                'TAIPEI' ,
                'CANBERRA',
                'CAIRO',
                'LUANDA',
                'MAPUTO',
                'NAIROBI']
    frutas = [
        "MAÇA",
        "BANANA",
        "LARANJA",
        "MORANGO",
        "ABACAXI",
        "UVA",
        "MELANCIA",
        "PERA",
        "MANGA",
        "KIWI",
        "PESSEGO",
        "ABACATE",
        "CEREJA",
        "MAMAO",
        "LIMAO"
    ]
    animais = [
        "CACHORRO",
        "GATO",
        "ELEFANTE",
        "LEÃO",
        "TIGRE",
        "GIRRAFA",
        "CROCODILO",
        "MACACO",
        "PANDA",
        "PÁSSARO",
        "BALEIA",
        "GOLFINHO",
        "COBRA",
        "ÁGUIA",
        "RINOCERONTE"
    ]
    esportes = [
        "FUTEBOL",
        "BASQUETEBOL",
        "TÊNIS",
        "CRÍQUETE",
        "NATAÇÃO",
        "GOLFE",
        "CORRIDA",
        "CICLISMO",
        "VÔLEI",
        "HÓQUEI",
        "ATLETISMO",
        "BOXE",
        "ESCALADA",
        "SURFE",
        "ESGRIMA"
    ]


    #Escolha aleatória de palavras
    while True:
        escolha = int(input('Digite sua escolha(1/2/3/4):'))
        if escolha == 1:
            palavra = random.choice(capitais)
            break
        elif escolha == 2:
            palavra = random.choice(frutas)
            break
        elif escolha == 3:
            palavra = random.choice(animais)
            break
        elif escolha == 4:
            palavra = random.choice(esportes)
            break
        else:
            print('\nVocê não escolheu uma opção possível!\n')
            

    #List comprehension retorna _ para cada letra na palavra escolhida, ou seja, para cada item da string
    letras_descobertas = ['_' for letra in palavra]

    chances = 6

    #Criando lista para letras erradas
    letras_erradas = list()

    while chances > 0:
        print(' '.join(letras_descobertas))
        print('\nChances restantes:', chances)
        print('Letras erradas:', ' '.join(letras_erradas))

        #Tentativas
        tentativa = input('\nDigite uma letra: ').upper()

        #CONDICIONAL
        #Verifica se a letra está na palavra
        if tentativa in palavra:
            i = 0
            #Percorra cada letra da palavra a partir do indíce e verifique se a letra pode ser substituída pela letra digitada
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[i] = letra
                i += 1
        #Se não puder, remova uma chance
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        #CONDICIONAL 2

        if '_' not in letras_descobertas:
            print('\nParabéns! Você venceu! A palavra era: ', palavra)
            break

    #CONDICIONAL 3
    if '_' in letras_descobertas:
        print('Que pena! Você perdeu. A palavra era: ', palavra)


if __name__ == "__main__":
    game()

    










