from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):                      # ✅ resuelto + mejora (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        if self.buscar(pasajero.numero) != -1:        # mejora: números únicos
            print("  ⚠ Ya existe un pasajero con ese número")
            return False
        self.datos[self.cantidad] = pasajero          # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del TOPE al FONDO
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):    # cantidad-1, ..., 1, 0  (hacia atrás)
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✅ IMPLEMENTADO (tabla 3) · recorre SIEMPRE del tope al fondo -------
    def desapilar(self):
        if self.cantidad == 0:
            return None
        tope = self.datos[self.cantidad - 1]          # solo sale el tope
        self.datos[self.cantidad - 1] = None          # no se corre nada: el cajón queda vacío
        self.cantidad = self.cantidad - 1
        return tope

    def ver_tope(self):
        if self.cantidad == 0:
            return None
        return self.datos[self.cantidad - 1]          # se mira, no se saca

    def buscar(self, numero):
        # Búsqueda lineal del TOPE al FONDO
        for i in range(self.cantidad - 1, -1, -1):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        posicion = self.buscar(numero)                # buscar ya recorre en el sentido de la pila
        if posicion == -1:
            return False
        self.datos[posicion].destino = nuevo_destino  # nadie cambia de lugar
        self.datos[posicion].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        # No se puede sacar del medio: se desapila hacia una pila AUXILIAR hasta encontrarlo
        auxiliar = MiPila(self.capacidad)
        encontrado = False
        while self.cantidad > 0 and not encontrado:
            pasajero = self.desapilar()
            if pasajero.numero == numero:
                encontrado = True                     # este se descarta
            else:
                auxiliar.apilar(pasajero)             # los demás esperan en la auxiliar
        # Se devuelven a la pila original: al invertirse dos veces, el orden queda igual
        while auxiliar.cantidad > 0:
            self.apilar(auxiliar.desapilar())
        return encontrado

    def copiar(self):
        nueva = MiPila(self.capacidad)
        for i in range(self.cantidad):                # del fondo al tope: el tope sigue siendo el mismo
            nueva.apilar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad                          # no hay que recorrer nada

    def esta_vacia(self):
        return self.cantidad == 0
