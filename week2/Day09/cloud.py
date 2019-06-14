# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:54:48 2019

@author: user
"""

import pymongo
import dns
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

client = pymongo.MongoClient("mongodb+srv://dbabhishek:<@7062082041%0A>@cluster0-l5mas.mongodb.net/test?retryWrites=true&w=majority")

mydb = client.university

def add_student(Student_Name, Student_Age, Student_Roll_no, Student_Branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.student.insert_one(
            {
            "Student_Name" : St_Name,
            "Student_Age" :St_Age,
            "Student_Roll_no" : St_Roll_no,
            "Student_Branch" : St_Branch
            })
    return "student detail added successfully"


def fetch_all_student():
    user = mydb.yourcollectionname.find()
    for i in user:
        print (i)



add_student("INSERT INTO student VALUES ('Sylvester',25, 50000, 'CSE')")
add_student("INSERT INTO student VALUES ('Yogendra',22, 70000, 'EC')")
add_student("INSERT INTO student VALUES ('Pradeep',23, 30000, 'CSE')")
add_student("INSERT INTO student VALUES ('Kunal',26, 30000, 'CSE')")

fetch_all_employee()
