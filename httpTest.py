from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello world!</h1>"

@app.route('/spell/<spellname>')
def spell(spellname):
    return "<p>Spell is " + spellname + "</p>"

@app.route('/spells/<int:spellid>')
def spells(spellid):
    return "<p>Spell is %s </p>" % spellid

@app.route('/postspell', methods=['GET','POST'])
def postspell():
    if request.method == "POST":
        return "You're using POST!"
    else:
        return "OH, just GET"

if __name__ == "__main__":
    app.run(debug=True)