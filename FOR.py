# lista en python
mi_lista = ['pocho', 'sander', 'caca']
for nombre in mi_lista:
    print (nombre)

# Realizar un programa que imprima en pantalla los números del 20 al 30.
for x in range(20,31):
    print(x)
    '''La función range puede tener dos parámetros, el primero indica el valor inicial que tomará la variable x, 
    cada vuelta del for la variable x toma el valor siguiente hasta llegar al valor indicado por el segundo parámetro
     de la función range menos uno.'''    

#ESTRUCTURAS DE DATOS CON FOR

lista=[]  # declaramos la lista
for k in range(10):
	lista.append(input("introduce valor en lista:"))  # añadimos los valores de la lista por teclado

print("los elementos de la lista son:"+str(lista))  # visualizamos los elementos de la lista
valor=int(input("introduce el valor a modificar de la lista pon el indice:"))  # índice a modificar
nuevo=input ("introduce el nuevo valor:")  # valor nuevo de índice que se modifica
lista[valor]=nuevo  # hacemos la modificación
print("los elementos de la lista son:"+str(lista)) # visualizamos los elemntos para comprobar la modificación
valor=int(input("introduce el índice en el que se insertará el nuevo valor:"))  # índice donde se inserta en nuevo valor
nuevo=input ("introduce el nuevo valor:") # valor a insertar
lista.insert(valor, nuevo) 
print("los elementos de la lista son:"+str(lista)) # visualizamos los elemntos para comprobar la modificación
nuevo=input ("introduce el valor a eliminar:") # valor a eliminar
lista.remove(nuevo)   # eliminamos el valor
print("los elementos de la lista son:"+str(lista)) # visulaizamos lista
nuevo=input ("introduce el valor a buscar:")
resultado=(nuevo in lista)
if (resultado):
	print ("existe este elemento y su índice es:"+str(lista.index(nuevo)))
else:
	print("no exite es elemento")





