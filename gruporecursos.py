from collections import defaultdict

from clases import Dependencia
from recurso import Recurso
from resolvedor import resolvedor


class GrupoRecursos:

    def __init__(self):
        self.recursos = defaultdict()
        self.dependencias = []

    def agregardependencias(self, recurso, rjson):
        if "dependsOn" in rjson:
            for rawdep in rjson["dependsOn"]:  # dependsOn contiene puro resourceId
                resolveddep = resolvedor.resolver(rawdep)
                for dep in resolveddep[1]:  # deps[0] es el tipo de los recursos
                    self.dependencias.append(Dependencia(recurso, resolveddep[0], dep))

    def agregarrecurso(self, rjson):
        recurso = Recurso(rjson)
        self.recursos[recurso.tipo, recurso.id] = recurso
        self.agregardependencias(recurso, rjson)

    def resolverdependencias(self):
        for dep in self.dependencias:
            t = (dep.tipoDependencia, dep.nombreDependencia)
            if t in self.recursos:
                dep.dependencia = self.recursos[t]
            else:
                print("no existe recurso ", t)

    def listarecursos(self):
        todos = []
        for rec in self.recursos.values():
            todos.append(rec)
        return todos
