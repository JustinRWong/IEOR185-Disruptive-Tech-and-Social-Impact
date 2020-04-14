import json

TAB = "  "
def print_json(json_like, tabs=1):
    if hasattr(json_like, 'keys'):
        for key in json_like.keys():
            if type(json_like[key]) == dict:
                print(TAB*tabs + key + " : ")
                print_json(json_like[key], tabs+1)
            else:
                print(TAB*tabs + "> " + key + " : " + str(json_like[key]))
    else:
        print(json_like)
