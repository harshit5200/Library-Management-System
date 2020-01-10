#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pickle,sys,datetime
class Student:
    def saveStudentData(self,name,year_of_admn,branch,sem,admn_id_no,dateOfIssue = [],returnDate = [],bookIssued = [],fineAmount = 0):
        self.name = name
        self.branch = branch
        self.sem = sem
        self.year_of_admn = year_of_admn
        self.admn_id_no = admn_id_no
        self.dateOfIssue = dateOfIssue
        self.returnDate = returnDate
        self.bookIssued = bookIssued
        self.fineAmount = fineAmount
        self.enrollNo = year_of_admn + '0187' + branch + admn_id_no 


# In[2]:


def AddStudent():
    import pickle,sys,datetime
    n = int(input("Enter the No of Student: "))
    with open('ListOfStudent.pkl','rb') as f:
        studentList = pickle.load(f)
        for _ in range(n):
            name = input('Enter the Name: ')
            branch = input('Enter the Branch: ')
            sem = input('Enter the Semester: ')
            year_of_admn = input('Enter Year of Admission: ')
            while True:
                if int(year_of_admn) <= int(datetime.datetime.today().year):
                    break
                else:
                    print('Invalid Year')
                    year_of_admn = input('Enter Year of Admission: ')
            admn_id_no = input('Enter Admission No: ')
            while True:
                if len(admn_id_no) == 4:
                    break
                else:
                    print('Invalid Input')
                    admn_id_no = input('Enter Admission No: ')
            with open('ListOfStudent.pkl','rb') as f:
                obj = pickle.load(f)
                i = 0
                while True:
                    try:
                        if obj[i].admn_id_no == admn_id_no:
                            print('Student Already Exist')
                            sys.exit(0)
                        i = i + 1
                    except(IndexError):
                        break
            s = Student()
            s.saveStudentData(name,year_of_admn,branch,sem,admn_id_no)
            print(s.name + ' is Register with Enrollment No: ' + s.enrollNo)
            studentList.append(s)
        with open('ListOfStudent.pkl','wb') as f1:
            pickle.dump(studentList,f1)


# In[3]:


import pickle,sys,datetime
def displayStudentList():
    with open('ListOfStudent.pkl','rb') as f:
        students = pickle.load(f)
        for student in students:
            print('Enrollment of Student is: ',student.enrollNo)
            print('Name of Student is: ',student.name)
            print('Branch of Student is: ',student.branch)
            print('Semester of Student is: ',student.sem)
            print('Date of Issue Book: ',student.dateOfIssue)
            print('Date for Returning Book: ',student.returnDate)
            print('Book Issued: ',student.bookIssued)
            print('Fine Amount of Student is: Rs',student.fineAmount)


# In[4]:


import pickle,sys,datetime
def deleteStudent():
    data = input('Enter the Enrollment No')
    with open('ListOfStudent.pkl','rb') as f:
        student = pickle.load(f)
        i = 0
        while True:
            try:
                if student[i].enrollNo == data:
                    del student[i]
                i = i + 1
            except:
                print('Data Deleted')
                break
    with open('ListOfStudent.pkl','wb') as f:
        pickle.dump(student,f)


# In[5]:


import pickle,sys,datetime
def modifyStudent():
    print('Press 1 for Name \nPress 2 for Semester')
    choice = int(input('Enter Your Choice'))
    if choice == 1:
        data = input('Enter the Data You Want to Update')
        with open('ListOfStudent.pkl','rb') as f:
            student = pickle.load(f)
            i = 0
            c = 0
            while True:
                try:
                    if student[i].name == data:
                        update = input('Enter the Updated Data: ')
                        student[i].name = update
                        c = 1
                    if c == 1:
                        print('Student Record Updated')
                        break
                    i = i + 1
                except:
                    print('Student Not Found')
                    break
        with open('ListOfStudent.pkl','wb') as f:
            pickle.dump(student,f)
    if choice == 2:
        data = input('Enter the Data You Want to Update')
        with open('ListOfStudent.pkl','rb') as f:
            student = pickle.load(f)
            i = 0
            c = 0
            while True:
                try:
                    if student[i].sem == data:
                        update = input('Enter the Updated Data: ')
                        student[i].sem = update
                        c = 1
                    if c == 1:
                        print('Student Record Updated')
                    i = i + 1
                except:
                    print('Student Not Found')
                    break
        with open('ListOfStudent.pkl','wb') as f:
            pickle.dump(student,f)


# In[6]:


import pickle,sys,datetime
def issue_Book():
    with open('ListOfStudent.pkl','rb') as f:
        student = pickle.load(f)
        rollno = input('Enter the Enrollment No: ')
        i = 0
        c = 0
        while True:
            try:
                if student[i].enrollNo == rollno:
                    if len(student[i].bookIssued) == 5:
                        print('Limit Reached')
                        break
                    if student[i].fineAmount == 0:
                        with open('ListOfBook.pkl','rb') as f1:
                            books = pickle.load(f1)
                            isbnNo = int(input('Enter the isbnNo: '))
                            for bookName,authList in books.items():
                                for auth in authList:
                                    for authName,isbnList in auth.items():
                                        if isbnList[0] == isbnNo:
                                            if isbnList[1] > 0:
                                                c = 1
                                                student[i].bookIssued.append(isbnNo)
                                                isbnList[1] -= 1
                                                student[i].dateOfIssue.append(datetime.date.today())
                                                student[i].returnDate.append(datetime.date.today() + datetime.timedelta(30))
                                                with open('ListOfBook.pkl','wb') as f2:
                                                    pickle.dump(books,f2)
                    else:
                        print('Pay Fine First')
                        break
                if c == 1:
                    print('Book Issued')
                    break
                i = i + 1
            except:
                print('Book Not Found')
                break
    with open('ListOfStudent.pkl','wb') as f3:
        pickle.dump(student,f3)


# In[7]:


import pickle,sys,datetime
def return_Book():
    with open('ListOfStudent.pkl','rb') as f:
        student = pickle.load(f)
        rollno = input('Enter the Enrollment No: ')
        i = 0
        c = 0
        isbnNo = int(input('Enter the isbnNo: '))
        while True:
            try:
                if student[i].enrollNo == rollno:
                    with open('ListOfBook.pkl','rb') as f1:
                        books = pickle.load(f1)
                        for bookName,authList in books.items():
                            for auth in authList:
                                for authName,isbnList in auth.items():
                                    c = 1
                                    if isbnNo == isbnList[0]:
                                        k = 0
                                        for j in student[i].bookIssued:
                                            if j == isbnNo:
                                                student[i].dateOfIssue.pop(k)
                                                student[i].returnDate.pop(k)
                                                break
                                            else:
                                                k = k + 1
                                        student[i].bookIssued.remove(isbnNo)
                                        isbnList[1] += 1
                                        break
                                        
                            
                if c == 1:
                    print('Book Returned')
                    break
                i = i + 1
            except:
                print('Not Found')
                break
        with open('ListOfBook.pkl','wb') as f2:
            pickle.dump(books,f2)
    with open('ListOfStudent.pkl','wb') as f3:
        pickle.dump(student,f3)


# In[8]:


import pickle,sys,datetime   
def calculateFine():
    with open('ListOfStudent.pkl','rb') as f:
        o = pickle.load(f)
        i = 0
        c = 0
        rno = input('Enter the Enrollment No')
        while True:
            try:
                if o[i].enrollNo == rno:
                    c = 1
                    for returndate in o[i].returnDate:
                        if ((datetime.date.today() - returndate).days > 0):
                            o[i].fineAmount += (datetime.date.today() - returndate).days * 2
                        print('Fine Amount is Rs',o[i].fineAmount)
                if c == 1:
                    print('Fine Calculated')
                    break
                i = i + 1
            except:
                print('Not Found')
                break
    with open('ListOfStudent.pkl','wb') as f1:
        pickel.dump(o,f1)

