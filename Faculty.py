#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pickle,sys,datetime
class Faculty:
    def saveFacultytData(self,name,id_no,dateOfIssue = [],returnDate = [],bookIssued = [],fineAmount = 0):
        self.name = name
        self.id_no = id_no
        self.dateOfIssue = dateOfIssue
        self.returnDate = returnDate
        self.bookIssued = bookIssued
        self.fineAmount = fineAmount


# In[2]:

import pickle,sys,datetime
def AddFaculty():
    n = int(input("Enter the No of Faculty: "))
    with open('ListOfFaculty.pkl','rb') as f:
        facultyList = pickle.load(f)
        for _ in range(n):
            name = input('Enter the Name: ')
            id_no = input('Enter Id No: ')
            while True:
                if len(id_no) == 5:
                    break
                else:
                    print('Invalid Input')
                    id_no = input('Enter Id No: ')
            with open('ListOfFaculty.pkl','rb') as f:
                obj = pickle.load(f)
                i = 0
                while True:
                    try:
                        if obj[i].id_no == id_no:
                            print('Faculty Already Exist')
                            sys.exit(0)
                        i = i + 1
                    except(IndexError):
                        break
            fa = Faculty()
            fa.saveFacultytData(name,id_no)
            facultyList.append(fa)
        with open('ListOfFaculty.pkl','wb') as f1:
            pickle.dump(facultyList,f1)    


# In[3]:

import pickle,sys,datetime
def displayFacultyList():
    with open('ListOfFaculty.pkl','rb') as f:
        faculties = pickle.load(f)
        for faculty in faculties:
            print('Id No of Faculty: ',faculty.id_no)
            print('Name of Faculty is: ',faculty.name)
            print('Date of Issue Book: ',faculty.dateOfIssue)
            print('Date for Returning Book: ',faculty.returnDate)
            print('Book Issued: ',faculty.bookIssued)
            print('Fine Amount of Faculty is: ',faculty.fineAmount)


# In[4]:

import pickle,sys,datetime
def deleteFaculty():
    data = input('Enter the Id No')
    with open('ListOfFaculty.pkl','rb') as f:
        faculty = pickle.load(f)
        i = 0
        c = 0
        while True:
            try:
                if faculty[i].id_no == data:
                    print('Data Deleted')
                    del faculty[i]
                    c = 1
                if c == 1:
                    break
                i = i + 1
            except:
                print('Id Not Found')
                break
    with open('ListOfFaculty.pkl','wb') as f:
        pickle.dump(faculty,f)


# In[5]:

import pickle,sys,datetime
def issue_Faculty_Book():
    with open('ListOfFaculty.pkl','rb') as f:
        faculty = pickle.load(f)
        idno = input('Enter the Id No: ')
        i = 0
        c = 0
        while True:
            try:
                if faculty[i].id_no == idno:
                    if faculty[i].fineAmount == 0:
                        with open('ListOfBook.pkl','rb') as f1:
                            books = pickle.load(f1)
                            isbnNo = int(input('Enter the isbnNo: '))
                            for bookName,authList in books.items():
                                for auth in authList:
                                    for authName,isbnList in auth.items():
                                        if isbnList[0] == isbnNo:
                                            if isbnList[1] > 0:
                                                c = 1
                                                faculty[i].bookIssued.append(isbnNo)
                                                isbnList[1] -= 1
                                                faculty[i].dateOfIssue.append(datetime.date.today())
                                                faculty[i].returnDate.append(datetime.date.today() + datetime.timedelta(30))
                                                break

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
        with open('ListOfBook.pkl','wb') as f2:
            pickle.dump(books,f2)
    with open('ListOfFaculty.pkl','wb') as f3:
        pickle.dump(faculty,f3)


# In[6]:

import pickle,sys,datetime
def returnFacultyBook():
    with open('ListOfFaculty.pkl','rb') as f:
        faculty = pickle.load(f)
        idno = input('Enter the Id No: ')
        i = 0
        c = 0
        isbnNo = int(input('Enter the isbnNo: '))
        while True:
            try:
                if faculty[i].id_no == idno:
                    with open('ListOfBook.pkl','rb') as f1:
                        books = pickle.load(f1)
                        for bookName,authList in books.items():
                            for auth in authList:
                                for authName,isbnList in auth.items():
                                    c = 1
                                    if isbnNo == isbnList[0]:
                                        k = 0
                                        for j in faculty[i].bookIssued:
                                            if j == isbnNo:
                                                faculty[i].dateOfIssue.pop(k)
                                                faculty[i].returnDate.pop(k)
                                                break
                                            else:
                                                k = k + 1
                                        faculty[i].bookIssued.remove(isbnNo)
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
    with open('ListOfFaculty.pkl','wb') as f3:
        pickle.dump(faculty,f3)


# In[ ]:
import pickle,sys,datetime
def calculateFine():
    with open('ListOfFaculty.pkl','rb') as f:
        o = pickle.load(f)
        i = 0
        c = 0
        idno = input('Enter the Id No')
        while True:
            try:
                if o[i].id_no == idno:
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
    with open('ListOfFaculty.pkl','wb') as f1:
        pickle.dump(o,f1)