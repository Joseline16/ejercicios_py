dia_semana = ('Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo')

print(dia_semana[3]) #1. Accede y muestra el tercer día de la semana. 

lista = list(dia_semana) #2. Convierte la tupla en una lista. 
print(lista)

lista.append('Nuevo día') #3. Añade un día adicional al final de la lista. 
print(lista)

tupla = tuple(lista) #4. Convierte la lista de nuevo en una tupla
print(tupla) 