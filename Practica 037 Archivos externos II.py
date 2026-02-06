# Curso Python. Archivos externos II. Vídeo 38
# trabajar con ficheros externos de texto con el módulo io: Punteros de texto.

print("-------------prueba 01---------------")

archivo_texto=open("archivo.text", "r") 

print(archivo_texto.read()) # imprimimos el texto

archivo_texto.seek(0) # para posicionar el cursor

print(archivo_texto.read())




print("-------------prueba 02---------------")

archivo_texto=open("archivo.text", "r") 

#archivo_texto.seek(15) # para posicionar el cursor

print(archivo_texto.read(20)) # puede usarse para posicionar la lectura hasta un carácter específico
print(archivo_texto.read()) # continuará la lectura desde la posición actual del curso, es decir, la 20




print("-------------prueba 03---------------")

archivo_texto=open("archivo.text", "r") 

archivo_texto.seek(len(archivo_texto.read())/2) # posicionar en la mitad el cursor
print(archivo_texto.read())





print("-------------prueba 04---------------")

archivo_texto=open("archivo.text", "r") 

archivo_texto.seek(len(archivo_texto.readline())) # posicionar en la mitad el cursor
print(archivo_texto.read())




print("-------------prueba 05---------------")

archivo_texto=open("archivo.text", "r+") # r+ como segundo parámetro permite leer y escribir el archivo

archivo_texto.write("----------COMIENZO DEL TEXTO--------- \n Hola a todos \n Tomen asiento \n")

print(archivo_texto.readlines())





print("-------------prueba 06---------------")

archivo_texto=open("archivo.text", "r+") 

print(archivo_texto.readlines()) # nos devuelve una lista con los saltos de líneas






print("-------------prueba 07---------------")

archivo_texto=open("archivo.text", "r+") 

lista_texto=archivo_texto.readlines();

lista_texto[2]=" Esta línea fue añadida desde el exterior \n"

archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()



