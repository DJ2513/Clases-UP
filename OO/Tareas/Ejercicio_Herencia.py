class Empresa():
    def __init__(self,nombre):
        self.nombre=nombre
        self.salario = 0
        print('Bienvenid@! '+ self.nombre)
    def empleo(self):
        print('Lo siento ese empleo no es correcto')

class Gerente(Empresa):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.salario = 50000
        
    def salario_base(self):
        print (self.nombre +' tu salario es de $' + str(self.salario))
    def trabajo(self):
        print('Soy el gerente')
    
    def cambiar_salario(self, empleado, monto):
        if(type(empleado) != Gerente):
            empleado.salario = monto
    
class Programador(Empresa):
    def __init__(self, nombre):
        self.nombre = nombre
        self.salario = 25000

    def salario_base(self):
        print ('Tu salario inicial $' + str(self.salario))

    def trabajo(self):
        print('Yo soy programador y me encargo de programar')
class Secretaria(Empresa):
    def __init__(self, nombre):
        self.nombre = nombre
        self.salario = 15000

    def salario_base(self):
        print ('Tu salario inicial es de $' + str(self.salario))
    def trabajo(self):
        print('Yo soy la secretaria y estoy a tus servicios')



Paco= Gerente("Paco")
Paco.salario_base()
Paco.trabajo()

Pedro= Programador('Pedro')
Pedro.salario_base()
Pedro.trabajo()

Laura= Secretaria('Laura')
Laura.salario_base()
Laura.trabajo()

Paco.cambiar_salario(Pedro, 100000)
Pedro.salario_base()









