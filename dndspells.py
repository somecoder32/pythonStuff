from pymongo import MongoClient
from bson import Binary, Code
from bson.json_util import dumps
from flask import Flask, request, render_template
import json
import operator

class dbInfo:
    strClient = 'mongodb://dndplayer:IRoll20@ds036967.mlab.com:36967/dndmain'

client = MongoClient(dbInfo.strClient)

db = client['dndmain']

    

def getSpellsByLevel(casterClass, spellLevel):
    try:    
        spellCollection = db['spells']

        print(casterClass + ' ' + str(spellLevel))
        result = spellCollection.find({ casterClass: int(spellLevel)}, { "name": 1, "_id":False})

        dumped = dumps(result)
        return dumped

    except:
        print("Error in SpellsByLevel")


def getSpell(spellName):
    try:
        spellCollection = db['spells']

        result = spellCollection.find_one({ "name": spellName}, { "full_text":False, "description":False})

        dumped = dumps(result)
        return dumped
    except:
        print('Error')


def getSpellsHTML(casterClass, spellLevel):
    try:
        spellCollection = db['spells']

        result = spellCollection.find({ casterClass: int(spellLevel)}, { "name": 1, "description": 1, "_id":False})

        dumped = dumps(result)

        jsondump = json.loads(dumped)

        sortedlist = sorted(jsondump, key=lambda k: k["name"])

        # newlist = ""

        # for s in sortedlist:
        #     newlist += "<div class='card'><h3 class='title'>" + s["name"] + "</h3>" + s["description_formated"] + "</div>"

        return sortedlist
    except:
        return dumps({"error": "DB Error"})



app = Flask(__name__)

@app.route('/spell/<spellname>')
def spell(spellname):
    return getSpell(spellname)

@app.route('/spells/<casterClass>/<spellLevel>')
def spells(casterClass, spellLevel):
    return getSpellsByLevel(casterClass, spellLevel)

@app.route('/spellsHTML/<casterClass>/<spellLevel>')
def spellsHTML(casterClass, spellLevel):
    jsonSpellList = getSpellsHTML(casterClass, spellLevel)
    return render_template('index.html', result = jsonSpellList)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=8080)