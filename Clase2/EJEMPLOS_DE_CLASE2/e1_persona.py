class Persona():

    def __init__(self,dni,nombre,apellido):
        self.dni= dni
        self.nombre= nombre
        self.apellido=apellido

    def __str__(self):
        return f"Dni:{self.dni}, Nombre y Apellido:{self.nombre} {self.apellido}"

def main():
    Alex = Persona(45981109,"Alex","Valdez")
    print(Alex)

if __name__=="__main__":
    main()
