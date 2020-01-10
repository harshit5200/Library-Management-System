#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pickle,sys,datetime
def addNewBook():
    with open('ListOfBook.pkl','rb') as f:
        books = pickle.load(f)
        bookN = input('Enter Name of Book: ')
        authN = input('Enter Author Name: ')
        isbnno = int(input('Enter isbn No'))
        while True:
            if len(str(isbnno)) == 13:
                break
            else:
                print('Invalid Input')
                isbnno = int(input('Enter isbn No'))
        try:
            for bookName,authList in books.items():
                for auth in authList:
                    for authName,isbnList in auth.items():
                        if isbnList[0] == isbnno:
                            print('isbn No Already Exist')
                            sys.exit(0)
        except:
            pass
        noofcopies = int(input('Enter No of Copies'))
        books.update({bookN:[{authN:[isbnno,noofcopies]}]})
    with open('ListOfBook.pkl','wb') as f:
        pickle.dump(books,f)
# In[2]:
import pickle,sys,datetime

def displayBookList():
    with open('ListOfBook.pkl','rb') as f:
        books = pickle.load(f)
        for bookName,authList in books.items():
            for auth in authList:
                for authName,isbnList in auth.items():
                    print('Book Name is: ',bookName)
                    print('Author of Book is: ',authName)
                    print('isbn No of Book: ',isbnList[0])
                    print('No of Copies: ',isbnList[1])


# In[3]:

# In[4]:

import pickle,sys,datetime
def addCopies():
    c = 0
    with open('ListOfBook.pkl','rb') as f:
        books = pickle.load(f)
        name = input('Enter Book Name: ')
        author = input('Enter Author Name: ')
        for bookName,authList in books.items():
            if bookName == name:
                for auth in authList:
                    for authName,isbnList in auth.items():
                        if authName == author:
                            isbnno = int(input('Enter isbn No'))
                            while True:
                                if len(str(isbnno)) == 13:
                                    break
                                else:
                                    print('Invalid Input')
                                    isbnno = int(input('Enter isbn No'))
                            if isbnList[0] == isbnno:
                                noofcopies = int(input('Enter No of Copies: '))
                                isbnList[1] += noofcopies
                                c = 1
            if c == 1:
                break
    with open('ListOfBook.pkl','wb') as f:
        pickle.dump(books,f)


# In[6]:
import pickle,sys,datetime

def isbnDetail():
    c = 0
    with open('ListOfBook.pkl','rb') as f:
        books = pickle.load(f)
        isbnNo = int(input('Enter isbn Number: '))
        for bookName,authList in books.items():
            for auth in authList:
                for authName,isbnList in auth.items():
                    if isbnList[0] == isbnNo:
                        print('Book Name is: ',bookName)
                        print('Author of Book is: ',authName)
                        c = 1
            if c == 1:
                break
        else:
            print('Invalid isbn No')


# In[7]:

import pickle,sys,datetime
def bookNameDetail():
    with open('ListOfBook.pkl','rb') as f:
        books = pickle.load(f)
        name = input('Enter Book Name')
        for bookName,authList in books.items():
            if bookName == name:
                for auth in authList:
                    for authName,isbnList in auth.items():
                        print('Author of Book is: ',authName)
                        print('isbn No of Books: ',isbnList[0])
                        print('No of Copies of Books: ',isbnList[1])


# In[8]:

import pickle,sys,datetime
def authorDetails():
    with open('ListOfBook.pkl','rb') as f:
        books = pickle.load(f)
        authN = input('Enter Author Name')
        for bookName,authList in books.items():
            for auth in authList:
                for authName,isbnList in auth.items():
                    if authName == authN:
                        print('Book Name is: ',bookName)
                        print('isbn No of Books: ',isbnList[0])
                        print('No of Copies: ',isbnList[1])


# In[ ]:




