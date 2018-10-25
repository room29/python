#crear una comparacion de dos edades 1 y edad 2

edad1=int (input("ingrese edad1: "))
edad2=int (input("ingrese edad2: "))
if edad1>edad2:
    print ("es mayor ") 
if edad1==edad2: 
    print ("son iguales")
else :
    print ("edad2 es mayor")

#preguntar 10 veces un entero y luego sumar con while

x=1
suma=0
while x<=10:
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    x=x+1
print (suma)


#preguntar 10 veces un entero y luego sumar con FOR

lista=[]
for x in range (10):
    lista.append (int(input("introduce valor en lista:")))
    suma=0
for i in lista:
	suma += i
print ("el resultado es: " +str (suma))

#crear una funcion simple que MULTIPLIQUE,SUMA,RESTE Y DIVIDA dos numeros

def datos():
    global v1
    global v2
    v1=int(input("ingrese numeros"))
    v2=int(input("ingrese numeros"))

def suma():
    sumar= v1+v2
    print ("el resultado de la suma" +str(sumar) )

def resta():
    restar= v1-v2
    print ("el resultado de la resta" +str(restar) )


def dividir():
    divide= v1/v2
    print ("el resultado de dividir" +str(divide) ) 

def multi():
    multiplicar= v1*v2
    print ("el resultado de multiplicar" +str(multiplicar) )

datos()
suma()
resta()
dividir()
multi()

