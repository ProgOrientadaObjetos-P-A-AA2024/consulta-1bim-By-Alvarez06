if __name__ == '__main__':
    # A pesar de que las tuplas son inmutables, estas se pueden utilizar para concatenar
    # Y crear una nueva tupla concatenada
    tupla1 = ("Contenido", "Tupla N°", 1)
    tupla2 = ("Datos de", "Tupla N°", 2)

    # Concatenar tuplas
    tupla_concatenada = tupla1 + tupla2
    print(tupla_concatenada,"\n")

    # Las tuplas nos brindan la facilidad de almacenar datos de diferentes tipos como por ejemplo
    # Numero entero, Cadena, Numero Real o decimal  y un booleano
    tupla_acceder = (1, "Byron", 18.5, True)

    # Las maneras en las que podemos acceder a los elementos de una tupla pueden ser desde
    print(tupla_acceder[0]) # indices, comenzando el conteo en 0 como el primer elemento
    print(tupla_acceder[-1],"\n")
    # Y como observamos anteriormente con indices negativos para expresar en orden inverso (ultimo, penultimo...)

    # E incluso podemos "desempaquetar" el contenido de una tupla en diferentes variables segun la longitud de este
    # Y mostrar por pantalla segun el caso que deseemos
    var1, var2, var3, var4 = tupla_acceder
    # Salida
    print(var1) # Salida: 1
    print(var2) # Salida: "Byron"
    print(var3) # Salida: 18.5
    print(var4) # Salida: True