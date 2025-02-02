estudiantes = {
    'estudiante1':{'nombre':'Juan','edad':20, 'grado': 'Medicina'},
    'estudiante2':{'nombre':'Pablo','edad':27, 'grado': 'Informática'},
    'estudiante3':{'nombre':'Marcos','edad':25, 'grado': 'Enfermería'}
}

for estudiante in estudiantes.values(): #1. Añade una nueva clave para la dirección.
        estudiante["dirección"]= "Desconocida"

print(estudiantes)    


estudiantes["estudiante2"]["grado"]="odontología"  #2. Modifica el grado del segundo estudiante.
print(estudiantes)



del estudiantes["estudiante3"] #3. Elimina el tercer estudiante del diccionario. 

print(estudiantes)

