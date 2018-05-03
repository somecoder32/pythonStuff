import json
import operator

myjson = '{"names":[{"name":"Jason"},{"name":"Geo"}]}'

mylist = json.loads(myjson)["names"]

mylist = sorted(mylist, key=lambda k: k["name"])

print(mylist)