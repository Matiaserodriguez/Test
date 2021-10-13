from random import randint

def main():
    
    len_prog = ['JavaScript','Python', 'Java', 'php', 'Swift', 'Matalab', '.net', 'Ruby' ]

    guessed = False

    while guessed == False:
        lenguaje = sorted(len_prog[randint(0, len(len_prog) - 1)])
        print(f'La palabra a adivinar es: {"".join(lenguaje)}')
        input_user = input('Cual pensas que es? ')

        if input_user in len_prog:
            print('Esaa! Era esa misma, perfecto.')
            guessed = True
        else: 
            print('La palabra es incorrecta, intente de nuevo.\n')

if __name__ == '__main__':
    main()