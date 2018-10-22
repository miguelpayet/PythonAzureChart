˘from clases import SKU
from collections import OrderedDict
from funciones import GetValor
from resolvedor import resolvedor


class Recurso:

    def __init__(self, r):
        self.apiVersion = ""
        self.displayName = ""
        self.id = ""
        self.nivel = 0
        self.nombre = ""
        self.sku = ""
        self.tipo = ""
        self.vmSize = ""
        self.setNombre(r)
        self.setTipo(r)
        self.setApiVersion(r)
        self.setVmSize(r)
        self.setDisplayName(r)

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __gt__(self, other):
        return self.__str__() > other.__str__()

    def __lt__(self, other):
        return self.__str__() < other.__str__()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.nombre + " (" + self.tipo + ")"

    def calcularNombre(self, n):
        cadena = resolvedor.resolver(n)
        return cadena

    def nombreAbreviado(self):
        lista = self.tipo.rpartition("/")
        nombre = self.nombre + " (" + lista[2] + ")"
        return nombre

    def setApiVersion(self, r):
        self.apiVersion = GetValor(r, "apiVersion")

    def setDisplayName(self, r):
        valor = self.__str__()
        if "properties" in r:
            if "displayName" in r["properties"]:
                valor = r["properties"]["displayName"]
        return valor

    def setNombre(self, r):
        self.nombre = self.calcularNombre(r["name"])
        lista = self.nombre.rpartition("/")
        self.id = lista[2]

    def setSKU(self, r):
        if "sku" in r:
            sku = r["sku"]
            self.sku = SKU()
            self.sku.name = GetValor(sku, "name")
            self.sku.capacity = GetValor(sku, "capacity")
            self.sku.tier = GetValor(sku, "tier")
        else:
            self.sku = None

    def setTipo(self, r):
        self.tipo = GetValor(r, "type")

    def setVmSize(self, r):
        self.vmSize = ""
        if "properties" in r:
            if "hardwareProfile" in r["properties"]:
                if "vmSize" in r["properties"]["hardwareProfile"]:
                    self.vmSize = r["properties"]["hardwareProfile"]["vmSize"]
