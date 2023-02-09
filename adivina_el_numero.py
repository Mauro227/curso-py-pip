# import random


# def run():
#     numero_aleatorio = random.randint(1, 100)
#     numero_elegido = int(input('elige un numero del 1 al 100: '))
#     while numero_elegido != numero_aleatorio:
#         if numero_elegido < numero_aleatorio:
#             print('busca un numero mas grande: ')
#         else:
#             print('busca un numero mas pequeño: ')
#         numero_elegido = int(input('elige otro numero: '))
#     print('¡ ganste !')
    
# if __name__=='__main__':
#     run()


# import random

# def run():
#     numero_aleatorio = random.randint(1 , 100)
#     numero_elejido = int(input('ingrese un numero del 1 al 100: '))
#     while numero_elejido != numero_aleatorio:
#         if numero_elejido < numero_aleatorio:
#             print('busca un numero mas grande: ')
#         else:
#             print('busca un numero mas pequeño: ')
#         numero_elejido = int(input('elije otro numero:'))
#     print('ganaste')    




# if __name__=='__main__':
#     run()


# import random

# def run():
#     numero_aleatorio = random.randint(1 , 100)
#     numero_elejido = int(input('ingrese un numero del 1 al 100'))
#     while numero_elejido != numero_aleatorio:
#         if numero_elejido < numero_aleatorio:
#             print('busca un numero mas grande: ')
#         else:
#             print('elije un numero mas pequeño: ')
#         numero_elejido = int(input('elije otro numero: '))
#     print('ganaste')


# if __name__=='__main__':
#     run()


# import random

# def run():
#     numero_aleatorio = random.randint(1 , 50 )
#     numero_elejido = int(input('ingrese un numero del 1 al 50: '))
#     while numero_elejido != numero_aleatorio:
#         if numero_elejido < numero_aleatorio:
#             print('elije un numero mas grande: ')
#         else:
#             print('elije un numero mas pequeño: ')
#         numero_elejido = int(input('elije otro numero: '))
#     print('! GANASTE ¡ ')


# if __name__=='__main__':
#     run()

import random

def run():
    numero_aleatorio = random.randint(1 , 200)
    numero_elejido = int(input('elije un numero: '))
    while numero_elejido != numero_aleatorio:
        if numero_elejido < numero_aleatorio:
            print('elige un numero mas grande: ')
        else:
            print('elije un numero mas pequeño: ')
        numero_elejido= int(input('elije otro numero: '))
    print('*******FELICIDADES GANASTE WIIIIIIIII*******: ')    

if __name__=='__main__':
    run()