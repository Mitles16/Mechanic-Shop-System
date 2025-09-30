# --- Imports ---
import json

# --- Backend System ---

# Mock Data
Parts = [
{'Part_Number': 'XYZ-ABC-FGH',
 'Fits': [['Make', 'Model', 'Year'], ['Make', 'Model', 'Year']],
 'Quantity': 4,
 'Location': 'Aisle 5, Bay 4'
 }
]

with open("parts.json", "w") as f:
    json.dump(Parts, f, indent=4)


def Search_Parts(Searching=[], Search_List=None):
    
    Part_Number = Searching[0]
    Make = Searching[1]
    Model = Searching[2]
    Year = Searching[3]

    params = sum(par is not None for par in [Part_Number, Make, Model, Year])
    Searched = []

    if Search_List == None:
        with open("parts.json", "r") as f:
            Parts = json.load(f)

    else:
        Parts = Search_List

    if params == 1:
        if Part_Number != None:
            for i in list(Parts):
                if i['Part_Number'] == Part_Number:
                    Searched.append(i)
                
        elif Make != None:
            for i in list(Parts):
                for e in list(i['Fits']):
                    if e[0] == Make:
                        Searched.append(i)
                    
        elif Model != None:
            for i in list(Parts):
                for e in list(i['Fits']):
                    if e[1] == Model:
                        Searched.append(i)
                    
        elif Year != None:
            for i in list(Parts):
                for e in list(i['Fits']):
                    if e[2] == Year:
                        Searched.append(i)
    
    elif params > 0:
        Search_Parts(Year, Search_Parts(Model, Search_Parts(Make, Search_Parts(Part_Number))))
            
    return Searched

# --- Frontend System ---


# --- Test Cases ---
print(Search_Parts(Part_Number='XYZ-ABC-FGH'))