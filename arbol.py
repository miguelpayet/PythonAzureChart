from collections import OrderedDict

from asciitree import LeftAligned


class Nodo:

    def __init__(self, padre, hijo=None):
        self.padre = padre
        self.hijos = []
        self.nombre = padre.__str__()
        self.esHijo = False
        if hijo is not None:
            self.hijos.append(hijo)

    def __str__(self):
        return self.padre.__str__()

    def addhijo(self, rec):
        self.hijos.append(rec)

    def creardict(self, arbol):
        lista = OrderedDict()
        if len(self.hijos) == 0:
            lista[self.__str__()] = {}
            arbol[self.__str__()] = lista
        else:
            for hijo in self.hijos:
                hijo.creardict(lista)
                arbol[self.__str__()] = lista


class Arbol:

    def __init__(self, gruporecursos):
        self.gruporecursos = gruporecursos
        self.nodos = []
        self.mainnode = None
        self.crearnodoprincipal()
        self.crearnodos()

    def crearnodoprincipal(self):
        self.mainnode = Nodo("principal", None)
        self.mainnode.nombre = "principal"

    def crearnodos(self):
        for rec in self.gruporecursos.listarecursos():
            self.nodos.append(Nodo(rec))
        for dep in self.gruporecursos.dependencias:
            # ignorar las relaciones donde el availability set depende de la vm
            if dep.dependencia is not None and dep.dependencia.tipo == "Microsoft.Compute/availabilitySets":
                if dep.recurso.tipo == "Microsoft.Compute/virtualMachines":
                    continue
            # encontrar el nodo donde la dependencia es el padre
            nodopadre = self.encontrarnodo(dep.dependencia)
            if nodopadre is None:
                print("warning nodo padre no encontrado para ", dep)
                continue
            # encontrar el nodo donde el recurso hijo es el padre
            nodohijo = self.encontrarnodo(dep.recurso)
            if nodohijo is None:
                print("warning nodo hijo no encontrado para ", dep)
                continue
            # añadir el hijo
            nodopadre.addhijo(nodohijo)
            nodohijo.esHijo = True
        for nod in self.nodos:
            if not nod.esHijo:
                self.mainnode.addhijo(nod)

    def encontrarnodo(self, rec):
        foundnode = None
        for n in self.nodos:
            if n.padre == rec:
                foundnode = n
                break
        return foundnode

    def imprimir(self):
        dictarbol = OrderedDict()
        self.mainnode.creardict(dictarbol)
        tr = LeftAligned()
        print(tr(dictarbol))
