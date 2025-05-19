# Lista que representa la pila de trajes
pila_trajes = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Impecable"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Dañado"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"},
    {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Impecable"},
    {"modelo": "Mark XLVI", "pelicula": "Capitan America: Civil War", "estado": "Dañado"},
]

# a. Buscar si el modelo Mark XLIV fue usado y en qué películas
def buscar_modelo(pila, modelo_buscar):
    peliculas = []
    for traje in pila:
        if traje["modelo"] == modelo_buscar:
            peliculas.append(traje["pelicula"])
    if peliculas:
        print(f"\nEl modelo {modelo_buscar} fue usado en:")
        for peli in peliculas:
            print(f" - {peli}")
    else:
        print(f"\nEl modelo {modelo_buscar} no fue encontrado.")

# b. Mostrar modelos dañados sin perder la pila
def mostrar_dañados(pila):
    print("\nModelos dañados:")
    for traje in pila:
        if traje["estado"] == "Dañado":
            print(f" - {traje['modelo']} en {traje['pelicula']}")

# c. Eliminar modelos destruidos mostrando sus nombres
def eliminar_destruidos(pila):
    nueva_pila = []
    print("\nModelos eliminados (estado: Destruido):")
    for traje in pila:
        if traje["estado"] == "Destruido":
            print(f" - {traje['modelo']} en {traje['pelicula']}")
        else:
            nueva_pila.append(traje)
    return nueva_pila

# e. Agregar el modelo Mark LXXXV si no está repetido en la misma película
def agregar_modelo(pila, nuevo_traje):
    for traje in pila:
        if traje["modelo"] == nuevo_traje["modelo"] and traje["pelicula"] == nuevo_traje["pelicula"]:
            print("\nEl modelo ya fue cargado en esa película.")
            return pila
    pila.append(nuevo_traje)
    print("\nModelo agregado correctamente.")
    return pila

# f. Mostrar trajes usados en películas específicas
def trajes_en_peliculas(pila, peliculas_objetivo):
    print("\nTrajes usados en las películas seleccionadas:")
    for traje in pila:
        if traje["pelicula"] in peliculas_objetivo:
            print(f" - {traje['modelo']} en {traje['pelicula']}")

buscar_modelo(pila_trajes, "Mark XLIV")  # Punto a

mostrar_dañados(pila_trajes)             # Punto b

pila_trajes = eliminar_destruidos(pila_trajes)  # Punto c

nuevo_traje = {
    "modelo": "Mark LXXXV",
    "pelicula": "Iron Man 4",  # Distinta película
    "estado": "Impecable"
}
pila_trajes = agregar_modelo(pila_trajes, nuevo_traje)  # Punto e

trajes_en_peliculas(
    pila_trajes,
    ["Spider-Man: Homecoming", "Capitan America: Civil War"]
)  # Punto f
