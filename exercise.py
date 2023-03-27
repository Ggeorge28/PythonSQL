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






'''
1)
Calculate the new budget for each department. Every department will be getting a 10% increase in their budget except for 
the Information Systems (IS) and Computer Science (CS) departments. The IS department gets a 20% increase and the 
CS department gets a 15 % increase. Create a well formatted report that shows each department name, their 
current budget, their new budget and the amount increased.



Dept Name				Original Budget		New Budget		Increse in Budget
Engineering				$350,000.00			$385,000.00		$35,000.00
English					$120,000.00			$132,000.00		$12,000.00
Economics				$200,000.00			$220,000.00		$20,000.00
Mathematics				$250,000.00			$275,000.00		$25,000.00
Information Systems		$375,000.00			$450,000.00		$75,000.00
Computer Science		$310,500.00			$357,075.00		$46,575.00

'''

cursor.execute ('select name, budget from school.dbo.Department')

#data1 = cursor.fetchall()

#for row in data1():
 #  print(row)

data = []

for row in cursor.fetchall():
    name = row[0]
    budget = float(row[1])
    data.append((name,budget))

print("{:<25} {:<20} {:<20} {:<20}".format('Dept Name', 'Original Budget', 'New Budget', 'Increase in Budget'))

for item in data:
    dept_name = item[0]
    original_budget = item[1]


    if dept_name == 'Information Systems':
        increase_in_budget = original_budget * 0.2
    elif dept_name == 'Computer Science':
        increase_in_budget = original_budget * 0.15
    else:
        increase_in_budget = original_budget * 0.1
    
    new_budget = original_budget + increase_in_budget

    print("{:<25} {:<20} {:<20} {:<20}".format(dept_name, f"${original_budget:,.2f}", f"${new_budget:,.2f}", f"${increase_in_budget:,.2f}"))



'''
2)
Display First Name, Last Name and corresponding personal and work email
for STUDENTS ONLY using Person and Contact_Info tables as shown below (only first row shown):


firstname	lastname	Personal Email					Work Email
Gytis		Barzdukas	josephine_darakjy@darakjy.org	ezekiel@chui.com
Peggy		Justice		art@venere.org					wkusko@yahoo.com
Yan			Li			lpaprocki@hotmail.com			bfigeroa@aol.com
Laura		Norman		donette.foller@cox.net			ammie@corrio.com
Nino		Olivotto	simona@morasca.com				francine_vocelka@vocelka.com

'''








'''
3)
Display First Name, Last Name and corresponding home,cell and work phone numbers
for instructors only using Person and Contact_Info tables as shown below (only first 2 rows shown):

FirstName	LastName		Home_Phone		Cell_Phone		Work_Phone
Kim			Abercrombie		(504) 621-8927	(410) 621-8927	(313) 621-8927
Fadi		Fakhouri		(810) 292-9388	(215) 292-9388	(815) 292-9388

'''

