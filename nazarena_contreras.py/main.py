#Este archivo contendrá la interfaz de usuario e importará las clases y métodos desde catalogo.py:
# #se importa la clase Pelicula y CatalogoPeliculas desde el módulo catalogo.
# #se crea un menú para que el usuario pueda interactuar con el catálogo de películas.

from catalogo import Pelicula, CatalogoPeliculas

catalogo = CatalogoPeliculas("catalogo_películas")

while True:
    print("\nMenú de Opciones:")
    print("1. Agregar película")
    print("2. Listar películas")
    print("3. Eliminar catálogo de películas")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    
    if opcion == '1':
        titulo = input("Introduce el título de la película: ")
        director = input("Introduce el director de la película: ")
        año = input("Introduce el año de la película: ")
        duracion = input("Introduce la duración de la película: ")
        genero = input("Introduce el género de la película: ")
        
        pelicula = Pelicula(titulo, director, año, duracion, genero)
        catalogo.agregar(pelicula)
        print("Película agregada correctamente.")
    elif opcion == '2':
        catalogo.listar()
    elif opcion == '3':
        catalogo.eliminar()
    elif opcion == '4':
        print("Cerrando programa.")
        break
    else:
        print("Opción no válida. Inténtalo de nuevo.")