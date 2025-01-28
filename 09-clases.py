class OperacionesBasicas:
    #Declaracion de propiedades
    num1 = 0 #Publico
    num2 = 0 #Privadas '_'
    res = 0 #Protegidas '__'

    #Declaracion de constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    #Declaracion de metodos
    def suma(self):
        self.res = self.num1 + self.num2
        print('La suma es: {}'.format(self.res))

    def resta(self):
        self.res = self.num1 + self.num2
        print('La resta es: {}'.format(self.res))

def main():
    obj = OperacionesBasicas(3, 4)
    obj.suma()

if __name__ == '__main__':
    main()