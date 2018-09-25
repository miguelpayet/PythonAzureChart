# PythonAzureChart

This program uses Python to create a diagram of an Azure resource group deployment script on a Visio document. 

Visio 2013 standard, 32 bit Python 3.x for Windows and the 32 bit version of win32com were used when this program was created.

Visio must be open before running this program. Open Visio, select NEW then select "Basic Diagram".  

The Azure stencil that is available at [https://www.microsoft.com/en-us/download/details.aspx?id=41937](https://www.microsoft.com/en-us/download/details.aspx?id=41937) must be installed. This is a zip file that contains CnE_CloudV2.7.vss, which has to be copied to your "My Shapes" folder.

You obtain the Azure deployment script for a resource group by going into the Azure Portal, selecting a Resource Group, and choosing Automation Script on the options panel. When you download that, you have to extract the template.json file and give that as an argument to the graficador.py script.

The template.json maps the dependency relationships between the resource group components. The program will create a Visio page for each root resource (one which depends on no other resources) and map in in a tree-like fashion with its dependencies. 

Root resources which have no dependencies will appear grouped in the first page.

This is a preliminary version that is riddled with hardcoded variables, testing stuff, and code smells. Over time it should clean up real nice.
