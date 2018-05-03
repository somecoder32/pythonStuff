from pymongo import MongoClient
from bson import Binary, Code
from bson.json_util import dumps
import json
import pprint


try:
    client = MongoClient('mongodb://dndplayer:IRoll20@ds036967.mlab.com:36967/dndmain')

    db = client['dndmain']

    spellCollection = db['spells']

    # pprint.pprint(posts.find_one({"name": "Fireball"}))
    print(spellCollection.count())
    # pprint.pprint(spellCollection.find_one({"name": "Fireball"}))
    result = spellCollection.find_one({ "name": "Fireball"})
    # pprint.pprint(result)
    dumped = dumps(result)
    print(json.loads(dumped)['name'] + "\n" +  json.loads(dumped)['description'])
except:
    print('Error')