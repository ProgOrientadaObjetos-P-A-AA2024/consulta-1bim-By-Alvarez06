if __name__ == '__main__':
    # Creación de una lista con elementos iniciales
    lista_productos = ["leche", "huevos", "pan", "mantequilla", "yogurt"]

    # Mostrar la lista completa
    print("Lista de productos:")
    for producto in lista_productos:
        print(f"- {producto}")

    # Eliminar un elemento específico
    producto_a_eliminar = "mantequilla"
    # Si el producto a eliminar se encuentra en la lista de productos, entonces la elimina con .remove
    if producto_a_eliminar in lista_productos:
        lista_productos.remove(producto_a_eliminar)
        print(f"\nSe ha eliminado {producto_a_eliminar} de la lista.")
    else:
        # Caso contrario, muestra un mensaje diciendo que el elemento no se encuentra en la lista
        print(f"\nEl producto {producto_a_eliminar} no está en la lista.")

    # Verificar si un elemento está en la lista
    producto_a_buscar = "yogurt"
    # Misma logica, si la variable se encuentra en la lista especificada, imprime el mensaje
    if producto_a_buscar in lista_productos:
        print(f"\nEl producto {producto_a_buscar} sí está en la lista.")
    else:
        # Caso contrario, especifica la ausencia del mismo
        print(f"\nEl producto {producto_a_buscar} no está en la lista.")

    print("\nLista final de productos:")
    for producto in lista_productos:
        print(f"- {producto}")
