with open ('datos.txt', 'w') as fichero: #Crea un fichero de texto llamado "datos.txt" con el siguiente contenido: 
    fichero.write('Hola\nMundo\nPython\n')

fichero = open('datos.txt', 'r')  #Abre y lee todo el contenido del fichero. 
contenido = fichero.read()
print(contenido)

with open ('datos.txt', 'r') as fichero: #Crea un fichero de texto llamado "datos.txt" con el siguiente contenido: 
  for linea in fichero:
    print(linea.strip().upper())
