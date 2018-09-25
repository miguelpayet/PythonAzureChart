def CalcularNombre(n, parameters):
    nombre = LimpiarNombre(n)
    valor = eval(nombre)
    tipo = type(valor).__name__
    cadena = ""
    if tipo == "dict":
        if "defaultValue" in valor:
            cadena = valor["defaultValue"]
    elif tipo == "str":
        cadena = valor
    return cadena


def concat(*args):
    cadena = ""
    for arg in args:
        tipo = type(arg).__name__
        if tipo == "dict":
            if "defaultValue" in arg:
                cadena = cadena + arg["defaultValue"]
        elif tipo == "str":
            cadena = cadena + arg
    return cadena
    

def LimpiarNombre(nombre):
    nombre = nombre[1:len(nombre) - 1]
    nombre = nombre.replace("(", "[")
    nombre = nombre.replace(")", "]")
    nombre = nombre.replace("'", "\'")
    cadenas = ["concat", "resourceId"]
    for c in cadenas:
        l = len(c)
        if nombre[0:l] == c:
            return nombre[0:l] + "(" + nombre[l + 1:len(nombre) - 1] + ")"
    return nombre


def resourceId(*args):
    resultado = []
    tipo = args[0]
    for i in range(1, len(args)):
        resultado.append(args[i]["defaultValue"])
    return (tipo, resultado)
    

def SetValor(r, unTipo):
    if unTipo in r:
        return r[unTipo]
    else:
        return ""