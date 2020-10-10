import json as j

def load_contacs():
    with open('contacts.json') as f:
        return j.load(f)
