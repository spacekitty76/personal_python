import re 
import sys

# # check for spaces
# def checkforspaces(string):
#     space_search = bool(re.search(r"\s", string))
#     if space_search is True:
#         print(f"problem, you have a space")
#         sys.exit()
#     else:
#         print("seems good")
#     print("continuing the program")

# # checkforspaces("nospace")
# checkforspaces("have a space")

# check for only certain characters in a name
"""
The user’s name. The name must consist of upper and lowercase alphanumeric characters with no spaces.
You can also include any of the following characters: =,.@-_.. User names are not distinguished by case
"""
def validate_name(string):
    character_search = bool(re.search(r"^[a-zA-Z0-9_=,.@\-]+$", string))
    if character_search is True:
        print("looks good")
    else:
        print("nope")

# validate_name("this.is_my..Test,2340-94-430r5@98mc=")
validate_name("lkads230>84.=,")
