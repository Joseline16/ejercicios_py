persona1 = {'nombre':'Joseline','edad':'31','ciudad':'Albacete'}

persona1['profesión'] = 'Ingeniero' #1. Añade una nueva clave para la profesión. 
print(persona1)

persona1['ciudad'] = 'Lima' #2. Modifica la ciudad. 
print(persona1)

del persona1 ['edad']
print(persona1) #3. Elimina la clave de edad. 

claves= persona1.keys()
valores = persona1.values() #4. Muestra todas las claves y todos los valores por separado. 
print("Claves",list(claves))
print("valores",list(valores))