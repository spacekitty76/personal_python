# role_perms = {"SecOpsAdmin": ["Stacy Walker", "Rando Guy"]}
role_perms = {"SecOpsAdmin": "Stacy Walker", "DevOps Admin": "Other thing"}

# for item in role_perms:
#     print(role_perms[item])


for key, value in role_perms.items():
    print(f"Key: {key}, Value: {value}")
    # print(f"Length of value: {len(value)}")

# print(f"len: {len(role_perms)}")

# print(role_perms)