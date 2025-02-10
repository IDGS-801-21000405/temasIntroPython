import os

class Cinepolis:
    nombreComprador = ''
    personas = 0
    boletos = 7
    boletosAsistentes = 0
    tarjetaCinepolis = False
    metodoPago = 0
    totalVenta = 0
    totalCorte = 0

    def limpiarPantalla(self):
        os.system('clear')

    def limpiarVariables(self):
        self.personas = 0
        self.boletos = 7
        self.boletosAsistentes = 0
        self.tarjetaCinepolis = False
        self.metodoPago = 0
        self.totalVenta = 0

    def menuPrincipal(self):
        self.limpiarPantalla()
        print('1. Comprar boletos.')
        print('2. Salir.')
        return int(input('Ingrese una opcion: '))
    
    def menuPago(self):
        self.limpiarPantalla()
        if self.nombreComprador == '':
            self.nombreComprador = input('Ingrese su nombre: ')
        self.personas = int(input('Cuántas personas asistirán?: '))
        self.boletosAsistentes = int(input('Cuántos boletos necesitan?: '))
        self.boletosPermitidos =  self.boletos * self.personas
        if self.boletosAsistentes <= self.boletosPermitidos:
            return [True]
        return [False, self.boletosPermitidos]
    
    def menuMetodosPago(self):
        self.limpiarPantalla()
        print('-- MÉTODOS DE PAGO --')
        print('1. Efectivo.')
        print('2. Tarjeta Cinepolis (10% descuento adicional).')
        self.metodoPago = int(input('Ingrese una opción: '))
        if self.metodoPago == 2:
            self.tarjetaCinepolis = True
        self.preCalculo()
        self.generarArchivo()
        return True

    def menuSecundario(self, respuesta):
        self.limpiarPantalla()
        print(f'Solamente puede comprar: {respuesta[1]} boletos!')
        print('1. Modificar asistentes.')
        print('2. Modificar boletos.')
        print('3. Salir.')
        return int(input('Ingrese una opcion: '))
    
    def preCalculo(self):
        total = self.boletosAsistentes * 12.0
        descuento = 0
        if self.boletosAsistentes > 5:
            descuento = 15
        elif 2 < self.boletosAsistentes <= 5:
            descuento = 10
        if self.metodoPago == 2:
            descuento += 10

        self.totalVenta = total - (total * descuento / 100)

    def calculaCosto(self):
        self.limpiarPantalla()
        total = self.boletosAsistentes * 12.0
        descuento = 0
        if self.boletosAsistentes > 5:
            descuento = 15
        elif 2 < self.boletosAsistentes <= 5:
            descuento = 10
        if self.metodoPago == 2:
            descuento += 10

        self.totalVenta = total - (total * descuento / 100)
        self.totalCorte = self.totalVenta
        print(f'Asistentes: {self.personas} - Boletos: {self.boletosAsistentes}')
        print(f'El total a pagar es: ${self.totalVenta:.2f}')
        print('1. Pagar y terminar.')
        print('2. Cancelar y salir.')

        opcion = int(input('Ingrese una opción: '))
        if opcion == 2:
            return False
        return True

    def modificarAsistentes(self):
        self.limpiarPantalla()
        self.personas = int(input('Cuántas personas asistirán?: '))

    def modificarBoletos(self):
        self.limpiarPantalla()
        self.boletosAsistentes = int(input('Cuántos boletos necesita?: '))

    def generarArchivo(self):
        texto = open('ticket.txt', 'a')
        texto.write(f'Comprador: {self.nombreComprador} - Total venta: ${self.totalVenta} \n')
        texto.write('------------------ \n')

    def asignarCorte(self):
        texto = open('ticket.txt', 'a')
        texto.write('------------------ \n')
        texto.write(f'Total corte: ${self.totalCorte} \n')
        texto.write('------------------ \n')

    def leerArchivo(self):
        texto = open('ticket.txt', 'r')
        lectura = texto.read()
        print(lectura)

    def calcularCorte(self):
        self.totalCorte = self.totalCorte + self.totalVenta
        self.asignarCorte()


    def finalizar(self):
        self.limpiarPantalla()
        print('-- RESUMEN DE VENTA -- \n')
        self.leerArchivo()
        print('\n')
        print('1. Hacer otra compra.')
        print('2. Finalizar')
        return int(input('Ingrese una opcion: '))

def eliminarArchivo():
    archivo = "ticket.txt"
    if os.path.exists(archivo):  
        os.remove(archivo) 

def run():
    continuar = True
    vueltas = 0
    eliminarArchivo()
    while (continuar == True):
        obj = Cinepolis()
        if obj.menuPrincipal() == 2:
            return
        respuesta = obj.menuPago()
        if respuesta[0] is False:
            opcion = obj.menuSecundario(respuesta)
            match opcion:
                case 1:
                    obj.modificarAsistentes()
                case 2:
                    obj.modificarBoletos()
                case 3:
                    obj.eliminarArchivo()
                    return
            obj.menuMetodosPago()
            if obj.calculaCosto() == False:
                return
            if obj.finalizar() == 2:
                obj.calcularCorte()
                continuar = False
                return
        else:
            obj.menuMetodosPago()
            obj.calculaCosto()
            if obj.finalizar() == 2:
                continuar = False
                obj.calcularCorte()
                return
            vueltas = vueltas + 1

if __name__ == '__main__':
    run()