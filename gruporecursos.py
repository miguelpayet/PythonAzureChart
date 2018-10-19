from visio import Visio        
from collections import  defaultdict, OrderedDict

class Dependencia:

    def __init__(self, t, n):
        self.tipo = t
        self.nombre = n

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.nombre + " (" + self.tipo + ")"


class GrupoRecursos:

    def __init__(self):
        self.recursos = defaultdict(dict)

    def agregarRecurso(self, recurso):
        self.recursos[recurso.tipo][recurso.id] = recurso

    def crearArbol(self):
        print ("--------------")
        llaves = list(self.recursos.keys()).sort()
        print(llaves)
        for tipo, recursos in self.recursos.items():
            print(tipo)
            for k,v in recursos.items():
                print('-> ', k)
                for d in v.dependencias:
                    if d.tipo in self.recursos:
                        if d.nombre in self.recursos[d.tipo]:
                            self.recursos[d.tipo][d.nombre].agregarDependiente(v)
                        else:
                            pass #print ("error de nombre que no existe ", ' -> ', d)
                    else:
                        pass #print ("error de tipo que no existe ", ' -> ', d)
        print ("--------------")

    def generarVisio(self):
        visio = Visio()
        x = 1
        visio.resetY()
        visio.agregarPagina("recursos sin agrupar")
        for r in self.recursosSinHijos():
            item = visio.obtenerShape(r.tipo)
            if item is not None:
                visio.dropShape(item, x, visio.y, r.displayName)
                visio.y -= 0.9
            else:
                print ("gráfico no existe para recurso ", r.tipo)            
            if visio.y < 0:
                x += 2
                visio.resetY()
        for r in self.recursosConHijos():
                visio.resetY()
                visio.agregarPagina(r.nombre)
                r.dibujar(visio, 1, 0)
                
    def recursosConHijos(self):
        todos = self.todosLosRecursos()
        todosConHijos = []
        for r in todos:
            if r.totalDependencias() == 0 and r.totalDependientes() > 0: 
                todosConHijos.append(r)
        return todosConHijos
    
    def recursosSinHijos(self):
        todos = self.todosLosRecursos()
        todosSinHijos = []
        for r in todos:
            if r.totalDependencias() == 0 and r.totalDependientes() == 0: 
                todosSinHijos.append(r)
        return todosSinHijos
    
    def todosLosRecursos(self):
        todos = []
        for recdict in self.recursos.values():
            for rec in recdict.values():
                todos.append(rec)
        return todos
