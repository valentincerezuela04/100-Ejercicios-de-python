#Saber si una palabra es palindromo o no


def palindromoONo(s):
    i=0
    j=len(s)-1
    cont=0
    while i < j:
        if s[i] != s[j]:  
            return False
        i += 1
        j -= 1

    return True
   
                
   

def strToArray(prueba):
    i=0
    ar=[]
    while i < len(prueba):
        ar.append(prueba[i])

        i+=1

    return ar
#main:

palabra = str(input("ingrese una plabra:"))
array=strToArray(palabra)
es_palindromo=palindromoONo(array)

if es_palindromo == True:
    print(f"la palabra '{palabra}' es un palindromo")

else:
    print(f"la palabra '{palabra}' no es un palindromo")


    


