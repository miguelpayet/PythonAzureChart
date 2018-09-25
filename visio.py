import win32com.client
from diccionario import Diccionario

visCharacterColor  = 1
visCharacterFont = 0
visSectionCharacter = 3
visCharacterSize = 7
visCharacterDblUnderline = 8
visSectionFirstComponent = 10
visSectionObject =  1 
visRowPrintProperties =  25 
visPrintPropertiesPageOrientation =  16 
visRowPage =  10 
visPageWidth =  0 
visPageHeight =  1 
visOpenDocked =	4
visInches = 65
visPaperSizeA4 = 9

class Visio:
    
    def __init__(self):
        self.visio = win32com.client.Dispatch("Visio.Application")
        self.stencil = self.agregarStencil("CnE_CloudV2.7.vss")
        FlowchartTemplateName = "Basic Flowchart.vst"
        self.visioDoc = self.visio.Documents.Add(FlowchartTemplateName)
        self.page = None
        self.pageHeight = self.visioDoc.PaperHeight(visInches)
        self.pageWidth = self.visioDoc.PaperWidth(visInches) - 2
        self.stencilDict = Diccionario()
        self.resetY()   
        
    def agregarPagina(self, nombre):
        if self.page is None:
            self.page = self.visioDoc.Pages.Item(1)
        else:
            self.page = self.visioDoc.Pages.Add()
        self.setLandscape()
        self.page.Name = nombre
        self.visio.Application.ActiveWindow.Zoom = 0.8
        
    def agregarStencil(self, FlowchartStencilName): # Name of Visio stencil containing shapes
        visioStencil = self.visio.Documents.OpenEx(FlowchartStencilName, visOpenDocked);
        return visioStencil  
             
    # Place a Visio shape on the Visio document
    def dropShape (self, shapeType, posX, posY, theText):
        vsoShape = self.page.Drop(shapeType, posX, posY)
        vsoShape.Text = theText
        return vsoShape   # Returns the shape that was created

    def enumerarShapes(self):
        print(self.visio.ActiveDocument)
        for master in self.visio.ActiveDocument.Masters:
            print(master.Name)

    def obtenerShape(self, nombre):
        try:
            shapeName = self.stencilDict.resolver(nombre)
            item = self.stencil.Masters.ItemU(shapeName)
        except:
            item = None
        return item
    
    def printShortcuts(self, FlowchartStencilName):
        vsoStencil = self.visio.Documents.add(FlowchartStencilName)
        vsoMasterShortcuts = vsoStencil.MasterShortcuts
        for short in vsoMasterShortcuts:
            print (short.Name)
        
    def resetY(self):
        self.y = self.pageWidth   
        
    # Get the stencil object
    def setDefaultShapeValues(self, vsoShape):
        vsoShape.Cells("LineColor").FormulaU = 0
        vsoShape.Cells("LineWeight").FormulaU = "2.0 pt"
        vsoShape.FillStyle  = "None"
        vsoShape.Cells("Char.size").FormulaU = "12 pt"
        vsoShape.CellsSRC(visSectionCharacter, 0, visCharacterDblUnderline).FormulaU = False
        vsoShape.CellsSRC(visSectionCharacter, 0, visCharacterColor).FormulaU = "THEMEGUARD(RGB(0,0,0))"
        vsoShape.CellsSRC(visSectionCharacter, 0, visCharacterFont).FormulaU = 100
        return vsoShape
        
    def setLandscape(self):
        # Change page from landscape to portrait but this works sometimes
        self.visio.Application.ActiveWindow.Page.PageSheet.CellsSRC(visSectionObject, visRowPrintProperties, visPrintPropertiesPageOrientation).FormulaForceU = "0"
        self.visio.Application.ActiveWindow.Page.PageSheet.CellsSRC(visSectionObject, visRowPage, visPageWidth).FormulaU = "8.5 in"
        self.visio.Application.ActiveWindow.Page.PageSheet.CellsSRC(visSectionObject, visRowPage, visPageHeight).FormulaU = "11 in"
