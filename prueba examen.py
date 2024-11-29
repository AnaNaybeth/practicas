"""
1)= es x=x-3
       x+1

#problem 1
n = 8
factorial = 1
for i in range(1, n+
1):
factorial *= i
print("El factorial de", n, "es:", factorial)

n=8
fac=1
while n<8:
    fac2=fac*1-n
    print("El factorial de", n, "es:", fac2)

#sxrip 1
cant=int(input("ingrese la cantidad en pesos mexicanos:"))
d=20.40
e=21.54
y=0.13
dolar=cant/d
euro=cant/e
yenes=cant/y
print(cant,"MXN=",dolar,"USD, ",euro,"E,",yenes,"Y")

#scrip3

import random

long=int(input("Ingrese la longitud de la lista:"))
lista=[]
pares=[]
impares=[]
for i in range(1,long+1):
    n=random.randint(1,100)
    lista.append(n)
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
print("Lista:",lista)
print("Numeros pares:",pares)
print("Numeros impares:",impares)
    

#scrip4
frase=input("Ingresa una frase:")
c=len(frase)
fs=frase.split()
p=len(fs)
print("Caracters:",c,"Palabras:",p)

#scric2-1
lista=input("Ingrese los numeros separados por espacio:")
lista1=[int(x) for x in lista.split()]
pares=[]
for x in lista1:
    if x%2==0:
        pares.append(x)
s=sum(pares)
print("La suma de los pares es",s)

#scric2-2
ct=input("Ingrese un texto:")
cdt=ct.split()
inv=[cdt[::-1] for cdt in cdt]
print(inv)


#scric2-3

lista=input("Ingrese los numeros separados por espacio:")
lista1=[int(x) for x in lista.split()]
conntar=[x for x in set(lista1) if lista1.count(x)>1]
print(conntar)

"""
