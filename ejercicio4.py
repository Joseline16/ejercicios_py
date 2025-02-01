grupo_a ={2,4,6,8,10}
grupo_b ={1,3,5,7,9}

union = grupo_a | grupo_b #1. Encuentra la unión de los dos conjuntos. 
print(union)

interseccion = grupo_a & grupo_b    #2. Encuentra la intersección de los dos conjuntos.  
print(interseccion)

diferencia = grupo_a - grupo_b #3. Encuentra la diferencia entre el primer conjunto y el segundo. 
print(diferencia)

disjuntos = grupo_a.isdisjoint(grupo_b) # 4. Verifica si los dos conjuntos son disjuntos. 
print(disjuntos)

