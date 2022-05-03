import json
import re

policy = json.dumps(
    {
        "name": "BUCKET_ARN",
        "account": "ACCOUNT"
    }
)

# replacement_string = "stacy"

# def replacer(policy, replacement_string):
#     return policy.replace("BUCKET_ARN", replacement_string)

# new_dump = replacer(policy=policy, replacement_string=replacement_string)
# print(new_dump)

rep1 = re.sub("BUCKET_ARN", "new_arn", policy)
rep2 = re.sub("ACCOUNT", "new_account", rep1)

print(rep2)