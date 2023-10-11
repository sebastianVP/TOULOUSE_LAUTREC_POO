class Usuarios:
    tipo_usuario = "Free"
    publicidad   = True

    def __init__(self,dni,alias,nombre):
        self.dni=dni
        self.alias=alias
        self.nombre= nombre
    
    def mostrar_datos(self):
        print("Elnombre del Usuario:",self.nombre)
        print("El DNI de usuario:",self.dni)
        print("El alias de Usuario", self.alias)

    def playmusic(self):
        if self.publicidad:
            print("La reproduccion del video contiene publicidad")
        else:
            print("La reproduccion del video no contine publicidad")


class UsuariosPremium(Usuarios):
    tipo_usuario= "Premium"
    publicidad  = False


    def __init__(self,dni,alias,nombre,compras):
        #Usuarios.__init__(self,dni,alias,nombre)
        super().__init__(dni,alias,nombre)
        self.compras = compras

def main():
    roberto = UsuariosPremium("45981109","roberto45","Roberto","Polo")
    roberto.mostrar_datos()
    roberto.playmusic()

if __name__=="__main__":
    main()


