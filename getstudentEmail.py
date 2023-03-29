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

cursor.execute('exec getStudentEmail')

data = cursor.fetchall()

print('First Name' .ljust(15),'Last Name'.ljust(15),'Personal Email'.ljust(30),'Work Email'.ljust(30))

for row in data:
    print(row[0].ljust(15),row[1].ljust(15),row[2].ljust(30),row[3].ljust(30))