

# --------------------------------------------- PARTE 1 ---------------------------------------------

#EJERCICIO 2

'''
insert(D,key, value)
Descripción: Inserta un key en una posición determinada por la función de hash (1)  en el diccionario (dictionary). Resolver colisiones por encadenamiento. En caso de keys duplicados se anexan a la lista.
Entrada: el diccionario sobre el cual se quiere realizar la inserción  y el valor del key a insertar 
Salida: Devuelve D
'''

'''
search(D,key)
	Descripción: Busca un key en el diccionario
Entrada: El diccionario sobre el cual se quiere realizar la búsqueda (dictionary) y el valor del key a buscar.
Salida: Devuelve el value de la key.  Devuelve None si el key no se encuentra.
'''

'''
delete(D,key)
Descripción: Elimina un key en la posición determinada por la función de hash (1) del diccionario (dictionary) 
Poscondición: Se debe marcar como nulo  el key  a eliminar.  
Entrada: El diccionario sobre el se quiere realizar la eliminación  y el valor del key que se va a eliminar.
Salida: Devuelve D
'''

# --------------------------------------------- PARTE 2 ---------------------------------------------

# EJERCICIO 3

'''
Considerar una tabla hash de tamaño m = 1000 y una función de hash correspondiente al método de la multiplicación donde A = (sqrt(5)-1)/2). Calcular las ubicaciones para las claves 61,62,63,64 y 65.
'''

# EJERCICIO 4

'''
Implemente un algoritmo lo más eficiente posible que devuelva True o False a la siguiente proposición: dado dos strings s1...sk  y p1...pk, se quiere encontrar si los caracteres de p1...pk corresponden a una permutación de s1...sk. Justificar el coste en tiempo de la solución propuesta.
'''

# EJERCICIO 5

'''
Implemente un algoritmo que devuelva True si la lista que recibe de entrada tiene todos sus elementos únicos, y Falso en caso contrario. Justificar el coste en tiempo de la solución propuesta.
'''

# EJERCICIO 6

'''
Los nuevos códigos postales argentinos tienen la forma cddddccc, donde c indica un carácter (A - Z) y d indica un dígito 0, . . . , 9. Por ejemplo, C1024CWN es el código postal que representa a la calle XXXX a la altura 1024 en la Ciudad de Mendoza. Encontrar e implementar una función de hash apropiada para los códigos postales argentinos.
'''

# EJERCICIO 7

'''
Implemente un algoritmo para realizar la compresión básica de cadenas utilizando el recuento de caracteres repetidos. Por ejemplo, la cadena ‘aabcccccaaa’ se convertiría en ‘a2blc5a3’. Si la cadena "comprimida" no se vuelve más pequeña que la cadena original, su método debería devolver la cadena original. Puedes asumir que la cadena sólo tiene letras mayúsculas y minúsculas (a - z, A - Z). Justificar el coste en tiempo de la solución propuesta.
'''

# EJERCICIO 8

'''
Se requiere encontrar la primera ocurrencia de un string p1...pk en uno más largo a1...aL. Implementar esta estrategia de la forma más eficiente posible con un costo computacional menor a O(K*L) (solución por fuerza bruta).  Justificar el coste en tiempo de la solución propuesta.
'''

# EJERCICIO 9

'''
Considerar los conjuntos de enteros S = {s1, . . . , sn} y T = {t1, . . . , tm}. Implemente un algoritmo que utilice una tabla de hash para determinar si S ⊆ T (S subconjunto de T). ¿Cuál es la complejidad temporal del caso promedio del algoritmo propuesto?
'''