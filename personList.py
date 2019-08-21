class Person(object):
   

    def __init__(self, name=None, job=None, nid=None):
        self.name = name
        self.job = job
        self.nid = nid




personList = []
personList.append(Person("John", "teacher", "1234"))
personList.append(Person("sara", "admin", "8787"))
personList.append(Person("fahad", "teacher", "8980"))
personList.append(Person("ford", "planner", "2313"))
personList.append(Person("Ghaida", "dentist", "9093"))
personList.append(Person("Jimy", "coach", "9234"))

import operator

personList.sort(key=operator.attrgetter('job'))


for person in personList:
    print(" NID: "+ person.nid +" Name: "+person.name +" Job: "+person.job+"\n")


choice = input("Enter a job to show  all persons in that job  \n teacher\n admin \n planner \n dentist \n coach \n ")


for person in personList:
    if choice in person.job:
       print(" NID: " + person.nid + " Name: " + person.name + " Job: " + person.job + "\n")

else 
 print("no one in this job ")
