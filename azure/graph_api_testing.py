import authentication_tokens as auth
from uuid import uuid4
import requests
import time

token = auth.get_sdk_token("https://graph.microsoft.com/.default")
# print(token)
headers = {
    "Authorization": "Bearer " + token,
    "x-ms-client-request-id": str(uuid4()),
    "x-ms-client-session-id": str(uuid4()),
}


provisioning_job_id = "aws.c55797bc397b4cf5b66dac3c5f3408c6.3230159b-1cba-4380-bf77-a1480836ba3d"
created_app_objId = "df8c5e6c-4a92-4955-8622-54f1eb97708a"
provisioning_progress_req = requests.get(
    url=f"https://graph.microsoft.com/beta/servicePrincipals/{created_app_objId}/synchronization/jobs/{provisioning_job_id}/",
    headers=headers,
).json()
print(provisioning_progress_req)

role_ids = {}

# def get_enterprise_app_roles(app_roles_req, counter):
#     """Continuously check for app roles until propagated. This 
#     is specifically for the AWS Single Sign On Enterprise application
#     after you've turned on provisioning."""

#     print(f"counter: {counter}")



# roles = ["stacy-walker-idp-anitian-devops-role,stacy-walker-idp-anitian-azad-saml-idp",
# "stacy-walker-idp-anitian-secops-admin-role,stacy-walker-idp-anitian-azad-saml-idp",
# "stacy-walker-idp-anitian-security-audit-role,stacy-walker-idp-anitian-azad-saml-idp"]

# role_dict = {'stacy-walker-idp-anitian-devops-role,stacy-walker-idp-anitian-azad-saml-idp': '4990f92f-47ce-44e4-8da4-ce8599bc3246', 'stacy-walker-idp-anitian-secops-admin-role,stacy-walker-idp-anitian-azad-saml-idp': '96c72212-da90-410b-a98b-d9d885832ab4', 'stacy-walker-idp-anitian-security-audit-role,stacy-walker-idp-anitian-azad-saml-idp': 'e346b69e-3ed5-44b9-a3cd-6642d36c1208'}
# # Remove everything after the comma to find just the group name
# for key in role_dict:
#     separator = ","
#     group_name = key.split(separator, 1)[0]
#     print(f"stripped role name: {group_name}")

# NOTE: Replace with your app
# created_app_objId = "df8c5e6c-4a92-4955-8622-54f1eb97708a"
# list_app_roles_req = requests.get(
#     url=f"https://graph.microsoft.com/beta/servicePrincipals/{created_app_objId}/",
#     headers=headers,
# ).json()
# print(list_app_roles_req)
# for role in list_app_roles_req["appRoles"]:
#     print(f"role in req: {role}\n\n")
#     for myrole in roles:
#         print(f"myroles: {myrole}\n")
#         if myrole == role["displayName"]:
#             print("they match. fuuuuck")


# for group in role_dict:
#     get_groups = requests.get(
#         url=f"https://graph.microsoft.com/v1.0/groups?$filter=displayName eq '{group}'",
#         headers=headers,
#     )
#     print(f"get groups: {get_groups.content}")
    # group_id = get_groups["value"][0]["id"]
    # print(f"role dict group: {role_dict[group]}")
    # requests.post(
    #     url=f"https://graph.microsoft.com/beta/servicePrincipals/{created_app_objId}/appRoleAssignedTo",
    #     headers=headers,
    #     json={"principalId": group_id, "resourceId": created_app_objId, "appRoleId": role_dict[group]},
    # )