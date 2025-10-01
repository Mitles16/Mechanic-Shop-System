# --- Imports ---
import json

# --- Backend System ---
def Search_Parts(Searching, Search_List=None):
    
    Part_Number = Searching[0]
    Make = Searching[1]
    Model = Searching[2]
    Year = Searching[3]

    params = sum(par != 'None' for par in [Part_Number, Make, Model, Year])
    Searched = []

    if Search_List == None:
        with open("parts.json", "r") as f:
            Parts = json.load(f)

    else:
        Parts = Search_List

    if sum(par != 'None' for par in [Part_Number, Make, Model, Year]) == 4:
        return Parts
    
    if params == 1:
        if Part_Number != 'None':
            for i in list(Parts):
                if i['Part_Number'] == Part_Number:
                    Searched.append(i)
                
        elif Make != 'None':
            for i in list(Parts):
                for e in list(i['Fits']):
                    if e[0] == Make:
                        Searched.append(i)
                    
        elif Model != 'None':
            for i in list(Parts):
                for e in list(i['Fits']):
                    if e[1] == Model:
                        Searched.append(i)
                    
        elif Year != 'None':
            for i in list(Parts):
                for e in list(i['Fits']):
                    if e[2] == Year:
                        Searched.append(i)

        
    
        
    elif params > 0:
        Searched = Search_Parts(['None', Make, 'None', 'None'],
                    Search_Parts(['None', 'None', Model, 'None'],
                        Search_Parts(['None', 'None', 'None', Year],
                            Search_Parts([Part_Number, 'None', 'None', 'None'], Parts))))            
    
    return Searched



# --- Frontend System ---
def Search():
    Parameters = []
    while True:
        for e in list(['Part_Number', 'Make', 'Model', 'Year']):
            k = input(f'{e}: ')
            if k == '':
                k = 'None'
            Parameters.append(k)

        print(Search_Parts(Parameters))

# --- Test Cases ---
Search()