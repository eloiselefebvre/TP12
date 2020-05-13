#DEFINITION DES FONCTIONS
def listSum(l) :
    if len(l) == 0 :
        return 0
    else :
        print('ok')
        return Sum(l)

def Sum(l) :
    a = 0
    while len(l) > 0 :
        a = a + l[0]
        del l[0]
    return a

#PROGRAMME PRINCIPAL
print(listSum([])) # 0
print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11
