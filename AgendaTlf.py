import os
import logging
logging.basicConfig(filename='app.log', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S') #modo configuracion de loggin
def obten_telefono(file, client):
    try:
        f = open(file, "r")  # apertura de ficheros en modo lectura
    except FileNotFoundError:  # excepcion de error
        logging.error("El fichero " + file + " no existe\n") #con esto colocamos un log de tipo error para que el usuario no sepa donde a fallado el programa
        return False #resultado
    else:
        directory = f.readlines()  # devuelve una lista que contiene cada linea del archivo como un elemento de lista
        f.close()  # cerramos el fichero
        if (os.stat(file).st_size == 0):  # miramos cuantas lineas tiene el archivo y si es 0 es que esta vacio
            logging.error('Archivo de texto vacio')
            return False
        else:
            directory = dict([tuple(line.split(",")) for line in directory]) #creamos un diccionario y una tupla dentro de el donde separamos los datos con comas
            if client in directory:
                print("El contacto al que intentas acceder es: " + directory[client])
                return True
            else:
                logging.error('El contacto no existe')
                return False

def agregar_telefono(file, client, telf):
    try:
        f = open(file, "r")
    except FileNotFoundError:
        logging.error("El fichero " + file + " no existe\n")
        return False
    else:
        buscarTlf = obten_telefono(file, client) #llamamos a la funcion
        if buscarTlf:
            input("El contacto" + client + "¿quieres modificarlo? s/n: ")
            if "n":
                return False
            else:
               eliminar_telefono(file, client)

        f = open(file, "a") #abrimos archivo
        f.write(client + "," + telf + "\n") #escribimos en el archivo
        f.close() #cerramos el archivo
        return True
def eliminar_telefono(file, client):
    try:
        f = open(file, "r")
    except FileNotFoundError:
        return("El fichero " + file + " no existe\n")
    else:
        directory = f.readlines()
        f.close()
        directory = dict([tuple(line.split(",")) for line in directory])
        if client in directory:
            f = open(file, "w")
            del directory[client]
            for client, telf in directory.items():
                f.write(client + "," + telf)
                f.close()
            return("El cliente se a eliminado\n")
           
        else:
            return("El cliente " + client + " no existe\n")
def crear_directory(file):
    if os.path.isfile(file):
        respuesta = input("El fichero " + file + " ya existe. ¿quieres vaciarlo? s/n")
        if respuesta == "n":
            return("no se ha creado el fichero por que ya existe")
        f = open(file, "w")
        f.close()
        return("se a creado el fichero\n")
def menu():
    print("Agenda telefonica")
    print("=============")
    print("1- Obtener telefono")
    print("2- Añadir telefono")
    print("3- Eliminar telefono")
    print("4- Salir")
    opcion = input("introduzca la opcion deseada: ")
    return opcion
def directory():
    file = "agenda.txt"
    while True:
        opcion = menu()
        if opcion == "1":
            client = input("Introduce el nombre del contacto: ")
            if obten_telefono(file, client) is False:
                print("El contacto: " + client + ". No existe")
        elif opcion == "2":
            client = input("Introduce el nombre del contacto: ")
            telf = input("Introduce el telefono del contacto: ")
            if (agregar_telefono(file, client, telf)):
                print("se a  creado el nuevo contacto")
            else:
                print("se a producido un error al crear el nuevo contacto")
        elif opcion == "3":
            client = input("Introduce el nombre del contacto: ")
            print(eliminar_telefono(file, client))
        elif opcion == "4":
            break
        else:
            print("Introduzca una opcion del 1 al 4")

    return
directory()


#referencias
#https://github.com/JetBrains/ideolog/issues/55