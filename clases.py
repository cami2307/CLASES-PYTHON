#Consulte un ejemplo donde se declare una clase con atributos y métodos.

class Persona:  # Definición de la clase Persona
    def __init__(self, nombre, edad):  # Método especial de inicialización de la clase
        self.nombre = nombre  # Asignación del atributo nombre
        self.edad = edad  # Asignación del atributo edad

    def saludar(self):  # Definición del método saludar
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 25)

# Acceder a los atributos y métodos de la instancia
print(persona1.nombre)  # Imprimir el valor del atributo nombre (Juan)
print(persona1.edad)  # Imprimir el valor del atributo edad (25)
persona1.saludar()  # Llamar al método saludar de la instancia (Hola, mi nombre es Juan y tengo 25 años.)

#Consulte un ejemplo donde se implemente la herencia

# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacerSonido(self):
        print("El animal hace un sonido.")

# Clase derivada que hereda de Animal
class Perro(Animal):
    def hacerSonido(self):
        print("El perro ladra.")

# Clase derivada que hereda de Animal
class Gato(Animal):
    def hacerSonido(self):
        print("El gato maulla.")

# Crear instancias de las clases derivadas
perro = Perro("Firulais")
gato = Gato("Misifu")

# Llamar al método hacer_sonido de cada instancia
perro.hacerSonido()  # El perro ladra.
gato.hacerSonido()  # El gato maulla.

#Consulte un ejemplo donde se implemente el polimorfismo

# Definición de una clase base "Animal"
class Animal:
    def _init_(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

# Definición de dos clases derivadas que heredan de "Animal"

class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice Woof!"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice Miau!"

# Función que toma un objeto de la clase base "Animal" y llama al método "hablar"
def hacerSonar(animal):
    return animal.hablar()

# Crear instancias de las clases derivadas
miPerro = Perro("Fido")
miGato = Gato("Whiskers")

# Llamar a la función con diferentes objetos
print(hacerSonar(miPerro))  # Salida: "Fido dice Woof!"
print(hacerSonar(miGato))   # Salida: "Whiskers dice Miau!"