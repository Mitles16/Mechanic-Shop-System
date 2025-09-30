import os
import json


Job_Number = 10934

with open("jobs.json", "r") as f:
    job = json.load(f)

def display(job):
    print(f'''
{'-'*78}
Order Number:   {job['Order_Number']}
Name:           {job['Name']}
Vechicle:       {job['Vechicle'][0]} {job['Vechicle'][1]} {job['Vechicle'][2]}
{'-'*78}
''')

def add_job(new_job):
    job.append(new_job)

    with open("jobs.json", "w") as f:
        json.dump(job, f, indent=4)

def Create_Job():
    Job_Number = 10934

    print('Click Enter to Leave Blank')
    Name = input('Customer Name: ')
    Contact_Ph = input('Phone Number: ')
    Contact_Email = input('Email: ')
    Contact_Address = input('Address: ')

    Vechile_Make = input('Make: ')
    Vechicle_Model = input('Model: ')
    Vechicle_Year = input('Year: ')


    Job_Number += 1

    new_job = {
        'Order_Number': Job_Number,
        'Name': Name, 
        'Contact': {
            'Phone': Contact_Ph,
            'Email': Contact_Email,
            'Address': Contact_Address
        },
        'Vechicle': [Vechile_Make, Vechicle_Model, Vechicle_Year],
        'Work_Performed': [],
        'Work_to_Perform': [],
        'Notes': []
        }
    
    add_job(new_job)

def Clear_Screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def Search(Job_Number=None, Job_Name=None):
    with open("jobs.json", "r") as f:
        job = json.load(f)

    for e in list(job):
        if Job_Number == e['Order_Number'] or Job_Name == e['Name']:
            display(e)

        else:
            print('Not Found')

def Find():
    find = input('Enter a Part Number or Name: ')

    Search(find, find)

def main():
    global job
    while True:
        Clear_Screen()
        
        print(f'''
    {'-'*78}
    1) View All Jobs
    2) View Specific Job
    3) Add New Job
    4) Save & Exit
    {'-'*78}
    ''')
        while True:
            try:
                choice = int(input('    Choice: '))

                if 0 < choice < 5:
                    break
                else:
                    continue
            
            except:
                pass

        if choice == 1:
            display(job)

        elif choice == 2:
            pass

        elif choice == 3:
            Create_Job()

        elif choice == 4:
            quit()

        input('Enter to Continue...')
        

Find()