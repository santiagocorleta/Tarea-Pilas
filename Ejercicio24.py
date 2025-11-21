from stack import Stack

pila_personajes = Stack()

# CARGAR LOS PERSONAJES EN LA PILA
datos = [
    {"nombre": "Iron Man", "peliculas": 10},
    {"nombre": "Captain America", "peliculas": 9},
    {"nombre": "Thor", "peliculas": 8},
    {"nombre": "Black Widow", "peliculas": 7},
    {"nombre": "Hulk", "peliculas": 6},
    {"nombre": "Rocket Raccoon", "peliculas": 5},
    {"nombre": "Groot", "peliculas": 4},
    {"nombre": "Doctor Strange", "peliculas": 4},
    {"nombre": "Gamora", "peliculas": 5},
    {"nombre": "Captain Marvel", "peliculas": 3}
]


for d in datos:
    pila_personajes.push(d)

def encontrar_posiciones(pila, nombres_buscar):
    aux = Stack()
    posiciones = {}
    pos_actual = 1

    # pasar todo a aux y registrar posiciones
    while not pila.is_empty():
        personaje = pila.pop()
        nombre = personaje["nombre"]
        if nombre in nombres_buscar:
            posiciones[nombre] = pos_actual
        aux.push(personaje)
        pos_actual += 1

    # restaurar pila
    while not aux.is_empty():
        pila.push(aux.pop())

    print("\nPosiciones desde la cima:")
    for nombre in nombres_buscar:
        if nombre in posiciones:
            print(f" - {nombre} está en la posición {posiciones[nombre]}")
        else:
            print(f" - {nombre} no está en la pila")
def personajes_mas_de_5(pila):
    aux = Stack()
    print("\nPersonajes con más de 5 películas:")

    while not pila.is_empty():
        personaje = pila.pop()
        if personaje["peliculas"] > 5:
            print(f" - {personaje['nombre']} ({personaje['peliculas']} películas)")
        aux.push(personaje)

    while not aux.is_empty():
        pila.push(aux.pop())     
def cantidad_peliculas_personaje(pila, nombre_buscar):
    aux = Stack()
    encontrado = False

    while not pila.is_empty():
        personaje = pila.pop()
        if personaje["nombre"].lower() == nombre_buscar.lower():
            print(f"\n{personaje['nombre']} participó en {personaje['peliculas']} películas.")
            encontrado = True
        aux.push(personaje)

    while not aux.is_empty():
        pila.push(aux.pop())

    if not encontrado:
        print(f"\n{nombre_buscar} no se encuentra en la pila.")
def nombres_con_letras(pila, letras):
    aux = Stack()
    print("\nPersonajes cuyos nombres comienzan con C, D o G:")

    while not pila.is_empty():
        personaje = pila.pop()
        if personaje["nombre"][0].upper() in letras:
            print(f" - {personaje['nombre']}")
        aux.push(personaje)

    while not aux.is_empty():
        pila.push(aux.pop())
