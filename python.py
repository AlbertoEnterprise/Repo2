from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

def list_resource_groups():
    # Inicializa las credenciales de Azure utilizando la identidad predeterminada
    credential = DefaultAzureCredential()

    # Crea un cliente de administración de recursos de Azure
    resource_client = ResourceManagementClient(credential, "<tu_id_de_suscripción>")

    print("Listado de Grupos de Recursos en la suscripción:")
    for resource_group in resource_client.resource_groups.list():
        print(f"- {resource_group.name}")

def create_resource_group(group_name, location):
    # Inicializa las credenciales de Azure utilizando la identidad predeterminada
    credential = DefaultAzureCredential()

    # Crea un cliente de administración de recursos de Azure
    resource_client = ResourceManagementClient(credential, "<tu_id_de_suscripción>")

    print(f"Creando Grupo de Recursos '{group_name}' en la ubicación '{location}'...")
    resource_client.resource_groups.create_or_update(
        group_name,
        {
            'location': location
        }
    )
    print("Grupo de Recursos creado correctamente.")

if __name__ == "__main__":
    # Lista los grupos de recursos existentes
    list_resource_groups()

    # Crea un nuevo grupo de recursos
    new_group_name = "nuevo-grupo-de-recursos"
    new_group_location = "eastus"
    create_resource_group(new_group_name, new_group_location)
