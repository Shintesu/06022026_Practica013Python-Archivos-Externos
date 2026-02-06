# Curso Python. Archivos externos I. Vídeo 37
# usando el módulo io

from io import open # importar de io el método open

# puede ser abierto en modo lectura,  escritura y append
archivo_texto=open("archivo.text", "w") # método open pide 2 argumentos

# añadiendo una frase al archivo de texto vacío
frase="Estupendo día para estudiar Python \n el miércoles" # alt 92 slash inverso
archivo_texto.write(frase) # llamando la variable del archivo incluimos el método write con el argumento a añadir

archivo_texto.close()


#--------------------------------------------------------------

# abriendo el archivo en modo lectura
archivo_texto=open("archivo.text", "r") # método open pide 2 argumentos
texto=archivo_texto.read() # se usa el método read

archivo_texto.close # se cierra 

print(texto) # imprimimos en la terminal el texto escrito en el archivo externo


#--------------------------------------------------------------
# abriendo el archivo en modo lectura de líneas e indicando una línea para abrir
archivo_texto=open("archivo.text", "r") 

lineas_texto=archivo_texto.readlines()  

archivo_texto.close()

print(lineas_texto[0]) # al tratarse de una lista, podemos indicar cuál línea abrir con []


#---------------------------------------------------------------------

# puede ser abierto con append para añadir información
archivo_texto=open("archivo.text", "a") # 2do argumento método append

archivo_texto.write("\n Siempre es una buena ocasión para aprender Python") # con el método escribir añadimos el texto