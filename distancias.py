class Distancias:

    def solicitarDatos(self):
        self.x1 = int(input("Ingresa el valor para x1: "))
        self.x2 = int(input("Ingresa el valor para x2: "))
        self.y1 = int(input("Ingresa el valor para y1: "))
        self.y2 = int(input("Ingresa el valor para y2: "))

    def calcularDistancia(self):
        distancia_x = self.x2 - self.x1
        distancia_y = self.y2 - self.y1
        distancia = ((distancia_x ** 2) + (distancia_y ** 2)) ** 0.5
        print("La distancia entre los dos puntos es: {}".format(distancia))

def main():
    obj = Distancias()
    obj.solicitarDatos()
    obj.calcularDistancia()
    

if __name__ == "__main__":
    main()