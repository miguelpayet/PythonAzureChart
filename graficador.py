from clases import Recurso, GrupoRecursos
from pathlib import Path
import json
import sys
from visio import Visio

def GenerarVisio(grupo):
    visio = Visio()
    x = 1
    visio.resetY()
    visio.agregarPagina("recursos sin agrupar")
    for r in grupo.recursosSinHijos():
        item = visio.obtenerShape(r.tipo)
        if item is not None:
            visio.dropShape(item, x, visio.y, r.nombreAbreviado())
            visio.y -= 0.9
        else:
            print ("gráfico no existe para recurso ", r.tipo)            
        if visio.y < 0:
            x += 2
            visio.resetY()
    for r in grupo.recursosConHijos():
            visio.resetY()
            visio.agregarPagina(r.nombre)
            r.dibujar(visio, 1, 0)
    print("fin")
    
def main():

    if len(sys.argv) == 1:
        print("no especificaste archivo")
        return -1
    file_directory = ""
    if len(sys.argv) > 1:
        file_directory = sys.argv[1]
        if file_directory == "":
            print("archivo en blanco?")
            return -1
    #file_directory = "D:\\WPy-3702\\PythonAzureChart\\template.json"
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
    GenerarVisio(grupo)
    
    
if __name__ == '__main__':
    main()