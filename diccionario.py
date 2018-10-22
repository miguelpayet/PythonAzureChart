class Diccionario:

    def __init__(self):
        self.d = {'Microsoft.ApiManagement/service': 'API Management',
                  'Microsoft.Cdn/profiles/endpoints': 'Content Delivery Network (CDN)',
                  'Microsoft.Cdn/profiles/endpoints/origins': 'Content Delivery Network (CDN)',
                  'Microsoft.Cdn/profiles': 'Content Delivery Network (CDN)',
                  'Microsoft.Compute/availabilitySets': 'Availability set',
                  'Microsoft.Compute/virtualMachines': 'Virtual machine',
                  'microsoft.insights/actionGroups': 'Application Insights',
                  'microsoft.insights/alertrules': 'Application Insights',
                  'microsoft.insights/components': 'Application Insights',
                  'microsoft.insights/webtests': 'Application Insights',
                  'Microsoft.KeyVault/vaults': 'Key Vault',
                  'Microsoft.Network/applicationGateways': 'Application Gateway (New)',
                  'Microsoft.Network/loadBalancers': 'Azure load balancer',
                  'Microsoft.Network/networkSecurityGroups': 'NSG',
                  'Microsoft.Network/virtualNetworkGateways': 'Azure VPN Gateway',
                  'Microsoft.RecoveryServices/vaults': 'Backup or Recovery Vault',
                  'Microsoft.Sql/servers': 'Azure SQL database',
                  'Microsoft.Sql/servers/databases': 'SQL database (generic)',
                  'Microsoft.Storage/storageAccounts': 'Storage',
                  'Microsoft.Web/sites': 'Web App (was websites)',
                  }

    def resolver(self, tipo):
        if tipo in self.d:
            value = self.d[tipo]
            return value
        else:
            return "Unidentified feature object"
