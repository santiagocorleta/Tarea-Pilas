# Pila de personajes (la cima es el final de la lista)
pila_personajes = [
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

# a. Determinar la posición de Rocket Raccoon y Groot (desde la cima)
def encontrar_posiciones(pila, nombres_buscar):
    print("\nPosiciones desde la cima:")
    for nombre in nombres_buscar:
        for i in range(len(pila)-1, -1, -1):  # Desde el final hacia el inicio
            if pila[i]["nombre"] == nombre:
                posicion = len(pila) - i
                print(f" - {nombre} está en la posición {posicion}")
                break
        else:
            print(f" - {nombre} no se encuentra en la pila")

# b. Mostrar personajes con más de 5 películas
def personajes_mas_de_5(pila):
    print("\nPersonajes con más de 5 películas:")
    for personaje in pila:
        if personaje["peliculas"] > 5:
            print(f" - {personaje['nombre']} ({personaje['peliculas']} películas)")

# c. Cantidad de películas de Black Widow
def cantidad_peliculas_personaje(pila, nombre_personaje):
    for personaje in pila:
        if personaje["nombre"].lower() == nombre_personaje.lower():
            print(f"\n{personaje['nombre']} participó en {personaje['peliculas']} películas.")
            return
    print(f"\n{name_personaje} no se encuentra en la pila.")

# d. Mostrar personajes cuyos nombres empiezan con C, D o G
def nombres_con_letras(pila, letras):
    print("\nPersonajes cuyos nombres comienzan con C, D o G:")
    for personaje in pila:
        if personaje["nombre"][0].upper() in letras:
            print(f" - {personaje['nombre']}")

# -----------------------------
# 🔽 Ejecución de los puntos
# -----------------------------
encontrar_posiciones(pila_personajes, ["Rocket Raccoon", "Groot"])         # Punto a
personajes_mas_de_5(pila_personajes)                                       # Punto b
cantidad_peliculas_personaje(pila_personajes, "Black Widow")              # Punto c
nombres_con_letras(pila_personajes, {"C", "D", "G"})                       # Punto d