job = [
        {
        'Order_Number': 10932,
        'Name': 'Jane Smith', 
        'Vechicle': ['Suzuki', 'GS500', '2012'],
        'Work_Performed': [{'Work': 'Work', 'Hours_Spent': 'Hours'}],
        'Work_to_Perform': [{'Work': 'Work', 'Estimated_Hours': 'Hours'}],
        'Notes': ['Note1', 'Note2']
        }
]

def display(job, number):
    print(f'''
{'-'*78}
Order Number:   {job[number]['Order_Number']}
Name:           {job[number]['Name']}
Vehicle:        {job[number]['Vechicle'][0]} {job[number]['Vechicle'][1]} {job[number]['Vechicle'][2]}
{'-'*78}
''')


display(job, 0)