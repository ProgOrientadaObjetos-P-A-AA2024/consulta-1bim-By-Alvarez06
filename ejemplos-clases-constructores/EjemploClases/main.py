class Estudiante:
    # Clase que representa a un estudiante

    def __init__(self, nombre, edad):
        """
        Constructor de la clase Estudiante.

        Parámetros:
          nombre: El nombre del estudiante.
          edad: La edad del estudiante.

        El parámetro self es un elemento crucial en la POO de Python, ya que permite a los métodos definidos en una
        clase interactuar con los objetos sobre los que se invocan. Facilita el acceso a los atributos y métodos de los
        objetos, permitiendo una programación modular y reutilizable.
        """
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        """
        Método que imprime un saludo con el nombre y la edad del estudiante.
        """
        print(f"¡Hola! Mi nombre es {self.nombre} y tengo {self.edad} años de edad.")


if __name__ == '__main__':
    # Crear una instancia de la clase Estudiante usando el constructor elaborado
    estudiante1 = Estudiante("Juan", 30)
    estudiante2 = Estudiante("Daniel", 25)

    # Imprimir un saludo
    estudiante1.saludar()
    estudiante2.saludar()
