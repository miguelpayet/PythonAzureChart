from clases import Recurso
from gruporecursos import GrupoRecursos
from pathlib import Path
import json
import sys
from exclusiones import exclusiones

    
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
    file_directory = "D:\\WPy-3702\\PythonAzureChart\\template.json"
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
        if r["type"] not in exclusiones:
            recurso = None
            recurso = Recurso(r, parameters)
            grupo.agregarRecurso(recurso)
    grupo.crearArbol()
    grupo.generarVisio()
    print("bye")
    
    
if __name__ == '__main__':
    main()
