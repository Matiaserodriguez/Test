def main():
    
    guerrero_health = 10
    troll_health = 3

    count = 0


    while guerrero_health >= 0:
        print('Nuestro guerrero ha vencido a un Troll!')
        print(f'Nuestro guerrero ha perdido {troll_health} puntos.')
        print()
        count += 1
        guerrero_health -= troll_health
        

        if guerrero_health <= 0:
            print(f'Nuestro guerrero ha matado {count} Trolls')
            print('Pero nuestro guerrero ha sido derrotado!')


if '__main__' == __name__:
    main()