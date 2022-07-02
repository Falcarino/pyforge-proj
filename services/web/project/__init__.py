from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from .api_requests import get_compound_properties

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

class Compound(db.Model):
    __tablename__ = 'compounds'

    compound = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    formula = db.Column(db.String)
    inchi = db.Column(db.String)
    inchi_key = db.Column(db.String)
    smiles = db.Column(db.String)
    cross_links_count = db.Column(db.Integer)

    def __init__(self, compound):
        properties = get_compound_properties(compound)

        self.compound = compound
        self.name = properties['name']
        self.formula = properties['formula']
        self.inchi = properties['inchi']
        self.inchi_key = properties['inchi_key']
        self.smiles = properties['smiles']
        self.cross_links_count = len(properties['cross_links'])

    def __repr__(self):
        entry = ""
        instance_values = self.__dict__.items()

        for attribute, value in instance_values:
            if attribute != "_sa_instance_state":
                entry += attribute.capitalize() + ": " + self.trunc_print(str(value)) + "\n"
        return entry

    def trunc_print(self, s):
        if len(s) > 13: s = s[:10] + "..."
        return s

@app.route("/")
def hello_world():
    return jsonify(status="Yes, I'm running just fine")
