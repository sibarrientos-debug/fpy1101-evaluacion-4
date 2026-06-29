def mostrar_menu():
    print("====== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("================================")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese un número del menú (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            print("Debe ingresar una opción entre 1 y 6.")
        except ValueError:
            print("Debe ingresar un número entero.")


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número entero.")


def validar_titulo(titulo):
    return titulo.strip() != ""


def validar_copias(copias):
    return copias >= 0


def validar_prestamo(prestamo):
    return prestamo > 0


def buscar_libro(lista, titulo):
    titulo = titulo.strip().lower()
    for indice, libro in enumerate(lista):
        if libro["titulo"].lower() == titulo:
            return indice
    return -1


def agregar_libro(lista):
    titulo = input("Ingrese el título del libro: ").strip()

    if not validar_titulo(titulo):
        print("El título no puede estar vacío.")
        return

    if buscar_libro(lista, titulo) != -1:
        print(f"El libro '{titulo}' ya se encuentra registrado.")
        return

    copias = leer_entero("Ingrese copias disponibles: ")
    if not validar_copias(copias):
        print("Las copias deben ser mayor o igual a 0.")
        return

    prestamo = leer_entero("Ingrese días de préstamo: ")
    if not validar_prestamo(prestamo):
        print("Los días de préstamo deben ser mayor a 0.")
        return

    nuevo_libro = {
        "titulo": titulo,
        "copias": copias,
        "prestamo": prestamo,
        "disponible": copias > 0
    }

    lista.append(nuevo_libro)
    print("Libro agregado correctamente.")


def eliminar_libro(lista):
    titulo = input("Ingrese el título del libro a eliminar: ")
    posicion = buscar_libro(lista, titulo)

    if posicion == -1:
        print(f"El libro '{titulo}' no se encuentra registrado.")
    else:
        libro_eliminado = lista.pop(posicion)
        print(f"El libro '{libro_eliminado['titulo']}' fue eliminado correctamente.")


def actualizar_disponibilidad(lista):
    for libro in lista:
        libro["disponible"] = libro["copias"] >= 1

    print("Disponibilidad actualizada correctamente.")


def mostrar_datos_libro(libro):
    print("Título:", libro["titulo"])
    print("Copias:", libro["copias"])
    print("Préstamo:", libro["prestamo"], "días")

    if libro["disponible"]:
        print("Estado: DISPONIBLE")
    else:
        print("Estado: SIN COPIAS")

    print("*" * 40)


def mostrar_libros(lista):
    if len(lista) == 0:
        print("No hay libros registrados.")
        return

    for libro in lista:
        libro["disponible"] = libro["copias"] >= 1

    print("=== LISTA DE LIBROS ===")
    for libro in lista:
        mostrar_datos_libro(libro)


lista_libros = []

while True:
    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_libro(lista_libros)

    elif opcion == 2:
        titulo = input("Ingrese el título a buscar: ")
        posicion = buscar_libro(lista_libros, titulo)

        if posicion > -1:
            print("Libro encontrado en la posición:", posicion)
            mostrar_datos_libro(lista_libros[posicion])
        else:
            print(f"El libro '{titulo}' no se encuentra registrado.")

    elif opcion == 3:
        eliminar_libro(lista_libros)

    elif opcion == 4:
        actualizar_disponibilidad(lista_libros)

    elif opcion == 5:
        mostrar_libros(lista_libros)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto.")
        break
