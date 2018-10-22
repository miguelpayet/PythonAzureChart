from pares import orden


def GetValor(r, unTipo):
    if unTipo in r:
        return r[unTipo]
    else:
        return ""


def ordenador(x):
    if x in orden:
        return orden[x]
    else:
        return 98
