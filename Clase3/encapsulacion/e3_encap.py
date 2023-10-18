class Carro:
    def __init__(self, marca, modelo, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__precio = precio

    def get_precio(self):
        return self.__precio

mustang = Carro("Ford", "Mustang", 50000)
print(mustang.get_precio())