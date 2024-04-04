import json

my_json = {
    'a': 'b'
}

# with open(args.config, "r") as config_file:
with open("abc.json", "r") as infile:
    users = json.load(infile)
# return indent here as we've already loaded the file
#     print(users)
    for user in users:
        print(user)