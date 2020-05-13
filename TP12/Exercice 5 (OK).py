#DEFINITION DES FONCTIONS
def product(a,b) :
    if b == 0 or a == 0 :
        return productNul(a,b)
    elif b > 0 :
        #print('ok')
        return productpositif(a,b)
    else :
        return productnegatif(a,b)

def productNul(a,b) :
    return 0

def productpositif(a,b) :
    c = 0
    while b != 0 :

        c = c + a
        b = b - 1
    return c

def productnegatif(a,b):
    if b%2 == 0 :
        a = 0
        while b != 0 :
            print('ok +')
            c = c + a
            b = b + 1
        return c
    else :
        a = 0
        while b != 0 :
            print('ok -')
            c = c + a
            b = b + 1
        c = c*(-1)
        return (c)

#PROGRAMME PRINCIPAL
print(product(5,2)) # 10
print(product(9,3)) # 27
