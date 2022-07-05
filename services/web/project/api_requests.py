from urllib.request import urlopen
from pathlib import Path
from .logger import log_function_call, create_logger
import json

'''
Path(__file__) returns the absolute file path,
but .parent makes it return just the dir the file is in.
'/' is an operator that appends the string that follows
'''
# Getting a list of the compounds user is allowed to call
file_path = Path(__file__).parent / "Allowed compounds.txt"
with open(file_path) as f:
    legal_compounds = list(map(str.strip,f.readlines()))

@log_function_call(create_logger())
def get_compound_properties(compound):

    global legal_compounds
    if compound not in legal_compounds:
        raise ValueError("Tried calling illegal compound")

    url = "https://ebi.ac.uk/pdbe/graph-api/compound/summary/"
    url += compound
    response = urlopen(url)

    # storing the JSON respons from url in data
    data_json = json.loads(response.read())
    
    # return a dictionary where keys are the properties
    return data_json[compound][0]
