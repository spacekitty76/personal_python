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

role_ids = {}

def get_enterprise_app_roles(app_roles_req, counter):
    """Continuously check for app roles until propagated. This 
    is specifically for the AWS Single Sign On Enterprise application
    after you've turned on provisioning."""

    print(f"counter: {counter}")
    roles = ["stacy-walker-idp-anitian-devops-role,stacy-walker-idp-anitian-azad-saml-idp",
        "stacy-walker-idp-anitian-secops-admin-role,stacy-walker-idp-anitian-azad-saml-idp",
        "stacy-walker-idp-anitian-security-audit-role,stacy-walker-idp-anitian-azad-saml-idp"]
    for role in app_roles_req["appRoles"]:
        # print(f"role: {role}\n\n\n")
        # print(f"role description: {role['description']}")
        # print(f"aws role name: {props['aws_role_name']}")
        for name in roles:
            #     # TODO: lookit where my ifs are, this don't make sense
            if name == role["displayName"]:
                role_ids[role["displayName"]] = [role["id"], "anitian-secops-admin-group"]
                print(f"adding to dict: {role_ids}")
    # print(f"** len of role ids: {len(role_ids)}")
    # print(f"** len of group name: {len(props['az_group_names'])}")
    # if len(role_ids) < len(props["az_group_names"]) - 1 and counter <= 12:
    #     print(" ***** ALL GROUPS NOT ADDED *****")
    #     print("Waiting for roles to propagate...")
    #     time.sleep(10)
    #     counter += 1
    #     return wait_for_app_role(app_roles_req, counter)
    # if counter > 12:
    #     print("Couldn't get ids for all the groups")
    #     return
    return role_ids

# NOTE: Replace with your app
created_app_objId = "a6ca08d0-6d7c-403d-9bee-4b3901d61c20"
list_app_roles_req = requests.get(
    url=f"https://graph.microsoft.com/beta/servicePrincipals/{created_app_objId}/",
    headers=headers,
).json()
# role_dict = get_enterprise_app_roles(list_app_roles_req, 0)
# print(f"role dict: {role_dict}")
# print(list_app_roles_req)
print(f"app role req: {list_app_roles_req}")

# # Get groups
# group = "stacy-walker-idp-anitian-devops-role"
# get_groups = requests.get(
#     url=f"https://graph.microsoft.com/v1.0/groups?$filter=displayName eq '{group}'",
#     headers=headers,
# ).json()
# print(get_groups)
# group_id = get_groups["value"][0]["id"]
# group_name = get_groups["value"][0]["displayName"]
# print(f"group name: {group_name}")
# print(f"group response: {get_groups.content}")