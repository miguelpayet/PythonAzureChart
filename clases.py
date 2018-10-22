class Dependencia:

    def __init__(self, recurso, tipoDep, nombreDep):
        self.recurso = recurso
        self.dependencia = None
        self.tipoDependencia = tipoDep
        self.nombreDependencia = nombreDep


class Nodo:

    def __init__(self):
        self.recurso = None
        self.dependsOn = []


class SKU:

    name = ""
    capacity = ""
    tier = ""
