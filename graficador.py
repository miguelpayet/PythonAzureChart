#from asciitree import LeftAligned
from clases import Recurso, GrupoRecursos
#from collections import OrderedDict
from pathlib import Path
import json
import sys
from visio import Visio

def GenerarVisio(grupo):
    visio = Visio()
    for r in grupo.todosLosRecursos():
        if r.totalDependencias() == 0: #r.nombre == "Ibjbossprd0100ip": #BLNCOTPRD0100": # # and 
            visio.resetY()
            visio.agregarPagina(r.nombre)
            r.dibujar(visio, 1, 0)
    print("fin")
    
def main():

    if len(sys.argv) == 1:
        print("no especificaste archivo")
        #return -1
    file_directory = ""
    if len(sys.argv) > 1:
        file_directory = sys.argv[1]
        if file_directory == "":
            print("archivo en blanco?")
            #return -1
    file_directory = "D:\\WPy-3702\\graficador\\template.json"
    file_path = Path(file_directory)
    if not file_path.is_file():
        print("archivo no existe")
        return -1

    totalRecursos = 0

    json_data = open(file_directory).read()

    data = json.loads(json_data)
    parameters = data["parameters"]

    grupo = GrupoRecursos()
    for r in data["resources"]:
        totalRecursos += 1
        recurso = None
        recurso = Recurso(r, parameters)
        grupo.agregarRecurso(recurso)

    grupo.crearArbol()
    '''
    arbol = OrderedDict()
    todos = sorted(grupo.todosLosRecursos())
    for r in todos:
        if r.totalDependencias() == 0:
            arbol[r.__str__()] = r.obtenerArbol(r)
    arbolprint = OrderedDict()
    arbolprint["rg"] = arbol
    tr = LeftAligned()
    #print(tr(arbolprint))        
    '''
    
    GenerarVisio(grupo)
    
    
if __name__ == '__main__':
    main()