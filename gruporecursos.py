from clases import Dependencia
from collections import defaultdict, OrderedDict
from funciones import ordenador
from recurso import Recurso
from resolvedor import resolvedor


class GrupoRecursos:

    def __init__(self):
        self.recursos = defaultdict(dict)
        self.dependencias = []

    def agregarDependencias(self, recurso, rjson):
        if "dependsOn" in rjson:
            for d in rjson["dependsOn"]:  # dependsOn contiene puro resourceId
                deps = resolvedor.resolver(d)
                for d in deps[1]:  # deps[0] es el tipo de los recursos
                    self.dependencias.append(Dependencia(recurso, deps[0], d))

    def agregarRecurso(self, rjson):
        recurso = Recurso(rjson)
        self.recursos[recurso.tipo][recurso.id] = recurso
        self.agregarDependencias(recurso, rjson)

    def generarMapa(self):
        print("generar mapa")

    def resolverDependencias(self):
        for dep in self.dependencias:
            if dep.tipoDependencia in self.recursos:
                res = self.recursos[dep.tipoDependencia]
                if dep.nombreDependencia in res:
                    dep.dependencia = res[dep.nombreDependencia]
                else:
                    print("no existe objeto " + dep.nombreDependencia)
            else:
                print("no existe tipo " + dep.tipoDependencia)

    def todosLosRecursos(self):
        todos = []
        for recdict in self.recursos.values():
            for rec in recdict.values():
                todos.append(rec)
        return todos
