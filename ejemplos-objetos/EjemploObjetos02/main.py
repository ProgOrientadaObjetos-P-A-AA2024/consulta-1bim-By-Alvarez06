class CuentaBancaria:
  # Define la clase CuentaBancaria para modelar las características de una cuenta bancaria.

  def __init__(self, nombre_titular, numero_cuenta, saldo_inicial):
    """
    Constructor de la clase CuentaBancaria.
    Con argumentos como nombre del titular, el numero de cuenta y un saldo inicial
    """
    self.nombre_titular = nombre_titular
    self.numero_cuenta = numero_cuenta
    self.saldo = saldo_inicial

  def __str__(self):
    """
    Muestra por pantalla la representacion del objeto de la clase en una cadena con sus atributos
    """
    return f"Titular: {self.nombre_titular}, Número de cuenta: {self.numero_cuenta}, Saldo: ${self.saldo:.2f}"

  def depositar(self, monto):
    """
    Funcion para depositar un monto en la cuenta creada, o el objeto instanciado
    """
    if monto > 0:
      self.saldo += monto
      print(f"\nSe ha depositado ${monto:.2f} en la cuenta {self.numero_cuenta}.")
    elif monto < 0:
      print("El monto no puede ser un numero negativo.")
    else:
        print("El monto debe ser mayor a 0")

  def retirar(self, monto):
    """
    Funcion para retirar un monto en la cuenta creada, o el objeto instanciado
    """
    if monto > 0 and self.saldo >= monto:
      self.saldo -= monto
      print(f"Se ha retirado ${monto:.2f} de la cuenta {self.numero_cuenta}.\n")
    elif monto < 0:
        print("El monto a retirar no puede ser menor a 0")
    else:
      print(f"Saldo insuficiente para retirar ${monto:.2f}.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Ejemplo de creación de instancias de la clase CuentaBancaria con el uso del constructor definido
    cuenta_ahorro = CuentaBancaria("Cielo Yepez", "123456789", 1000.00)
    cuenta_corriente = CuentaBancaria("Pedro López", "987654321", 500.00)

    # Impresión de la información de las cuentas
    print(cuenta_ahorro)
    print(cuenta_corriente)

    # Ejemplo de uso de los métodos depositar y retirar
    cuenta_ahorro.depositar(200.00)
    cuenta_corriente.retirar(150.00)

    # Impresion final con los cambios realizados
    print(cuenta_ahorro)
    print(cuenta_corriente)

