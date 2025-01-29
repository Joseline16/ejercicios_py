list_numeros = [1,2,3,4,5,6,7,8,9,10]

list_numeros.append(11)#1 Añade el número 11 al final de la lista
print(list_numeros)

list_numeros.insert(0,0)#2 Inserta el número 0 al principio de la lista. 
print(list_numeros)

list_numeros.pop(5)#3 Elimina el número 5 de la lista
print(list_numeros)

print(list_numeros[3:7] )#4 Muestra la sublista desde el tercer elemento hasta el sexto (inclusive). 

list_numeros.sort(reverse=True) #5 Ordena la lista en orden descendente. 
print(list_numeros)
