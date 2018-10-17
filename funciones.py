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