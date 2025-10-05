# --- Imports ---
import json

# --- Backend System ---
def Search_Jobs(Searching, Search_List=None):
    Invoice_Number, Name = Searching
    
    if Search_List == None:
        with open("package/jobs.json", "r") as f:
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

    with open("package/jobs.json", "r") as f:
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
