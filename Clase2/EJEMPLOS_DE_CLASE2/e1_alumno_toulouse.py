from e1_persona import Persona
# aqui o dentro del parantesis es que se coloca la clase Persona
class AlumnoToulouse(Persona):
    def __init__(self,dni,nombre,apellido,curso,horas):
        Persona.__init__(self,dni,nombre,apellido)
        self.curso=curso
        self.horas= horas
    
    def __str__(self):
        return f"Dni:{self.dni}, Nombre y Apellido:{self.nombre} {self.apellido}, Inscrito:{self.curso}, Horas de estudio: {self.horas}"

def main():
    alex= AlumnoToulouse(45981109,"Alex","Valdez","POOPYTHON",4)
    print(alex)


if __name__=="__main__":
    main()