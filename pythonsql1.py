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