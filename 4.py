#calcular el promedio de las notas de los alumnos con clases
#-ingresar las notas de los alumnos por consola
#-ingresar sus notas 
#-hacer una funcion que devuelva el promedio de estas mismas

class estudiantes:
    
    def __init__(self,nombre,edad,grado,promedio):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.promedio =promedio
        
   
    
def cargaAlumnos():    
    students=[]    
    cont=1
    control='s'
    while control == 's':
        
        print(f"-----Ingresar datos del estudiante {cont}-----")
        name=input(f"-ingrese el nombre del alumno {cont}:")
        age=int(input(f"-ingrese el la edad del alumno {cont}:"))
        grade=int(input(f"-ingrese el grado del alumno (en numeros){cont}:"))
        auxnotas=int(input(f"-ingrese cuantas notas va a ingresar de el alumno {cont}:"))
        i=1
        acum=0
        for i in range(1,auxnotas+1):
            notas=int(input(f"Ingrese la nota {i}:"))
            acum+=notas
            promedio=(acum/i)
               
        student = estudiantes(name,age,grade,promedio)
        students.append(student)
        cont+=1
        control =input("desea seguir cargando estudiantes (s/n):")
    return students  



def mostrarAlumnos(arreglo):
    for i, estudiante in enumerate(arreglo, 1):#enumerate es para leer los subindices del arreglo
        print(f"""
              
              -----Estudiante {i}:-----
              \nNombre: {estudiante.nombre}\nEdad: {estudiante.edad}\nGrado: {estudiante.grado}\nPromedio de notas: {estudiante.promedio}
              
              """)
    """
    en este print esta referenciando directamente a la clase ya que dentro del array tiene
    [[name,age,student][name,age,student]] #adetro de   las varables tee los datos de los alumnos   
         indice:0          indice:1

    """
    
    
arreglo_students =cargaAlumnos()
mostrarAlumnos(arreglo_students)    