#se importa el módulo os para realizar operaciones del sistema, como verificar la existencia de archivos y eliminarlos.
#se crea la clase Pelicula con los atributos privados __titulo, director, año, duracion y genero.

import os

class Pelicula:
    def __init__(self, titulo, director, año, duracion, genero):
        self.__titulo = titulo #atributo privado
        self.director = director
        self.año = año
        self.duracion = duracion
        self.genero = genero
        
    def __str__(self):
        return f"{self.__titulo} ({self.año}) - Dirigida por {self.director}"
    
class CatalogoPeliculas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ruta_archivo = "catalogo_de_peliculas.txt" #ruta del archivo
        if not os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'w') as archivo:
                pass
            
    def agregar(self, pelicula):
        with open(self.ruta_archivo, 'a') as archivo:
            archivo.write(str(pelicula) + '\n')
            
    def listar(self):
        if os.path.exists(self.ruta_archivo):
            with open(self.ruta_archivo, 'r') as archivo:
                peliculas = archivo.readlines() #leyendo archivo txt
                if peliculas:
                    print("Catálogo de Películas:")
                    for pelicula in peliculas:
                        print(pelicula.strip())
                else:
                    print("El catálogo está vacío.")
        else:
            print("El catálogo no existe.")
            
    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print("El catálogo ha sido eliminado.")
        else:
            print("El catálogo no existe.")
