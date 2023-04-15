from dictionary import *
import linkedlist

new = dictionary(6)

# ------------ PRUEBA INSERT ------------


print("")
print(" ============== PRUEBA INSERT ============== ")
print("")
print("Inserto: 'buenas''tardes''hola''adios''llueve'")

insert(new, 7, "buenas")
insert(new, 1, "tardes")
insert(new, 3, "hola")
insert(new, 15, "adios")
insert(new, 8, "llueve")

for i in range(len(new)):
    if new[i] == None:
        print(None)
    else:
        linkedlist.printlinkedlist(new[i])

# ------------ PRUEBA SEARCH ------------
print("")
print(" ============== PRUEBA SEARCH ============== ")
print("")
print("Busqueda de key 1: ",search(new, 1))

# ------------ PRUEBA DELETE ------------

print("")
print(" ============== PRUEBA DELETE ============== ")
print("")
delete(new, 8)
print("Remuevo la key 8")
for i in range(len(new)):
    if new[i] == None:
        print(None)
    else:
        linkedlist.printlinkedlist(new[i])
        
delete(new, 3)
delete(new, 1)
print("")
print("Remuevo las key 1 y 3")

for i in range(len(new)):
    if new[i] == None:
        print(None)
    else:
        linkedlist.printlinkedlist(new[i])

# ------------ PRUEBA PERMUTACION ------------

print("")
print(" ============== PRUEBA PERMUTACION ============== ")
print("")
print("Son permutacion 'hola' y 'ahlo': ",isPermutation("hola", "alho"))
print("")
print("Son permutacion 'hola' y 'asado': ",isPermutation("hola", "asado"))

# ------------ PRUEBA UNICOS ------------

print("")
print(" ============== PRUEBA UNICOS ============== ")
print("")
List1 = [1,2,3,4,5,6,7,8,9]
print("Lista1: ", List1)
print("Los valores en la lista son unicos: ", Unique(List1))

List2 = [1,5,12,1,2]
print("")
print("Lista 2: ",List2)
print("Los valores en la lista son unicos: ", Unique(List2))

# ------------ PRUEBA POSTAL ------------
print("")
print(" ============== PRUEBA POSTAL ============== ")
print("")
codigopostal = "C1024CWN"

print("Codigo postal: 'C1024CWN', key = ",hashPostal(codigopostal, 1000))

codigopostal2 = "CWNC1042"

print("Codigo postal: 'CWNC1042', key = ",hashPostal(codigopostal2, 1000))

# ------------ PRUEBA COMPILADOR ------------
print("")
print(" ============== PRUEBA COMPILADOR ============== ")
print("")
print("Compilar 'aaaaabbbbbaaaaabbbbaab' = ",Compile("aaaaabbbbbaaaaabbbbaab"))
print("")
print("Compilar 'aabaab' = ",Compile("aabaab"))

# ------------ PRUEBA SUBSTRING ------------
print("")
print(" ============== PRUEBA SUBSTRING ============== ")
print("")
print("La subcadena 'ncag' se encuentra a partir de la posicion: ",subString("aconcagua", "ncag"))

# ------------ PRUEBA SUBSET ------------
print("")
print(" ============== PRUEBA SUBSET ============== ")
print("")
T = [1,2,3,4,5,6,7,8,9,10]
S = [5,7,8]
print("Lista T:", T)
print("Lista S:", S)
print("S es subconjunto de T: ", isSubset(S,T))