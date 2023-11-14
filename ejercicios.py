class Estudiante:

    codigo=0
nombre=""
apellido=""

def imprimirDatos(self,codigo,nombre,apellido):
    print (self.codigo, self.nombre, self.apellido)

# Clase Estudiante
#Representa a un estudiante con atributos como el código, nombre y apellido.

# Atributos:
# codigo: el código del estudiante (valor numérico)
# nombre: el nombre del estudiante (cadena de texto)
# apellido: el apellido del estudiante (cadena de texto)

# Método imprimirDatos
#Imprime en la consola el código, nombre y apellido del estudiante. Recibe los parámetros código, nombre y apellido.

#crear objeto adso
adso=Estudiante()

#Accediendo a través del objeto adso a los atributos de la clase estudiante y dando valores 

adso.codigo = 1
adso.nombre = 'Sandra'
adso.apellido='Cruz'

adso.imprimir_Datos()

#Clase Constructor

class Estudiante1:

    def __init__(self, codigo, nombre,apellido):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido=apellido

    def imprimirInformacion(self):

        print (self.codigo, self.nombre, self.apellido)

adso1 =Estudiante1(2,'Maria','Galindo')
adso1.imprimirInformacion()

# Clase Estudiante1
# Representa a un estudiante con atributos como el código, nombre y apellido.

# Método _init_
# Inicializa la clase Estudiante1 con los parámetros código, nombre y apellido.

# Método imprimirInformacion
# Imprime en la consola el código, nombre y apellido del estudiante.

# Creación de instancia adso1
# Se crea una instancia de la clase Estudiante1 con los valores de código 2, nombre 'Maria' y apellido 'Galindo'.

# Llamada al método imprimirInformacion
# Se llama al método imprimirInformacion de la instancia adso1.