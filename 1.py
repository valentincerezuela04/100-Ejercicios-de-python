#Calcular la secuencia de Fibonacci.

def fibonacci (n):
    fibonaccii=[0,1]
    while len(fibonaccii) < n:
     fibonaccii.append(fibonaccii[-2] +fibonaccii[-1])   
    return fibonaccii[:n] #imprime solo hasta 10 elementos

# Ejemplo de uso:
n=int(input("Ingrese la cantidad total de figonacci: "))
fib = fibonacci(n)
print(fib)   



