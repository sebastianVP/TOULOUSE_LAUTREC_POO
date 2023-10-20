'''
TRABAJO FINAL DEL CURSO POO CON PYTHON:
RECOMENDACIONES Y EJEMPLO DE ESQUEMA.
LOS # INDICAN COMENTARIOS
'''

# EN LA PARTE SUPERIOR COLOCAR TODAS LAS LIBRERIAS A UTILIZAR Y QUE PERMITEN EJECUTAR
# LA APLICACION
import numpy
import os
import time

# 1.DECLARAR LA CLASE PRINCIPAL DE LA TAREA
# 2.DEFINIR SUS METODOS 
#   LA CLASE DEBE CONTAR CON UN METODO INIT DONDE SE DEBEN DECLARAR Y DEFINIR LOS ATRIBUTOS
#   DE ENTRADA. SE PUEDE DECLARAR DE MANERA ADICIONAL SI ES NECESARIO UN METODO LLAMADO SETUP
# 3.LA CLASE DEBE CONTAR CON LOS METODOS Y FUNCIONES QUE SE REQUIEREN PARA CUMPLIR CON EL
#   OBJETIVO DE LA CLASE, ES DECIR, SI LA CLASE DESCARGA PRIMERO ARCHIVOS, UN METODO QUE PERMITA REALIZAR 
#   ESTA OPERACION DE MANERA INDEPENDIENTE, SI LA CLASE ALMACENA Y GUARDA LOS ARCHIVOS DESPUES DE LA 
#   DESCARGA SE DEBE DEFINIR UN METODO QUE GUARDE LOS ARCHIVOS.
class MyApp():

    def __init__(self,atributo1,atributo2,...):
        ...

    def descargar_archivos(self):
        ...

    def guardar_archivos(self):
        ...

# PARA EJECUTAR EL PROGRAMA, SE DEBE DEFINIR AL FINAL DEL SCRIPT EL METODO MAIN DENTRO DEL 
# METODO MAIN LLAMAR A LA CLASE Y UTILIZAR SUS METODOS CORRESPONDIENTES.

def main():
    obj= MyApp()
    obj.descargar_archivos()
    obj.guardar_archivos()
# FINALMENTE ESCRIBIR LO SIGUIENTE:

if __name__== "__main__":
    main()