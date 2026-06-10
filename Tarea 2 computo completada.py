
## Inventa 5 ejemplos del uso de if para cada variante.
# Ejemplo 1: Uso de if simple
x = 10
if x > 5:
    print("x es mayor que 5")   
## Ejemplo 2: Uso de if-else
y = 3       
if y % 2 == 0:
    print("y es un número par")
else:    print("y es un número impar")
## Ejemplo 3: Uso de if-elif-else                
z = 15
if z < 10:
    print("z es menor que 10")
elif z == 10:
    print("z es igual a 10")    
else:    print("z es mayor que 10")
# Ejemplo 4: Uso de if anidado      
a = 8
if a > 0:
    if a % 2 == 0:
        print("a es un número positivo y par")
    else:
        print("a es un número positivo e impar")        
## Ejemplo 5: Uso de if con operadores lógicos
b = 12
if b > 0 and b < 20:
    print("b es un número positivo y menor que 20")
if b < 0 or b > 100:
    print("b es un número negativo o mayor que 100")

#Implementa una funcion que regrese el primer elemento de una lista
def first_element(lista): return lista[0]
lista = ["mango", "fresa", "piña", "uva", "naranja"]
print(first_element(lista))  # Output: "mango"

#Implementa una funcion que regrese el resto de los elementos de una lista
def rest_of_elements(lista): return lista[1:]
lista = ["mango", "fresa", "piña", "uva", "naranja"]
print(rest_of_elements(lista))  # Output: ["fresa", "piña", "uva", "naranja"]

# Algoritmo SUMALISTA
numeros = [1, 2, 3, 4, 5]
def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

print(sumar_lista(numeros))  # Output: 15

#Funcion Ultimo
#Algoritmo: por cada elemento de la lista
#crea una lista nueva colocando ese elemento al final de la lista nueva y regresa el primer elemento de la lista nueva
lista_original = ["perro", "gato", "conejo"]
def procesar_lista(lista):
    nueva_lista = []
    for elemento in lista:
        nueva_lista.append(elemento)
    return nueva_lista[0]
resultado = procesar_lista(lista_original)
print(resultado)  # Output: "perro"

#FACTORIAL
#Para una secuendia de numeros desde 1 hasta n, el factorial de n es el producto de todos los numeros en esa secuencia
def calcular_factorial(n):
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado
numero = 5
print(calcular_factorial(numero))  # Output: 120

#POTENCIA 
def calcular_potencia(base, exponente):
    if base == 0:
        return False
    resultado = 1
    for i in range(exponente):
        resultado *= base   
    return resultado
print(calcular_potencia(2, 3))  # Output: 8
print(calcular_potencia(0, 5))  # Output: False

#FIBONACCI
def fibonacci(indice_posicion):
    a = 0
    b = 1
    for i in range(indice_posicion):
        a, b = b, a + b
    return a

print("El numero de Fibonacci en el indice 6 es:", fibonacci(6))  # Output: 8