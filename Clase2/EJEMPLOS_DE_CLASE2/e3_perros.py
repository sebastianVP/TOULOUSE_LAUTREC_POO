class Perros():
    def ladrar(self):
        print("GUAAAA GUAAAAAA")
    def grunir(self):
        print("GRRRR GRRRRRRRR")

class Caniche(Perros):
    def ladrar(self):
        print("guaaaa guaaaa")
    def grunir(self):
        print("grrrr  grrrr")

class PastorAleman(Perros):
    def ladrar(self):
        print("GuAuA GuAuAu")
    def grunir(self):
        print("GrGrgR GrGrGrGr")


class Shepadoodle(PastorAleman,Caniche):
    def ladrar_x(self,veces):
        for  cuantas in range(veces):
            #super(Shepadoodle,self).ladrar()
            super().ladrar()

def main():
    Tommy=PastorAleman()
    Copo = Caniche()
    Lazy = Shepadoodle()
    Lazy.ladrar_x(4)

if __name__ =="__main__":
    main()


