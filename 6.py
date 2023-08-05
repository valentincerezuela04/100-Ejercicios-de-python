#calcular si un numero es primo o no




def es_primo(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

numero = int(input("ingresa un numero para saber si es primo:"))
print(es_primo(numero))