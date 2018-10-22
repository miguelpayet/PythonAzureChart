class Dependencia:

    def __init__(self, recurso, tipodep, nombredep):
        self.recurso = recurso
        self.dependencia = None
        self.tipoDependencia = tipodep
        self.nombreDependencia = nombredep

    def __str__(self):
        return self.recurso.__str__()


class SKU:

    name = ""
    capacity = ""
    tier = ""
