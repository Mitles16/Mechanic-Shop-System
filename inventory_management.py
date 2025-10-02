# --- Imports ---
import json

# --- Backend System ---
def Search_Parts(Searching, Search_List=None):
    Part_Number, Make, Model, Year = Searching
    
    if Search_List == None:
        with open("parts.json", "r") as f:
            Parts = json.load(f)

    else:
        Parts = Search_List

    Searched = Parts

    if Part_Number != 'None':
        Searched = [i for i in Searched if i['Part_Number'] == Part_Number]

    if Make != 'None':
        Searched = [i for i in Searched if any(f[0] == Make for f in i['Fits'])]
    
    if Model != 'None':
        Searched = [i for i in Searched if any(f[1] == Model for f in i['Fits'])]

    if Year != 'None':
        Searched = [i for i in Searched if any(f[2] == Year for f in i['Fits'])]

    return Searched

def Add_Part(Part_Number, Fits, Quantity, Location, Description, Cost_Price, RRP):

    Found = False

    with open("parts.json", "r") as f:
        Parts = json.load(f)

    for i in list(Parts):
        if i['Part_Number'] == Part_Number:
            i['Quantity'] += Quantity
            Found = True

    if Found != True:
        New_Part = {
            'Part_Number': Part_Number,
            'Fits': Fits,
            'Quantity': Quantity,
            'Location': Location,
            'Description': Description,
            'Cost_Price': Cost_Price,
            'RRP': RRP
        }

        Parts.append(New_Part)

    with open("parts.json", "w") as f:
        json.dump(Parts, f, indent=4)

def Remove_Part(Part_Number, Quantity):
    with open("parts.json", "r") as f:
        Parts = json.load(f)

    for i in range(len(Parts)):
        if Parts[i]['Part_Number'] == Part_Number:
            Parts[i]['Quantity'] -= Quantity

    with open("parts.json", "w") as f:
        json.dump(Parts, f, indent=4)
# --- Frontend System ---
def Search():
    while True:
        Parameters = []

        for e in list(['Part_Number', 'Make', 'Model', 'Year']):
            k = input(f'{e}: ')
            if k == '':
                k = 'None'
            Parameters.append(k)

        print(Search_Parts(Parameters))

def Add():
    Part_Number = input('Part_Number: ')

    Fits = []
    while True:
        Make = input('Make: ')
        if Make == '' and len(Fits) > 0:
            break
        elif Make == '':
            print('Please Enter a Model Number')
        else:
            while True:
                Model = input('Model: ')

                if Model == '':
                    print('Please Enter a Model')

                else:
                    while True:
                        Year = input('Year: ')

                        if Year == '':
                            print('Please Enter a Valid Year')
                        else:
                            break
                    break
            
            Fits.append([Make, Model, Year])

    Quantity = int(input('Quantity: '))

    Location = input('Location: ')

    Description = input('Description: ')
    Cost_Price = '$' + input('Cost Price: ')
    RRP = '$' + input('RRP: ')

    Add_Part(Part_Number, Fits, Quantity, Location, Description)


# --- Test Cases ---
Remove_Part('Manny', 2)