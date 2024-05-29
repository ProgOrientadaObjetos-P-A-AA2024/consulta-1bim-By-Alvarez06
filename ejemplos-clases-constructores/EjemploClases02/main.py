class Curso:
    """
    Clase que representa a un curso académico.
    """

    def __init__(self, nombre, codigo, docente):
        """
        Constructor de la clase Curso.

        Parámetros:
          nombre: El nombre del curso.
          codigo: El código identificativo del curso.
          docente: El nombre del docente a cargo del curso.
        """
        self.nombre = nombre
        self.codigo = codigo
        self.docente = docente

    def mostrar_informacion(self):
        """
        Método que muestra información detallada del curso.
        """
        print(f"Nombre del curso: {self.nombre}")
        print(f"Código del curso: {self.codigo}")
        print(f"Docente a cargo: {self.docente}")


if __name__ == "__main__":
    # Crear instancias de la clase Curso
    curso1 = Curso("Algebra Lineal", "ALG-101", "Ing. Nora Parra")
    curso2 = Curso("Programación Orientada a Objetos", "POO-202", "Ing. René Elizalde")

    # Mostrar información de cada curso
    curso1.mostrar_informacion()
    print("------------------")
    curso2.mostrar_informacion()
