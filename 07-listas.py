'''
Una lista es una secuencia de elementos
se crean con [] 
'''

lista1=['Gabriel', 21, 9.5, True, 'Mexicano', 15.2]
print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[-1])
print(lista1[0:3])
print(lista1[3:])

lista1.append("Sanchez")
print(lista1)

lista1.insert(2, "Diana")
print(lista1)

lista1.extend(["uno", 1.1, False])
print(lista1)

lista1.remove(21)
print(lista1)

lista1.pop()
print(lista1)

lista2 = ['tres', 'cuatro']
lista3 = lista1 + lista2
print(lista3)

print(lista2 * 2)

lista4 = [2, 1, 5, 4, 3]
print(lista4)
print(lista4.sort())

del lista4[0]
print(lista4)