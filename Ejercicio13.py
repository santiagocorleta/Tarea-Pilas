from stack import Stack

pila_trajes = Stack()

trajes = [
    {"modelo": "Mark III", "pelicula": "Iron Man", "estado": "Impecable"},
    {"modelo": "Mark XLIV", "pelicula": "Avengers: Age of Ultron", "estado": "Dañado"},
    {"modelo": "Mark XLVII", "pelicula": "Spider-Man: Homecoming", "estado": "Dañado"},
    {"modelo": "Mark L", "pelicula": "Avengers: Infinity War", "estado": "Destruido"},
    {"modelo": "Mark LXXXV", "pelicula": "Avengers: Endgame", "estado": "Impecable"},
    {"modelo": "Mark XLVI", "pelicula": "Capitan America: Civil War", "estado": "Dañado"},
]

for t in trajes:
    pila_trajes.push(t)



def buscar_modelo(pila, modelo_buscar):
    aux = Stack()
    peliculas = []

    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == modelo_buscar:
            peliculas.append(traje["pelicula"])
        aux.push(traje)

 
    while aux.size() > 0:
        pila.push(aux.pop())

    if peliculas:
        print(f"\nEl modelo {modelo_buscar} fue usado en:")
        for p in peliculas:
            print(f" - {p}")
    else:
        print(f"\nEl modelo {modelo_buscar} no fue encontrado.")



def mostrar_dañados(pila):
    aux = Stack()
    print("\nModelos dañados:")

    while pila.size() > 0:
        traje = pila.pop()
        if traje["estado"] == "Dañado":
            print(f" - {traje['modelo']} en {traje['pelicula']}")
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())



def eliminar_destruidos(pila):
    aux = Stack()
    nueva = Stack()

    print("\nModelos eliminados (estado: Destruido):")

    while pila.size() > 0:
        traje = pila.pop()
        aux.push(traje)

    while aux.size() > 0:
        traje = aux.pop()
        if traje["estado"] == "Destruido":
            print(f" - {traje['modelo']} en {traje['pelicula']}")
        else:
            nueva.push(traje)

    return nueva



def agregar_modelo(pila, nuevo_traje):
    aux = Stack()
    existe = False

    while pila.size() > 0:
        traje = pila.pop()
        if traje["modelo"] == nuevo_traje["modelo"] and traje["pelicula"] == nuevo_traje["pelicula"]:
            existe = True
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())

    if existe:
        print("\nEl modelo ya fue cargado en esa película.")
        return pila

    pila.push(nuevo_traje)
    print("\nModelo agregado correctamente.")
    return pila



def trajes_en_peliculas(pila, peliculas_objetivo):
    aux = Stack()

    print("\nTrajes usados en las películas seleccionadas:")

    while pila.size() > 0:
        traje = pila.pop()
        if traje["pelicula"] in peliculas_objetivo:
            print(f" - {traje['modelo']} en {traje['pelicula']}")
        aux.push(traje)

    while aux.size() > 0:
        pila.push(aux.pop())


buscar_modelo(pila_trajes, "Mark XLIV")

mostrar_dañados(pila_trajes)

pila_trajes = eliminar_destruidos(pila_trajes)

nuevo_traje = {
    "modelo": "Mark LXXXV",
    "pelicula": "Iron Man 4",
    "estado": "Impecable"
}
pila_trajes = agregar_modelo(pila_trajes, nuevo_traje)

trajes_en_peliculas(
    pila_trajes,
    ["Spider-Man: Homecoming", "Capitan America: Civil War"]
)
