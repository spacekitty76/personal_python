import os
import logging
from msal import ConfidentialClientApplication
import azure.identity
from typing import Union
from uuid import uuid4
import requests

# NOTE: you have to export some stuff to your shell variables for this to work
"""
export ARM_CLIENT_ID="" \
export ARM_CLIENT_SECRET="" \
export ARM_TENANT_ID=""
"""

# MSAL library. Used it for Graph Api
def assume_graph_role(sp_app_id: str = None, sp_secret: str = None, sp_tenant: str = None, set_env: bool = False) -> dict:
    """Assume a role for a given account using a service principal for graph-api.

    Args:
        sp_app_id (str, optional): The App Id of the service principal.
        sp_secret (str, optional): The service principal secret.
        sp_tenant (str, optional): The tenant of the service principal.
        set_env (bool, optional): Set to true if you want to overwrite the Azure.
            environment variables. Defaults to False.

    Returns:
        token: msal token object
    """
    sp_app_id = os.environ.get("ARM_CLIENT_ID")
    sp_secret = os.environ.get("ARM_CLIENT_SECRET")
    sp_tenant = os.environ.get("ARM_TENANT_ID")
    scope = "https://graph.microsoft.com/.default"
    app = ConfidentialClientApplication(client_id=sp_app_id, client_credential=sp_secret, authority=f"https://login.microsoftonline.com/{sp_tenant}")
    token = app.acquire_token_for_client(scopes=scope)
    if "access_token" in token:
        print(f"{token['token_type']}\n")
    else:
        print(f"{token.get('error')}\n")
        print(f"{token.get('error_description')}\n")
        print(f"{token.get('correlation_id')}\n")  # You might need this when reporting a bug.
    return token

# graph_token = assume_graph_role()
# print(graph_token)


# SDK to get credentials. Can also be used to auth to the graph api. But you have to use .get_token()
  # wehreas MSAL above just returns you the token
def get_sdk_credential(
    client_id: str = None, client_secret: str = None, tenant_id: str = None
) -> Union[azure.identity.ClientSecretCredential, azure.identity.AzureCliCredential]:
    """Generate and return the object for Azure SDK.

        The order of precedence is as follows.
        1. If params are passed in explicitly they will be used.
        2. If a param is missing, it will be looked up in the env i.e. ARM_CLIENT_ID.
        3. If not all params (client id, secret and tenant id) are either passed in,
           or found in the env this will attempt to fall back to the az cli logged in user and tenant.

    Args:
        client_id (str, optional): Explicitily call out the client_id to use.
        client_secret (str, optional): Explicitily call out the client_secret to use.
        tenant_id (str, optional): Explicitily call out the tenant_id to use.

    Returns:
        Union[azure.identity.ClientSecretCredential, azure.identity.AzureCliCredential]: The credential object.
    """
    # Get the credentials from the provider, or the environment
    client_id = client_id if client_id else os.getenv("ARM_CLIENT_ID", None)
    client_secret = client_secret if client_secret else os.getenv("ARM_CLIENT_SECRET", None)
    tenant_id = tenant_id if tenant_id else os.getenv("ARM_TENANT_ID", None)

    # Create the credential object from either client details or the AZ CLI
    if all([client_id, client_secret, tenant_id]):
        print(f"Using client credentials client: {client_id}, tenant: {tenant_id}")
        credential = azure.identity.ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)
    else:
        print("Using Azure CLI Credentials since all(client_id, client_secret and tenant_id) evaluated false")
        credential = azure.identity.AzureCliCredential()

    return credential

sdk_cred = get_sdk_credential(client_id="", client_secret="", tenant_id="")
# print(sdk_cred)
token = sdk_cred.get_token("https://graph.microsoft.com/.default")
# print(token[0])

def get_sdk_token(scope: str, client_id: str = None, client_secret: str = None, tenant_id: str = None):
    """Return the token from the sdk_credential.

    Args:
        client_id (str, optional): Explicitily call out the client_id to use.
        client_secret (str, optional): Explicitily call out the client_secret to use.
        tenant_id (str, optional): Explicitily call out the tenant_id to use.
        scope (str, required): Scope for the token's authentication.
            Example: "https://graph.microsoft.com/.default"

    Returns:
        str: The authorization token as a string
    """
    return get_sdk_credential(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id).get_token(scope).token
