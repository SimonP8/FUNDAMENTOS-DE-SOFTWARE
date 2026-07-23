# usuarios.py
# Semana 6 - Quantum Wallet: codigo a MODELAR en UML (no se programa nada nuevo).
# Aqui estan las 3 clases que vas a dibujar como diagrama de clases:
#   Wallet, Usuario y UsuarioEmpresa.
# Para ejecutar (opcional, para verlo funcionar):  python usuarios.py


# ============================================================
# CLASE 1: Wallet (la billetera)
# ============================================================
class Wallet:
    def __init__(self):
        # __saldo lleva DOBLE guion bajo -> es PRIVADO.  En UML:  - saldo: float
        self.__saldo = 0.0

    # Metodos PUBLICOS.  En UML:  + consultar_saldo()
    def consultar_saldo(self):
        return self.__saldo

    def recargar(self, monto):        # + recargar()
        self.__saldo += monto
        return self.__saldo


# ============================================================
# CLASE 2: Usuario (el dueno de la billetera)
# ============================================================
class Usuario:
    def __init__(self, nombre):
        # 'nombre' es simple -> es PUBLICO.  En UML:  + nombre: str
        self.nombre = nombre

        # COMPOSICION: el Usuario "es dueno" de una Wallet, que se crea DENTRO de
        # su constructor. Si se borra el Usuario, su Wallet deja de existir.
        # __wallet lleva doble guion bajo -> PRIVADO.  En UML:  - wallet: Wallet
        self.__wallet = Wallet()

    # Metodo PUBLICO.  En UML:  + realizar_pago()
    def realizar_pago(self, monto):
        saldo = self.__wallet.consultar_saldo()
        if monto > saldo:
            raise ValueError("saldo insuficiente")
        self.__wallet.recargar(-monto)   # descuenta el pago
        return self.__wallet.consultar_saldo()

    def recargar_wallet(self, monto):
        return self.__wallet.recargar(monto)


# ============================================================
# CLASE 3: UsuarioEmpresa (HEREDA de Usuario)
# ============================================================
# HERENCIA: UsuarioEmpresa(Usuario) -> hereda TODO de Usuario y agrega lo suyo.
# En UML: una flecha con TRIANGULO HUECO que apunta al padre (Usuario).
class UsuarioEmpresa(Usuario):
    def __init__(self, nombre, nit):
        super().__init__(nombre)      # reutiliza el constructor del padre
        # __nit lleva doble guion bajo -> PRIVADO.  En UML:  - nit: str
        self.__nit = nit

    # Metodo PUBLICO propio.  En UML:  + generar_factura()
    def generar_factura(self):
        return f"Factura de {self.nombre} (NIT: {self.__nit})"


# ============================================================
# Demostracion (opcional)
# ============================================================
if __name__ == "__main__":
    ana = Usuario("Ana")
    ana.recargar_wallet(100000)
    print("Saldo tras pagar 30000:", ana.realizar_pago(30000))

    bancolombia = UsuarioEmpresa("Bancolombia", "900123456-7")
    bancolombia.recargar_wallet(500000)
    print(bancolombia.generar_factura())
    print("Saldo empresa:", bancolombia.realizar_pago(200000))
