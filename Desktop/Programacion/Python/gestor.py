import json


def cargar_jugador():
    try:
        with open("jugadores.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError:
        return []


jugadores = cargar_jugador()

class Jugador:
    def __init__(self, nombre, elo):
        self.nombre = nombre
        self.elo = elo

    def mostrar_jugador(self):
        print(self.nombre, self.elo)


def guardar_jugador(jugadores):
    with open("jugadores.json", "w") as archivo:
        json.dump(jugadores, archivo, indent=4)


def buscar_jugador(jugadores, nombre):
    for jugador in jugadores:
        if jugador["Nombre"].lower() == nombre.lower():
            return jugador
    return None


def act_elo(jugadores, nombre, nuevo_elo):
    for jugador in jugadores:
        if jugador["Nombre"].lower() == nombre.lower():
            jugador["Elo"] = nuevo_elo
            guardar_jugador(jugadores)
            return jugador
    return None


def agregar_jugador(jugadores, nombre, elo):
    nuevo_jugador = {"Nombre": nombre, "Elo": int(elo)}
    jugadores.append(nuevo_jugador)
    guardar_jugador(jugadores)
    return nuevo_jugador


def eliminar_jugador(jugadores, nombre):
    for jugador in jugadores:
        if jugador["Nombre"].lower() == nombre.lower():
            jugadores.remove(jugador)
            guardar_jugador(jugadores)
            return jugador
    return None


def ordenar_elo(jugadores):
    jugadores = sorted(jugadores, key=lambda jugador: jugador["Elo"])
    return jugadores

def menor_elo(jugadores):
    jugador = min(jugadores, key=lambda jugador: jugador["Elo"])
    return jugador

def mayor_elo(jugadores):
    jugador = max(jugadores, key=lambda jugador: jugador["Elo"])
    return jugador


def promedio_elo(jugadores):
    if len(jugadores) == 0:
        return 0

    elos = [jugador["Elo"] for jugador in jugadores]
    promedio = (sum(elos)) / (len(elos))


    return promedio


while True:
    print("====================")
    print("Gestor de Ajedrez")
    print("v0.6")
    print("====================")
    print("1. Buscar jugador")
    print("2. Actualizar ELO")
    print("3. Agregar jugador")
    print("4. Mostrar rankings ordenados")
    print("5. Eliminar jugador")
    print("6. Mostrar promedio de ELO")
    print("7. Mostrar mayor ELO")
    print("8. Mostrar menor ELO")
    print("9. Mostrar jugador")
    print("10. Salir")
    print("")

    opcion = input("Elige una opcion: ")

    if opcion == "1":
        nombre = input("Escribe el nombre del jugador: ")

        resultado = buscar_jugador(jugadores, nombre)

        if resultado is not None:
            print("Jugador encontrado!")
            print(resultado)
        else:
            print("Jugador no encontrado.")

    elif opcion == "2":
        nombre = input("Escribe el nombre del jugador: ")

        try:
            nuevo_elo = int(input("Escribe el nuevo elo: "))
        except ValueError:
            print("Prueba con un número!")
            continue

        resultado = act_elo(jugadores, nombre, nuevo_elo)

        if resultado is not None:
            print("Elo actualizado!")
            print(resultado)
        else:
            print("Jugador no encontrado.")

    elif opcion == "3":
        nombre = input("Escribe el nombre del jugador que quieres agregar: ")

        try:
            elo = int(input("Escribe su elo: "))
        except ValueError:
            print("Prueba con un número!")
            continue

        resultado = agregar_jugador(jugadores, nombre, elo)

        print("Jugador agregado!")
        print(resultado)

    elif opcion == "4":
        resultado = ordenar_elo(jugadores)

        print("Ranking:")
        for jugador in resultado:
            print(jugador["Nombre"], "-", jugador["Elo"], "ELO")

    elif opcion == "5":
        nombre = input("¿Qué jugador desea eliminar?: ")

        resultado = eliminar_jugador(jugadores, nombre)

        if resultado is not None:
            print("Jugador eliminado correctamente.")
        else:
            print("Jugador no encontrado.")

    elif opcion == "6":
        resultado = promedio_elo(jugadores)

        print("El promedio de ELO es:", resultado)


    elif opcion =="7":
        try:
            resultado = mayor_elo(jugadores)
            print("El mayor ELO es: ", resultado)
        except ValueError:
            print("La lista está vacía!")

    elif opcion =="8":
        try:
            resultado = menor_elo(jugadores)
            print("El menor ELO es: ", resultado)
        except ValueError:
            print("La lista está vacía!")

    elif opcion == "9":
        nombre = input("que jugador desea elegir?: ")
        for jugador in jugadores:
            if jugador["Nombre"] == nombre:
                objeto = Jugador(jugador["Nombre"], jugador["Elo"])
                objeto.mostrar_jugador()
        

    elif opcion == "10":
        print("Adiós...")
        break
    else:
        print("Opción no válida.")