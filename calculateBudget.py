import pyodbc

login = 'grant_george1'
pw = 'MIS4322student'

preList = {}
courseList = []
cn_str = (
'Driver={SQL Server};'
'Server=MIS-SQLJB;'
'Database=School;'
'UID='+login+';'
'PWD='+pw+';'
)

cn = pyodbc.connect(cn_str)

cursor = cn.cursor()


cursor.execute('Select Name, Budget from School.dbo.department')

data = cursor.fetchall()

print('Dept. Name' .ljust(25),'Original Budget' .ljust(20),'New Budget' .ljust(15),'Increase in Budget' .ljust(10))

for row in data:
    name = row[0]
    old_budget = float(row[1])
    

    if name == 'Information Systems':
        new_budget = old_budget * 1.2
    elif name == 'Computer Science':
        new_budget = old_budget * 1.15
    else:
        new_budget = old_budget * 1.1
    
    increase = new_budget - old_budget

    print(f"{name.ljust(25)} {old_budget:,.2f} {new_budget:20,.2f} {increase:14,.2f} ")