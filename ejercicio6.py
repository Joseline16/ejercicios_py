#Crea un fichero de texto llamado "números.txt" y escribe en él los números del 1 al 10, 
# cada uno en una línea diferente. 
# Luego, lee y muestra el contenido del fichero. 
with open ('numeros.txt', 'w') as numeros:
    numeros.writelines(['1\n','2\n','3\n','4\n','5\n','6\n','7\n','8\n','9\n','10\n'])

numeros=open('numeros.txt','r')
leer=numeros.read()
print(leer)