# --- Imports ---
import os
import time
import inventory_management
import job_manangement


# --- UI Control ---
def Clear_Lines(Lines=None):
    if Lines is None:
        if os.name == 'nt':
            _ = os.system('cls')
        # For macOS and Linux
        else:
            _ = os.system('clear')

    else:
        for i in range(Lines):
            print("\033[F\033[K", end="") 


# --- Inventory System ---
def Search_Inventory():
    Parameters = []

    Clear_Lines()
    print('Searching Parts:')
    for e in list(['Part Number', 'Make', 'Model', 'Year']):
        k = input(f'    {e + ':':<15} ')
        if k == '':
            k = 'None'
        Parameters.append(k)

    Clear_Lines()
    print('Parts Found:')
    print(f'    {'-'*78}')
    for i in list(inventory_management.Search_Parts(Parameters)):
        print(f'    Part Number:      {i['Part_Number']}\n \n    Fits:')
        for e in list(i['Fits']):
            print(f'                      {e[0]} {e[1]} {e[2]}')

        print(f'\n    Quantity:         {int(i['Quantity'])}')
        print(f'    Location:         {i['Location']}')

        print(f'{'\n    Description'}')
        print(f'        {i['Description']}')

        print(f'{'\n    Cost'}')
        print(f'        Cost Price - {i['Cost_Price']} | RRP - {i['RRP']}')

        print(f'    {'-'*78}')

    input('Items Searched')

def Add_Inventory():
    while True:
        Clear_Lines()
        try:
            print('Add Part:')
            Part = []

            Part.append(input(f'    {"Part_Number:":<15}'))

            Fits = []
            while True:
                Make = input(f'    {'Make:':<15}')
                if Make == '' and len(Fits) > 0:
                    break
                elif Make == '':
                    print('    Please Enter a Model Number')
                else:
                    while True:
                        Model = input(f'    {'Model:':<15}')

                        if Model == '':
                            print('    Please Enter a Model')

                        else:
                            while True:
                                Year = input(f'    {'Year:':<15}')

                                if Year == '':
                                    print('    Please Enter a Valid Year')
                                else:
                                    break
                            break
                    
                    Fits.append([Make, Model, Year])

            Part.append(Fits)

            Part.append(int(input(f'    {'Quantity:':<15}')))

            Part.append(input(f'    {'Location:':<15}'))

            Part.append(input(f'    {'Description:':<15}'))
            Part.append('$' + input(f'    {'Cost Price:':<15}'))
            Part.append('$' + input(f'    {'RRP:':<15}'))

            inventory_management.Add_Part(Part)
            input('Part Added')
            break

        except ValueError:
            print("\nInvalid input.")
            time.sleep(1)

def Remove_Inventory():
    print('Stub Implimentation')

# --- Job Management ---

def Search_Job():
    Parameters = []

    Clear_Lines()
    print('Searching Orders:')
    Order_Number = int(input(f'    {'Order Number:':<15}'))
    Name = input((f'    {'Name:':<15}'))
    if Order_Number == '':
        Order_Number = 'None'

    if Name == '':
        Name = 'None'

    Parameters.append(Order_Number)
    Parameters.append(Name)

    Clear_Lines()
    print('Orders Found:')
    print(f'    {'-'*78}')
    for i in list(job_manangement.Search_Jobs(Parameters)):
        print(f'    Order Number:      {i['Invoice_Number']}')
        print(f'    Name:              {i['Name']}\n \n    Contact:')
        print(f'        Phone:     {i['Contact']['Phone']}')
        print(f'        Email:     {i['Contact']['Email']}')
        print(f'        Address:   {i['Contact']['Address']}')

        print(f'\n    Vechicle:         {i['Vechicle'][0]} {i['Vechicle'][1]} {i['Vechicle'][2]}\n')
        
        print('    Work Performed:')
        for e in list(i['Work_Performed']):
            print(f'        {e['Work']} - {e['Hours']} Hours')

        print('\n    Work to Perform:')
        for e in list(i['Work_to_Perform']):
            print(f'        {e['Work']} - Estimated {e['Estimated_Hours']} Hours')

        
        print('\n    Notes:')
        for e in list(i['Notes']):
            print(f'        - {e}')


        print(f'{'\n    Description'}')
        print(f'    {'-'*78}')

    input('Items Searched')

def Add_Job():
    input('Stub Implimentation')

def Remove_Job():
    input('Stub Implimentation')

# ---  Main ---
def main():
    
    while True:
        Clear_Lines()
        try:
            print(f'''
                  
+{'-'*82}+
|  __  __           _                 _         _____           _                  |
| |  \/  |         | |               (_)       / ____|         | |                 |
| | \  / | ___  ___| |__   __ _ _ __  _  ___  | (___  _   _ ___| |_ ___ _ __ ___   |
| | |\/| |/ _ \/ __| '_ \ / _` | '_ \| |/ __|  \___ \| | | / __| __/ _ \ '_ ` _ \  |
| | |  | |  __/ (__| | | | (_| | | | | | (__   ____) | |_| \__ \ ||  __/ | | | | | |
| |_|  |_|\___|\___|_| |_|\__,_|_| |_|_|\___| |_____/ \__, |___/\__\___|_| |_| |_  |
|                                                      __/ |                       |
|                                                     |___/                        |
+{'-'*82}+

    {'-'*52}
    (1) Search Job
    (2) Add Job
    (3) Edit / Remove from Job
    {'-'*52}
    (4) Search Parts
    (5) Add Part
    (6) Sell / Remove Part
    {'-'*52}
    (0) Exit
    ''')
            Choice = int(input(f''))
            if Choice == 0:
                exit()
            elif Choice == 1:
                Search_Job()
            elif Choice == 2:
                Add_Job()
            elif Choice == 3:
                Remove_Job()
            elif Choice == 4:
                Search_Inventory()
            elif Choice == 5:
                Add_Inventory()
            elif Choice == 6:
                Remove_Inventory()

        except ValueError:
            print("\nInvalid input, please enter a number.")
            time.sleep(1)

main()