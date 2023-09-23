#convertidor de temperaturas

print("""
      1-Convertir de grados a Fahrenheit
      2-Convertir de  Fahrenheit a Grados
      
      """)

eleccion =int(input("eliga una opcion : "))

def grados_Fahrenheit(grados):
    return ( grados*9/5)+32
    

def  Fahrenheit_grados(Fahrenheit):
    return (Fahrenheit-32)*5/9
    
if eleccion == 1 :
    grados = int(input("Ingresar una temperatura en grados para poder covertirla a  Fahrenheit : "))
    gradoss = grados_Fahrenheit(grados)
    print(f"Los grados eran : '{grados}' y en  Fahrenheit son : {gradoss}")
    
else:
    Fahrenheit= int(input("ingresar una temperatura en  Fahrenheit para poder convertirla en grados : "))
    Fahrenheitt = Fahrenheit_grados(Fahrenheit)
    print(f"La temperatura en Fahrenheit era :'{Fahrenheit}' y a grados son : '{Fahrenheitt}'")



