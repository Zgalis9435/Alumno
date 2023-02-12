class alumno():

    nombre= None
    nota=0

    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def getNota(self):
        return self.nota
    def getNombre(self):
        return self.nombre
    def isAproved(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        if(self.nota>=5):
            print(self.nombre,'esta aprovado con un', self.nota)
        else:
            print(self.nombre,'esta suspendido con un',self.nota)



alumno1=alumno('Manolo',4)
alumno1.isAproved(alumno1.getNombre(),alumno1.getNota())
alumno2=alumno('Manoli',8)
alumno2.isAproved(alumno2.getNombre(),alumno2.getNota())