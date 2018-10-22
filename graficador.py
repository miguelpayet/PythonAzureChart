from exclusiones import exclusiones
from funciones import GetValor
from gruporecursos import GrupoRecursos
from pathlib import Path
from resolvedor import resolvedor
import json
import sys

def main():

    if len(sys.argv) == 1:
        print("no especificaste archivo")
        #return -1
    file_directory = ""
    if len(sys.argv) > 1:
        file_directory = sys.argv[1]
        if file_directory == "":
            print("archivo en blanco?")
            return -1
    file_directory = "./template.json"
    file_path = Path(file_directory)
    if not file_path.is_file():
        print("archivo no existe")
        return -1

    json_data = open(file_directory, encoding='latin-1').read()
    data = json.loads(json_data)
    parameters = data["parameters"]

    resolvedor.setParametros(parameters)
    grupo = GrupoRecursos()
    for r in data["resources"]:
        if GetValor(r, "type") not in exclusiones:
            grupo.agregarRecurso(r)
    grupo.resolverDependencias()
    #grupo.crearArbol()
    ##grupo.generarVisio()
    #grupo.generarArbol()
    print("bye")
    
    
if __name__ == '__main__':
    main()
