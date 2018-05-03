from flask import Flask, request
from io import StringIO
import random


app = Flask(__name__)

def setRoom():
    noises = ["Bang","Bang","Bang","Bang","Bang",
    "Bellowing",
    "Buzzing"
    "Chanting","Chanting","Chanting",
    "Chiming",
    "Chirping",
    "Clanking",
    "Clashing",
    "Clicking",
    "Coughing",
    "Creaking","Creaking",
    "Drumming",
    "Footsteps Ahead","Footsteps Ahead","Footsteps Ahead","Footsteps Ahead",
    "Footsteps Approaching","Footsteps Approaching","Footsteps Approaching",
    "Footsteps Behind","Footsteps Behind","Footsteps Behind",
    "Footsteps Receding","Footsteps Receding",
    "Footsteps to the side","Footsteps to the side",
    "Giggling (faint)","Giggling (faint)",
    "Gong",
    "Grating","Grating","Grating",
    "Groaning","Groaning",
    "Grunting",
    "Hissing","Hissing",
    "Horn sounding",
    "Howling",
    "Humming","Humming",
    "Jingling",
    "Knocking","Knocking","Knocking","Knocking",
    "Laughter","Laughter",
    "Moaning","Moaning",
    "Murmuring","Murmuring","Murmuring",
    "Music","Music",
    "Rattling",
    "Ringing",
    "Rustling","Rustling","Rustling","Rustling",
    "Scratching or scrabbling","Scratching or scrabbling","Scratching or scrabbling","Scratching or scrabbling",
    "Screaming","Screaming",
    "Scuttling","Scuttling","Scuttling",
    "Shuffling",
    "Slithering","Slithering",
    "Snapping",
    "Sneezing",
    "Sobbing",
    "Splashing",
    "Splintering",
    "Squeaking","Squeaking",
    "Squealing",
    "Tapping","Tapping",
    "Thud","Thud",
    "Thumping","Thumping",
    "Tinkling",
    "Twanging",
    "Whining",
    "Whispering",
    "Whistling","Whistling"
    ]

    air = ["clear and damp","clear and drafty","clear but cold","foggy or misty and cold","clear, with mist covering the floor",
    "clear and warm","hazy and humid","smoky and steamy","clear, with smoke covering the ceiling","Clear and windy"]

    odors = ["acrid","chlorine","dank or moldy","Earthy","Manure","Metallic","Ozone","Putrid","Rotting vegetation",
    "Salty and wet","Smoky","Stale","Sulfurous","Urine"]

    features = ["a broken arrow",
    "a pile of ashes","a pile of ashes","a pile of ashes",
    "a pile of bones","scattered bones",
    "a broken bottle",
    "a corroded chain",
    "a splintered club",
    "cobwebs","cobwebs","cobwebs","cobwebs","cobwebs","cobwebs","cobwebs","cobwebs","cobwebs",
    "a copper piece",
    "a dagger hilt",
    "dampness on the ceiling","dampness on the ceiling",
    "dampness on the wall","dampness on the wall","dampness on the wall","dampness on the wall",
    "dried blood",
    "blood dripping","blood dripping","blood dripping","blood dripping","blood dripping","blood dripping","blood dripping",
    "a pile of dung","a pile of dung","a pile of dung",
    "dust","dust","dust","dust","dust","dust","dust","dust","dust",
    "a cracked flask",
    "scraps of food",
    "common fungus",
    "guano","guano","guano",
    "some type of hair or fur",
    "a cracked hammer",
    "a badly dented helmet",
    "a bent iron bar",
    "a blunt javelin head",
    "a leather boot",
    "leaves and twigs","leaves and twigs","leaves and twigs",
    "common mold","common mold","common mold","common mold",
    "a pick handle",
    "a broken wooden pole",
    "pottery shards",
    "a pile of rags","scattered rags",
    "a rotten rope",
    "rubble and dirt","rubble and dirt",
    "a torn sack",
    "a slimy substance","a slimy substance","a slimy substance",
    "a rusted spike",
    "loose sticks","loose sticks",
    "small stones",
    "a bed of straw",
    "a broken sword",
    "scattered teeth or fangs",
    "a burned out torch",
    "scratches on the wall",
    "a large puddle of water","a large puddle of water",
    "a small puddle of water","a small puddle of water",
    "trickling water","trickling water",
    "melted candle",
    "wax drippings",
    "rotten wood scraps","rotten wood scraps","rotten wood scraps"
    ]

    furnishings = ["altar",
    "armchair",
    "armoire",
    "curtain",
    "bag",
    "barrel",
    "bed","bed",
    "bench",
    "blanket",
    "large box",
    "brazier and charcoal",
    "bucket",
    "buffet cabinet",
    "wrack of bunks",
    "butt or huge cask",
    "cabinet",
    "candelabrum",
    "large carpet",
    "cask",
    "chandelier",
    "charcoal",
    "plain chair","plain chair",
    "padded chair","padded chair",
    "large chest",
    "medium chest",
    "chest of drawers",
    "closet",
    "pile of coal",
    "couch","couch",
    "crate",
    "cresset",
    "cupboard",
    "cushion",
    "dais",
    "desk",
    "fireplace and wood","fireplace and wood","fireplace and wood",
    "fireplace mantle",
    "firkin (small cask)",
    "fountain",
    "fresco",
    "grindstone",
    "hamper",
    "hassock",
    "hogshead (large cask)",
    "large idol",
    "keg",
    "loom",
    "mat",
    "mattress",
    "pail",
    "painting",
    "pallet","pallet","pallet",
    "pedestal",
    "pegs","pegs","pegs",
    "pillow",
    "pipe (large cask)",
    "quilt",
    "medium rug","small rug","medium rug",
    "rushes",
    "sack",
    "sconce",
    "screen",
    "sheet",
    "shelf","shelf",
    "shrine",
    "sideboard",
    "sofa",
    "normal staff",
    "stand",
    "statue",
    "high stool",
    "stool",
    "large table",
    "long table",
    "low table",
    "round table",
    "small table",
    "trestle table",
    "tapestry",
    "throne",
    "trunk",
    "tub",
    "tun (huge cask)",
    "urn",
    "wall basin and font",
    "wood billets",
    "workbench"
    ]

    currentNoise = noises[random.randint(0,98)]
    currentAir = ""
    currentOdor = ""

    airNum = random.randint(0,99)

    if airNum <= 60:
        currentAir = air[0]
    elif airNum > 60 and airNum <= 70:
        currentAir = air[1]
    elif airNum > 70 and airNum <=80:
        currentAir = air[2]
    elif airNum > 80 and airNum <= 83:
        currentAir = air[3]
    elif airNum > 84 and airNum <= 85:
        currentAir = air[4]
    elif airNum > 85 and airNum <= 90:
        currentAir = air[5]
    elif airNum > 90 and airNum <= 93:
        currentAir = air[6]
    elif airNum > 93 and airNum <= 96:
        currentAir = air[7]
    elif airNum > 96 and airNum <= 98:
        currentAir = air[8]
    elif airNum > 98 and airNum <= 99:
        currentAir = air[9]

    odorNum = random.randint(0,99)

    if odorNum < 4:
        currentOdor = odors[0]
    elif odorNum > 3 and odorNum < 6:
        currentOdor = odors[1]
    elif odorNum > 5 and odorNum < 40:
        currentOdor = odors[2]
    elif odorNum > 39 and odorNum < 50:
        currentOdor = odors[3]
    elif odorNum > 49 and odorNum < 58:
        currentOdor = odors[4]
    elif odorNum > 57 and odorNum < 62:
        currentOdor = odors[5]
    elif odorNum > 61 and odorNum < 66:
        currentOdor = odors[6]
    elif odorNum > 65 and odorNum < 71:
        currentOdor = odors[7]
    elif odorNum > 70 and odorNum < 76:
        currentOdor = odors[8]
    elif odorNum > 75 and odorNum < 78:
        currentOdor = odors[9]
    elif odorNum > 77 and odorNum < 83:
        currentOdor = odors[10]
    elif odorNum > 82 and odorNum < 90:
        currentOdor = odors[11]
    elif odorNum > 89 and odorNum < 96:
        currentOdor = odors[12]
    elif odorNum > 95 and odorNum < 99:
        currentOdor = odors[13]

    seenFurnishings = "The air is " + currentAir.lower() + " and smells " + currentOdor.lower() + ", you hear " + currentNoise.lower() + "."

    # seenFeatures = "You see "
    # numOfFeatures = random.randint(1,4)
    # for i in range(0,numOfFeatures):    
    #     seenFeatures += features[random.randint(0,98)] + ", "
    #     if i == numOfFeatures - 1:
    #         seenFeatures = seenFeatures[:-2]
    #         seenFeatures += " and " + features[random.randint(0,99)]

    # print(seenFeatures)
    flatItems = ["table","desk","carpet","rug","chest","couch","pallet"]

    numFurnishings = random.randint(2,5)
    seenFurnishings += "<br \>The room contains the following, "

    for i in range(0,numFurnishings):
        if i == 0:
            item = furnishings[random.randint(0,99)]
            if any(s in item for s in (flatItems)):
                seenFurnishings += "a " + item + " in the center of the room with " + features[random.randint(0,98)] + " on it, "
            else: continue
        elif i == 1:
            item = furnishings[random.randint(0,99)]
            if any(s in item for s in (flatItems)):
                seenFurnishings += "a " + item + " in the far corner of the room with " + features[random.randint(0,98)] + " on it, "
            else:
                seenFurnishings += "a " + item + " in the far corner of the room, "
        elif i == 2:
            item = furnishings[random.randint(0,99)]
            if any(s in item for s in (flatItems)):
                seenFurnishings += "a " + item + " on the east side of the room with " + features[random.randint(0,98)] + " on it, "
            else:
                seenFurnishings += "a " + item + " on the east side of the room, "
        elif i == 3:
            item = furnishings[random.randint(0,99)]
            if any(s in item for s in (flatItems)):
                seenFurnishings += "a " + item + " on the west side of the room with " + features[random.randint(0,98)] + " on it, "
            else:
                seenFurnishings += "a " + item + " on the west side of the room, "
        elif i == 4:
            item = furnishings[random.randint(0,99)]
            if any(s in item for s in (flatItems)):
                seenFurnishings += "a " + item + " on the north side of the room with " + features[random.randint(0,98)] + " on it, "
            else:
                seenFurnishings += "a " + item + " on the north side of the room, "
        elif i == 5:
            item = furnishings[random.randint(0,99)]
            if any(s in item for s in (flatItems)):
                seenFurnishings += "a " + item + " on the south side of the room with " + features[random.randint(0,98)] + " on it, "
            else:
                seenFurnishings += "a " + item + " on the south side of the room, "

    if i == numFurnishings -1:
        seenFurnishings = seenFurnishings[:-2]       

    if "wall" in seenFurnishings:
        seenFurnishings = seenFurnishings.replace("on the wall","in it")

    dot = seenFurnishings.rfind(",")
    seenFurnishings = seenFurnishings[:dot] + " and" + seenFurnishings[dot+1:]

    return seenFurnishings

# print(seenFurnishings)

@app.route('/')
def index():
    return setRoom()

@app.route('/rooms/<numRooms>')
def rooms(numRooms):
    rooms = StringIO()

    for i in range(1,int(numRooms)+ 1):
        rooms.write('<p>' + str(i) + '. ' + setRoom() + '</p>')

    return rooms.getvalue()

if __name__ == "__main__":
    app.run(debug=True)

# spaces = 0
# finalString = ""

# for i, c in enumerate(seenFurnishings):
#     # print(i, c)
#     if c == ' ':
#         spaces += 1        
    
#     if spaces % 10 == 0:
#         finalString += c + "\r"
#     else:
#         finalString += c

# print(finalString)