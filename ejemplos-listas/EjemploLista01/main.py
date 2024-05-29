if __name__ == "__main__":
    # Creación de una lista con elementos iniciales
    lista_frutas = ["manzana", "naranja", "tomate", "sandia", "banana"]

    # Modificar elementos de la lista
    lista_frutas[1] = "pera"  # Reemplaza "naranja" por "pera", debido al conteo desde 0 en indices

    # Agregar elementos a la lista
    lista_frutas.append("uvas")  # Agrega "uvas" al final de la lista con .append

    # Eliminar elementos de la lista
    lista_frutas.remove("manzana")  # Elimina "manzana" de la lista usando .remove
    # Este elimina cualquier elemento de la lista independientemente de su indice o posicion

    # Acceder a elementos de la lista por índice
    primera_fruta = lista_frutas[0]  # Obtiene el primer elemento (manzana)
    ultima_fruta = lista_frutas[-1]  # Obtiene el último elemento (banana)
    # El indice -1, sirve para ir directamente a la posicion final, -2 para la penultima posicion y así sucesivamente

    # Imprimir la lista por pantalla
    print(lista_frutas)
    print("La primera fruta de la lista es", primera_fruta, "y la ultima fruta de la lista es", ultima_fruta)
