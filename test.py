import ast
from pprint import pprint

class FuncLister(ast.NodeVisitor):
    
    def visit_Call(self, node):
        print(node.func.id)
        for c in node.args:
            if type(c).__name__ == "Call":
                print(c.func.id)
                for c1 in c.args:
                    if type(c1).__name__ == "Str":
                        print(c1.s)                    
            elif type(c).__name__ == "Str":
                print(c.s)
        


print("hola")
test = "concat(parameters('service_apimgmtscuportalesprd01_name'), '/', parameters('apis_prodportalesofertaapi_name'), '/', parameters('operations_listarcoberturas_name'))"
tree = ast.parse(test, filename='<unknown>', mode='eval')
FuncLister().generic_visit(tree)
print("bye")

