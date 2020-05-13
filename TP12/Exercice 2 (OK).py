#DEFINITION DES FOCNTIONS
def reverseString(s, i = 0):
    if i == len(s):
        return ""
    return reverseString(s, i+1) + s[i]

#PROGRAMME PRINCIPAL
print(reverseString("")) # ""
print(reverseString("bonjour")) # ruojnob
print(reverseString("ressasser")) # ressasser
