def main():
    
    items = ['0. Salir', '1. Mostrar Puntaje', '2. Agregar Puntaje', '3. Eliminar Puntaje', '4. Ordenar Puntajes']
    scores = []
    quit_scores = False

    while quit_scores == False:
        for i in items:
            print(i)

        print()
        try:
            indice = int(input('Ingresar índice: '))

            if indice == 1:     
                if len(scores) == 0:
                    print('No hay puntajes todavía.\n')
                else:
                    for i in scores: 
                        print(i)
                    print()
            elif indice == 2:
                puntaje = int(input('Ingresar Puntaje: '))
                scores.append(puntaje)
                print()
            elif indice == 3:
                eliminar = int(input('Ingresar puntaje a eliminar: '))
                delete_value(scores, eliminar)
            elif indice == 4:
                scores.sort(reverse = True)
                print('Hemos ordenado los puntajes de mayor a menor.\n')
            elif indice == 0:
                print('\nGracias!')
                quit_scores = True
            else:
                print('No pudimos procesar su respuesta.\nAsegúrese de ingresar un número del 1-5.\n')
                
        except ValueError:
            print('No pudimos procesar su respuesta.\nAsegúrese de ingresar un número del 1-5.\n')
            
    

def delete_value(array, number):

    try:
        array.remove(number)
        print(f'El puntaje {number} se ha eliminado correctamente.\n')
    except: 
        print('El valor especificado no se encuentra.\n')


if '__main__' == __name__:
    main()