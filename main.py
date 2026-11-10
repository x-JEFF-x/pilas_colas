import os
from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


# ------------------------- funciones de apoyo ✅ -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def limpiar_pantalla():
    # "cls" en Windows, "clear" en Mac/Linux
    os.system("cls" if os.name == "nt" else "clear")


def pausa():
    input("\n  Presione Enter para continuar...")


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        limpiar_pantalla()
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if pila.apilar(pasajero):                  # 2. LLAMAR
                print("  ✓ Apilado: ahora es el tope") # 3. MOSTRAR
        elif op == "2":
            pila.listar()
        elif op == "C":
            for p in datos_prueba():
                pila.apilar(p)
            print("  ✓ Datos de prueba apilados")

        elif op == "3":
            sacado = pila.desapilar()
            if sacado is None:
                print("  ⚠ La pila está vacía")
            else:
                tope = pila.ver_tope()
                if tope is None:
                    print(f"  Salió: {sacado.nombre} · la pila quedó vacía")
                else:
                    print(f"  Salió: {sacado.nombre} · nuevo tope: {tope.nombre}")
        elif op == "4":
            tope = pila.ver_tope()
            if tope is None:
                print("  ⚠ La pila está vacía")
            else:
                print(f"  Tope: {tope.nombre} ({tope.numero})")
        elif op == "5":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            posicion = pila.buscar(numero)
            if posicion == -1:
                print("  No existe")
            else:
                print(f"  Encontrado en [{posicion}]: {pila.datos[posicion].nombre}")
                revisados = ""
                for i in range(pila.cantidad - 1, posicion - 1, -1):
                    if revisados != "":
                        revisados = revisados + " → "
                    revisados = revisados + pila.datos[i].nombre
                print(f"  (revisó {revisados})")
        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if pila.modificar(numero, destino, asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe")
        elif op == "7":
            numero = leer_entero("  N.º de pasajero a eliminar: ")
            if pila.eliminar_por_numero(numero):
                print(f"  ✓ Pasajero {numero} eliminado")
            else:
                print("  No existe")
        elif op == "8":
            copia = pila.copiar()
            print("  Copia:")
            copia.listar()
            print("  Original:")
            pila.listar()
        elif op == "9":
            estado = "está vacía" if pila.esta_vacia() else "no está vacía"
            print(f"  Longitud: {pila.longitud()} · {estado}")

        elif op == "0":
            break
        else:
            print("  Opción no válida")
        pausa()                                        # deja leer el resultado


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        limpiar_pantalla()
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if cola.encolar(pasajero):                 # 2. LLAMAR
                print("  ✓ Encolado: está al final")   # 3. MOSTRAR
        elif op == "2":
            cola.listar()
        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)
            print("  ✓ Datos de prueba encolados")

        elif op == "3":
            sacado = cola.desencolar()
            if sacado is None:
                print("  ⚠ La cola está vacía")
            else:
                frente = cola.ver_frente()
                if frente is None:
                    print(f"  Salió: {sacado.nombre} · la cola quedó vacía")
                else:
                    print(f"  Salió: {sacado.nombre} · nuevo frente: {frente.nombre}")
        elif op == "4":
            frente = cola.ver_frente()
            if frente is None:
                print("  ⚠ La cola está vacía")
            else:
                print(f"  Frente: {frente.nombre} ({frente.numero})")
        elif op == "5":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            posicion = cola.buscar(numero)
            if posicion == -1:
                print("  No existe")
            else:
                print(f"  Encontrado en [{posicion}]: {cola.datos[posicion].nombre}")
                revisados = ""
                for i in range(0, posicion + 1):
                    if revisados != "":
                        revisados = revisados + " → "
                    revisados = revisados + cola.datos[i].nombre
                print(f"  (revisó {revisados})")
        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()
            if cola.modificar(numero, destino, asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  No existe")
        elif op == "7":
            numero = leer_entero("  N.º de pasajero a eliminar: ")
            if cola.eliminar_por_numero(numero):
                print(f"  ✓ Pasajero {numero} eliminado")
            else:
                print("  No existe")
        elif op == "8":
            copia = cola.copiar()
            print("  Copia:")
            copia.listar()
            print("  Original:")
            cola.listar()
        elif op == "9":
            estado = "está vacía" if cola.esta_vacia() else "no está vacía"
            print(f"  Longitud: {cola.longitud()} · {estado}")

        elif op == "0":
            break
        else:
            print("  Opción no válida")
        pausa()                                        # deja leer el resultado


# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        limpiar_pantalla()
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")
            pausa()


if __name__ == "__main__":
    main()
