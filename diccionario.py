class Diccionario:
    
    def __init__(self):
        self.d = {"Microsoft.Compute/availabilitySets": "Availability set",
                 "Microsoft.Compute/virtualMachines": "Virtual machine",
                 "Microsoft.Network/loadBalancers":	"Azure load balancer",
                 "Microsoft.Network/networkSecurityGroups":	"NSG",
                 "Microsoft.Sql/servers": "Azure SQL database",
                 "Microsoft.Sql/servers/databases": "SQL database (generic)",
                 "Microsoft.Storage/storageAccounts": "Storage",
                 "Microsoft.Web/sites": "Web App (was websites)",}

    def resolver(self, tipo):
        if tipo in self.d:
            value = self.d[tipo]
            return value
        else:
            return "Unidentified feature object"
