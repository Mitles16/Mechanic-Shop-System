Job_Number = 10934
job = [
        {
        'Order_Number': 10932,
        'Name': 'Jane Smith', 
        'Contact': {
            'Phone': '04000000000',
            'Email': 'a_cool_guy@yahoo.com',
            'Address': '104 Cool st, Old York, Merica'
        },
        'Vechicle': ['Suzuki', 'GS500', '2012'],
        'Work_Performed': [{'Work': 'Work', 'Hours_Spent': 'Hours'}],
        'Work_to_Perform': [{'Work': 'Work', 'Estimated_Hours': 'Hours'}],
        'Notes': ['Note1', 'Note2']
        }
]

def display(job):
    for number in range(len(job)):
        print(f'''
{'-'*78}
Order Number:   {job[number]['Order_Number']}
Name:           {job[number]['Name']}
Vechicle:       {job[number]['Vechicle'][0]} {job[number]['Vechicle'][1]} {job[number]['Vechicle'][2]}
{'-'*78}
''')

def add_job(new_job):
    job.append(new_job)

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


def Titlescreen():
    print(f'''
{'-'*78}
1) View All Jobs
2) View Specific Job
3) Add New Job
{'-'*78}
''')
    while True:
        try:
            choice = int(input('Choice: '))

            if 0 < choice < 5:
                break
            else:
                continue
        
        except:
            pass

    
            

        
Create_Job()

display(job)
