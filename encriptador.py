#Funcion de encriptar texto
def encriptar(texto):
    textoFinal = ''
    for letra in texto:
        oculto = ord(letra)
        oculto += 1
        textoFinal += chr(oculto)
    return textoFinal

#Funcion para desencriptar texto
def desencriptar(texto):
    textoFinal = ''
    for letra in texto:
        oculto = ord(letra)
        oculto -= 1
        textoFinal += chr(oculto)
    return textoFinal

#Encriptador de archivos llamando a la funcion encriptar
def encriptarArchivos(ruta):
    archivo = open(ruta, 'r')
    texto = archivo.read()
    archivoEncriptado = encriptar(texto)
    archivo.close()

    archivo = open(ruta, 'w')
    archivo.write(archivoEncriptado)
    archivo.close()
    print('El encriptado se realizo correctamente')

#Encriptador de archivos llamando a la funcion desencriptar
def desencriptarArchivos(ruta):
    archivo = open(ruta, 'r')
    texto = archivo.read()
    archivoDesenncriptado = desencriptar(texto)
    archivo.close()

    archivo = open(ruta, 'w')
    archivo.write(archivoDesenncriptado)
    archivo.close()
    print('El desencriptado se realizo correctamente')
#Inicio de interfaz
eleccion = input('Presione la letra "E" para encriptar, o "D" para desencriptar')
ruta = input('Ingrese la ruta del archivo')
#Opciones de interfaz
if eleccion == 'E':
    encriptarArchivos(ruta)
else:
    desencriptarArchivos(ruta)





