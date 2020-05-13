#DEFINITION DES FONCTIONS
def pow(x,n) :

    if n > 0 :
        #print('rentré dans le if')
        return powpositif(x,n)
    elif n == 0 :
        b = 1
        return b
    else :
        return pownegatif(x,n)


def powpositif(x,n) :
    a = 1
    #print('a initialisé')
    while n > 0 :
        #print(n)
        a = a * x
        n = n - 1
    return a


def pownegatif(x,n) :
    a = 1
    while n < 0 :
        a = a*x
        n = n - 1
    return 1/a

#PROGRAMME PRINCIPAL
print(pow(42, 0)) # 1
print(pow(1, 10)) # 1
print(pow(2, 5)) # 32
print(pow(7, 2)) # 49

