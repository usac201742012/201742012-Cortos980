
#ENCUENTRA LAS PAREJAS DE NUMEROS AMIGOS HASTA n, NO PUDE IMPLEMENTAR UN LISTADO YA QUE SON DOS NUMEROS Y NO SUPE CUAL DE LOS DOS ENLISTAR. 

numero = input('ingrese el valor de N: ')

if numero.isdigit():
    numero = int(numero)


for a in range(1, numero):
    aux = 0
    
    for i in range(1, a):
        if a % i == 0:
            aux += i

    for b in range(1, numero):
        t = 0
        for j in range(1, b):
            if b % j == 0:
                t += j
        if (aux == b and t ==a and a != b):
            print(a, b)
