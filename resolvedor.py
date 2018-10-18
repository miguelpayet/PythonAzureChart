import ast
import re 

class Visitador(ast.NodeVisitor):
    
    def __init__(self, parametros):
        self.parametros = parametros
        self.result = None
        
    def resolver(self, node):      
        if type(node).__name__ == "Call":
            resolved_args = []
            for arg in node.args:
                resolved_args.append(self.resolver(arg))
            if node.func.id == "concat":
                cadena = ''.join(resolved_args)
                return cadena
            elif node.func.id == "parameters":
                cadena = resolved_args[0]                    
                if resolved_args[0] in self.parametros:
                    if "defaultValue" in self.parametros[resolved_args[0]]:
                        if self.parametros[resolved_args[0]]["defaultValue"] is None:
                            m = re.search("^[^_]+_(.+)_[^_]+$", cadena)
                            if m: 
                                cadena = m.group(1)
                        else:
                            cadena = self.parametros[resolved_args[0]]["defaultValue"]
                return cadena
            elif node.func.id == "resourceId":
                return (resolved_args[0], resolved_args[1:])
        elif type(node).__name__ == "Str":
            return node.s
     
    def visit_Call(self, node):
        self.result = self.resolver(node)
   
        
class Resolvedor:
    
    def __init__(self, parametros):
        self.parametros = parametros
        self.visitador = Visitador(parametros)

    def resolver(self, formula):
        tree = ast.parse(formula, filename='<unknown>', mode='eval')
        self.visitador.generic_visit(tree)
        return self.visitador.result
    
    
        
        
#print("hola")
#json_data = open("D:\WPy-3702\PythonAzureChart\portales.json").read()
#data = json.loads(json_data)
#parameters = data["parameters"]
#test = "Echo API"
#r = Resolvedor(parameters)
#res = r.resolver(test)
#print (res)
#print("bye")
