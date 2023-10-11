class TestClass():
    def operacion(self,variable):
        if type(variable)==int:
            print("A es un entero")
        elif type(variable)==str:
            print("A es texto")
        else:
            print("Otros")

def main():
    test=TestClass()
    a= 0.3333333
    test.operacion(a)

if __name__=="__main__":
    main()
