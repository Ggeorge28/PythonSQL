import tkinter as t
import tkinter.messagebox 

import pyodbc

class mySQL:
    def __init__(self):
        self.main_window = t.Tk()

        self.main_window.geometry('275x125')
        self.main_window.title('SQL Server Login')

        self.frame1 = t.Frame(self.main_window)
        self.frame2 = t.Frame(self.main_window)
        self.frame3 = t.Frame(self.main_window)

        
        self.login = t.Label(self.frame1,text='Login:', anchor = 'w', width = 10)
        self.loginentry = t.Entry(self.frame1,width=20)
        self.loginentry.pack(side = 'right')
        self.login.pack(side='left')



        self.password = t.Label(self.frame2,text='Password:', anchor = 'w', width = 10)
        self.passwordentry = t.Entry(self.frame2,width=20, show = '*')
        self.passwordentry.pack(side = 'right')
        self.password.pack(side='left')

        self.Button = tkinter.Button(self.frame3,text="Login", command=self.access_database)

        self.Button.pack(anchor='c')

        self.frame1.pack(anchor='c')
        self.frame2.pack(anchor='c')
        self.frame3.pack(anchor='c')
        

        t.mainloop()

    def access_database(self):
        login = self.loginentry.get()
        pw = self.passwordentry.get()

        self.main_window.destroy()

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
        cursor.execute ('select * from School.dbo.Course')

        data = cursor.fetchall()

        #print(data)
        for course in data:
            courseID = course[0]
            title = course[1]
            credits = course[2]
            deptID = course[3]

            preList = {'CourseID':courseID, 'Title':title, 'Credits':credits, 'DeptID':deptID}

            courseList.append(preList)

            #print(courseList)

        a = int(input("enter Course ID: "))

        for dictionary in courseList:
            if a == dictionary['CourseID']:
                print(f'Title: {dictionary["Title"]}')
                print(f'Credits: {dictionary["Credits"]}')
                print(f'Dept ID: {dictionary["DeptID"]}')
sql = mySQL()





#
# Define the percentage increase for each department
budget_increase = {
    'Engineering': 0.1,
    'English': 0.1,
    'Economics': 0.1,
    'Mathematics': 0.1,
    'Information Systems': 0.2,
    'Computer Science': 0.15
}

# Define the original budget for each department
budgets = {
    'Engineering': 350000.00,
    'English': 120000.00,
    'Economics': 200000.00,
    'Mathematics': 250000.00,
    'Information Systems': 375000.00,
    'Computer Science': 310500.00
}

# Calculate the new budget and increase in budget for each department
new_budgets = {}
budget_increases = {}
for department, budget in budgets.items():
    if department in budget_increase:
        increase = budget_increase[department]
    else:
        increase = 0.1
    new_budget = budget * (1 + increase)
    budget_increase_amount = new_budget - budget
    new_budgets[department] = new_budget
    budget_increases[department] = budget_increase_amount

# Print the report
print('{:<25}{:<20}{:<20}{}'.format('Dept Name', 'Original Budget', 'New Budget', 'Increase in Budget'))
for department, budget in budgets.items():
    original_budget_str = '${:,.2f}'.format(budget)
    new_budget_str = '${:,.2f}'.format(new_budgets[department])
    increase_str = '${:,.2f}'.format(budget_increases[department])
    print('{:<25}{:<20}{:<20}{}'.format(department, original_budget_str, new_budget_str, increase_str))