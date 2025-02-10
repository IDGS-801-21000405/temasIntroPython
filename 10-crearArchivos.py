from io import open

lectura = ''
texto = open('archivo.txt', 'r')
lectura = texto.read()
print(lectura)
texto.close()