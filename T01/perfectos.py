


#LO HICE MEDIANTE UNA LISTA DEBIDO A QUE ES NECESARIO POSEER UNA GRAN CAPACIDAD DE COMPUTO PARA ENCONTRAR NUMEROS PERFECTOS

numerosperfectos = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128]

numero = input('ingrese el numero N: ')

if numero.isdigit():
        numero = int(numero)

if numero >= 9:
    print('El siguiente numero perfecto es demasiado grande, intente con uno menor.')

else:
    print(numerosperfectos[0:numero])
