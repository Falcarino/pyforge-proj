from urllib.request import urlopen
import json

def get_compound_properties(compound):
    legal_compounds = ["ADP", "ATP", "STI", "ZID",
                       "DPM", "XP9", "18W", "29P"]

    url = "https://ebi.ac.uk/pdbe/graph-api/compound/summary/"
    url += compound
    response = urlopen(url)

    # storing the JSON respons from url in data
    data_json = json.loads(response.read())
    
    # return a dictionary where keys are the properties
    return data_json[compound][0]
