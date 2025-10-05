# --- Imports ---
import json

# --- Backend System ---
def Search_Jobs(Searching, Search_List=None):
    Invoice_Number, Name = Searching
    
    if Search_List == None:
        with open("jobs.json", "r") as f:
            Parts = json.load(f)

    else:
        Parts = Search_List

    Searched = Parts

    if Invoice_Number != 'None':
        Searched = [i for i in Searched if i['Invoice_Number'] == Invoice_Number]

    if Name != 'None':
        Searched = [i for i in Searched if i['Name'] == Name]
    
    return Searched

def Add_Job(Job):
    Invoice_Number, Name, Contact, Vechicle = Job

    with open("jobs.json", "r") as f:
        Jobs = json.load(f)

    New_Job = {
        'Invoice_Number': Invoice_Number,
        'Name': Name,
        'Contact': Contact,
        'Vechicle': Vechicle,
        'Work_Performed': [],
        'Work_to_Perform': [],
        'Notes': []
    }

    Jobs.append(New_Job)

    with open("jobs.json", "w") as f:
        json.dump(Jobs, f, indent=4)

def Add_to_Job(Invoice_Number, Type, Work):
    with open("jobs.json", "r") as f:
        Jobs = json.load(f)

    for i in list(Jobs):
        if i['Invoice_Number'] == Invoice_Number:
            i[Type].append(Work)

    with open("jobs.json", "w") as f:
        json.dump(Jobs, f, indent=4)

# --- Frontend System ---
def Add():
    Invoice_Number = int(input('Invoice Number: '))

    Type = int(input('''
1) Work Performed
2) Work to Perfrom
3) Notes
'''))
    if Type == 1:
        Work = {
        'Work': input('Work: '),
        'Hours': input('Hours: ')
        }
        Add_to_Job(Invoice_Number, 'Work_Performed', Work)

    elif Type == 2:
        Work = {
        'Work': input('Work: '),
        'Estimated_Hours': input('Estimated Hours: ')
        }

        Add_to_Job(Invoice_Number, 'Work_to_Perform', Work)

    elif Type == 3:
        Note = input('Note: ')

        Add_to_Job(Invoice_Number, 'Notes', Note)

#Add()


def print_job():
    Job = Search_Jobs([int(input('Job Number: ')), 'None'])

    print(f'''{'-'*78}
Invoice Number: {Job[0]['Invoice_Number']}
Name:           {Job[0]['Name']} | {Job[0]['Contact']['Phone']} | {Job[0]['Contact']['Email']} | {Job[0]['Contact']['Address']}
Vechicle:       {Job[0]['Vechicle'][0]} {Job[0]['Vechicle'][1]} {Job[0]['Vechicle'][2]}
{'-'*78}''')
    print('\n Work Perfromed:')
    for i in list(Job[0]['Work_Performed']):
        print(f'  - {i['Work']} - {i['Hours']}')

    print('\n Work to Perform:')
    for i in list(Job[0]['Work_to_Perform']):
        print(f'  - {i['Work']} - {i['Estimated_Hours']}')

    print('\n Notes:')
    for i in list(Job[0]['Notes']):
        print(f'  - {i}')


#print_job()

