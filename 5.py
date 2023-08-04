#Calcular la suma de múltiplos


def multiplos():
    multiplo = int(input("ingrese un numero para poder mostrar sus multiplos: "))
    hasta = int(input("ingrese hasta que numero quiere que se muestren los multiplos: "))

    for i in range(1,hasta):
        
        multi= multiplo*i
        if multi <= hasta:
            print(f"|{multi}|")
        else:
            pass
        
        
def divisores():
    
    divisor = int(input("ingrese un numero para poder mostrar sus divisores: "))
    

    for i in range(1,divisor+1):
        
        if divisor %i == 0:
            print(f"|{i}|")
        else:
            pass
        
        


        
control='s'

while control =='s':
    
    opcion = int(input("""
                   -----Divisores y multiplos de cualquier numero!-----
                   cual deseas averiguar:
                   -1_Multiplos
                   -2_Divisores
                   
                   """))
    
    if opcion == 1:
       multiplos()
    
    else:
        divisores() 

    control=input("¿ Desea seguir ? : (s/n)")
    
