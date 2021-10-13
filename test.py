import random

def main():
    
    print('Bienvenido a este espectacular juego,')
    print('Deberás adivinar un número entr 1 a 100!')
    print()
    print('Tenés hasta 10 intentos, sino fuiste!!')
    print()

    sigue_jugando = True

    count = 0
    guess_number = random_number()

    while sigue_jugando:

        try:
            user_input = int(input('Decime un número del 1 al 100: '))
            print()

            print(higher_lower(user_input, guess_number, count))
            count += 1

            if user_input == guess_number:
                print()
                print(f'GANASTE CAMPEÓN!')
                sigue_jugando = False

            elif count == 10:
                print('Che, hiciste 10 intentos, Game Over')
                sigue_jugando = False

        except ValueError:
            print()
            print('Solo se aceptan números. Por favor intente de nuevo.\n')
            continue

def random_number():
    guess = random.randint(1, 100)

    return guess

def higher_lower(number, guess, tries):
    
    if number > guess:
        return 'Mas bajo...\n'
    elif number < guess:
        return 'Mas alto...\n'
    elif number == guess:
        return f'Sos re piola, adivinaste el número en {tries} intentos!!!!!!!!!!!!!!!!!!!'

if '__main__' == __name__:
    main()