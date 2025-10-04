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
    while True:
        Parameters = []

        for e in list(['Part_Number', 'Make', 'Model', 'Year']):
            k = input(f'{e}: ')
            if k == '':
                k = 'None'
            Parameters.append(k)

        print(inventory_management.Search_Parts(Parameters))

def Add_Inventory():
    Part = []

    Part.append(Part_Number = input('Part_Number: '))

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

    Part.append(Fits)

    Part.append(Quantity = int(input('Quantity: ')))

    Part.append(Location = input('Location: '))

    Part.append(Description = input('Description: '))
    Part.append(Cost_Price = '$' + input('Cost Price: '))
    Part.append(RRP = '$' + input('RRP: '))

    inventory_management.Add_Part(Part)

def Remove_Inventory():
    print('Stub Implimentation')

# --- Job Management ---

def Search_Job():
    print('Stub Implimentation')

def Add_Job():
    print('Stub Implimentation')

def Remove_Job():
    print('Stub Implimentation')

# ---  Main ---
def main():
    Clear_Lines()
    while True:
        try:
            print('''
  __  __           _                 _         _____           _                 
 |  \/  |         | |               (_)       / ____|         | |                
 | \  / | ___  ___| |__   __ _ _ __  _  ___  | (___  _   _ ___| |_ ___ _ __ ___  
 | |\/| |/ _ \/ __| '_ \ / _` | '_ \| |/ __|  \___ \| | | / __| __/ _ \ '_ ` _ \ 
 | |  | |  __/ (__| | | | (_| | | | | | (__   ____) | |_| \__ \ ||  __/ | | | | |
 |_|  |_|\___|\___|_| |_|\__,_|_| |_|_|\___| |_____/ \__, |___/\__\___|_| |_| |_|
                                                      __/ |                      
                                                     |___/                          
                  ''')
            Choice = int(input(f'''
    {'-'*78}
    (1) Search Job
    (2) Add to Job
    (3) Edit / Remove from Job
    {'-'*78}
    (4) Search Parts
    (5) Add Part
    (6) Sell / Remove Part
    {'-'*78}
    (0) Exit
    '''))
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
        except:
            print('Error With input')
            time.sleep(1)
            Clear_Lines()

main()