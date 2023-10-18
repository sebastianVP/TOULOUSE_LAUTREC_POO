# encapsulamiento
# desde afuera directamente no se puede acceder a los valores
# internamente si
# el truco o el camino a seguir es utilizar metodos publicos
class Clase:
    atributo_clase = "Hola"   # Accesible desde el exterior
    __atributo_clase = "Hola2" # No accesible

    # No accesible desde el exterior
    def __mi_metodo(self):
        print("Haz algo")
        self.__variable = 0

    # Accesible desde el exterior
    def metodo_normal(self):
        # El método si es accesible desde el interior
        self.__mi_metodo()

    def check(self):
        print("hola",self.__atributo_clase)
        self.__mi_metodo()

mi_clase = Clase()
#mi_clase.__atributo_clase  # Error! El atributo no es accesible
#mi_clase.__mi_metodo()     # Error! El método no es accesible
#mi_clase.atributo_clase     # Ok!
#mi_clase.metodo_normal()    # Ok!
#mi_clase.check()
'''
OJO AQUI
'''
#print(dir(mi_clase))
#print(mi_clase._Clase__atributo_clase)
#print(mi_clase._Clase__mi_metodo())