# Inventa 5 ejemplos del uso de if para cada variante.
# Ejemplo 1: Uso de if simple
x = 10
if x > 5:
    print("x es mayor que 5")   
# Ejemplo 2: Uso de if-else
y = 3       
if y % 2 == 0:
    print("y es un número par")
else:    print("y es un número impar")
# Ejemplo 3: Uso de if-elif-else                
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
# Ejemplo 5: Uso de if con operadores lógicos
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