# AgendaTelefono

Este código es una pequeña agenda telefónica que utiliza archivos de texto para almacenar los datos. El usuario puede realizar cuatro operaciones:

Obtener el teléfono de un contacto.
Añadir un nuevo contacto y su teléfono.
Eliminar un contacto existente.
Salir del programa.
El programa comienza configurando un registro de registro de eventos (logging) para registrar los errores y eventos importantes. A continuación, se definen cuatro funciones que realizan las operaciones de la agenda telefónica:

obten_telefono(file, client): Abre el archivo file y busca el nombre client en el directorio. Si encuentra el nombre, devuelve el teléfono correspondiente. Si no lo encuentra, escribe un mensaje de error en el archivo de registro y devuelve False.
agregar_telefono(file, client, telf): Abre el archivo file y busca el nombre client en el directorio. Si encuentra el nombre, pregunta al usuario si desea sobrescribir el contacto existente. Si el usuario no desea sobrescribir el contacto, devuelve False. Si el usuario confirma que desea sobrescribir el contacto, se llama a la función eliminar_telefono(file, client) para eliminar el contacto existente. A continuación, escribe el nuevo contacto en el archivo y devuelve True. Si no encuentra el nombre en el archivo, escribe el nuevo contacto en el archivo y devuelve True.
eliminar_telefono(file, client): Abre el archivo file y busca el nombre client en el directorio. Si encuentra el nombre, elimina el contacto del archivo y devuelve un mensaje de éxito. Si no lo encuentra, devuelve un mensaje de error.
crear_directory(file): Crea un archivo con el nombre file si no existe, y devuelve un mensaje de éxito. Si el archivo ya existe, pregunta al usuario si desea sobrescribir el archivo. Si el usuario no desea sobrescribir el archivo, devuelve un mensaje de advertencia.
Por último, se define la función directory(), que muestra un menú y llama a las funciones correspondientes según la opción seleccionada por el usuario. El programa se ejecuta en un bucle infinito hasta que el usuario seleccione la opción "Salir".
