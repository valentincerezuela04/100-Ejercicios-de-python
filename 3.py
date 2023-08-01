#Contar las palabras en un str.

def cantidadDePalabras(texto):
    espacio= " "
    cont=0
    for i in cadena:
    
        if i ==  espacio:
            cont+=1
    if cont == 0:
        print("ingrese una frase por favor, no una palabra")
        
        
    return cont



cadena=input("ingrese una frase:")
texto=cantidadDePalabras(cadena)
print(f"la cantidad de palabras que tiene las frase |{cadena}| es de :{texto}")