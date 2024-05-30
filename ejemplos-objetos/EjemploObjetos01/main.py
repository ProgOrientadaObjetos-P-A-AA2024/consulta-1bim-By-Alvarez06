class Libro:
  """
  Define la clase Libro para modelar las características de un libro.
  """

  def __init__(self, titulo, autor, genero, anio_publicacion):
    """
    Constructor de la clase Libro.
    Con argumentos como titulo, autor, genero y año
    """
    self.titulo = titulo
    self.autor = autor
    self.genero = genero
    self.anio_publicacion = anio_publicacion

  def __str__(self):
    """
    Define la representación en cadena del objeto Libro.

    Es el equivalente a la funcion toString en Java, muestra una cadena la cual le damos el formato
    y presenta su contenido dependiendo del objeto
    """
    return f"Titulo: {self.titulo}, Autor: {self.autor}, Género: {self.genero}, Año de publicación: {self.anio_publicacion}"


if __name__ == '__main__':
    # Ejemplo de creación de instancias de la clase Libro
    libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía", 1954)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 1967)

    # Impresión de la información de los libros
    print(libro1)
    print(libro2)
