import random


def generar_contrasena():
    mayusculas =['A','B','C','D','E','R','S','T','U','V','W','X','Y','Z']
    minusculas =['a','b','c','d','e','f','g','h','i','j','k','l','m']
    simbolos =['!','#','$','/','(','*','+','-']
    numeros =['1','2','3','4','5','6','7','8','9','10','11']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena =[]

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


def run():
    contrasena = generar_contrasena()
    print('tu nueva contraseña es: ' + contrasena)



if __name__=='__main__':
    run()