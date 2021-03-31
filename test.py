#Pregunta 1:
#Generar un codigo en python que sume 10 numeros aleatorios de la siguiente forma: los 5 mas bajos y los 5 mas altos
import random
ran = sum([random.randrange(1, 50, 1) for i in range(10)])

print ("Random number summation list is : " + str(ran))

#Pregunta 2:
#Escribir un codigo en python que sume y multiplique respectivamente todos los numeros de una lista, ejemplo
#Numeros=1 2 3 4, suma 10, multiplicacion 24.

def listaSuma(listaS) :

	resultado = 0
	for x in listaS:
		resultado = resultado + x
	return resultado

def listaMultiplicar(listaM) :
     
    resultado = 1
    for x in listaM:
         resultado = resultado * x
    return resultado
     

list1 = [1, 2, 3, 4]
print(listaSuma(list1))
print(listaMultiplicar(list1))

#Pregunta 3:
#Que es INDEX (indice) en base de datos, indicar beneficios y desventajas

'''El indice es una estructura de datos que mejora la velocidad de las operaciones que se realicen en una base de datos.
Ventajas 
 - Los índices nos permiten una mayor rápidez en la ejecución de las consultas tipo SELECT lo que sea WHERE
Desventajas
 - Los índices son una desventaja en aquellas tablas las que se utiliza frecuentemente operaciones de escritura (Insert, Delete, Update), esto es porque los índices se actualizan cada vez que se modifica una columna.
'''

#Pregunta 4
#Hacer un programa que tenga la funcion de listar las carpetas y archivos y ordenar por tamaño o fecha, y que muestre si hay archivos duplicados en contenido


#Pregunta 5
#Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24

def listaSuma(listaS) :

	resultado = 0
	for x in listaS:
		resultado = resultado + x
	return resultado

def listaMultiplicar(listaM) :
     
    resultado = 1
    for x in listaM:
         resultado = resultado * x
    return resultado
     

list1 = [1, 2, 3, 4]
print(listaSuma(list1))
print(listaMultiplicar(list1))


#Pregunta 6
#Crear una funcion que determine si dado una serie de parentesis, estas se encuentran en pares, es decir, abierto '(' y cerrado ')'.
#Ejm: Entrada: '(()()())()()(())' Salida: True  Entrada: '(()(' Salida: False

def matched(str):
    count = 0
    for i in str:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0
#Pregunta 7
#Desarrollar una funcion que me devuelva el n-esimo fibonacciRecordar que la serie fibonacci inicia en uno, es decir que fibonacci(1) = 1, ademas que el fibonacci(3) = fibonacci(2) + fibonacci(1)
#Nota: Implementarlo de modo iterativo.
def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a
#Pregunta 8
#Escribir un programa que tenga como input 10 numeros positivos de 3 digitos, y como output liste los que son capicuas, ordenandolos de menor a mayor

#Pregunta 9
#Hacer un programa que genere un array y que imprima los numeros que no son iguales

arreglo = [7, 7, 7, 20, 7, 7, 20, 10, 7, 404]
duplicados = any(x != 204 for x in arreglo)
print(duplicados)
#Defina indice en base datos, como hacer un flujo de respaldo, como operar con null

