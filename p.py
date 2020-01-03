import math
import datetime 
import arrow
import numpy as np

def read_file():
    emp=[]
    a=[]
    f= open("Work.txt","r")
    if f.mode == 'r':
        contents =f.readlines()
    
    del contents[0] 
    for i in range(len(contents) ):
        ID,data,start_time,end_time = contents[i].split(',')
        time=arrow.get(end_time, 'HH:mm') -arrow.get(start_time, 'HH:mm')
        emp.append([ID,time])  
        if ID not in a:
            a.append(ID) 
    return [emp,a]
 

if __name__ == "__main__":
    ID=0
    emp=[]
    mylist=[]
    LIST=read_file()
    emp=LIST[0]
    mylist=LIST[1] 
    time=arrow.get("00:00", 'HH:mm')
    # time=emp[1][1]+ emp[1][1] 
     
    new=[] 
    new.append([])
    for i in range(len(mylist) ):
        time=arrow.get("00:00", 'HH:mm')
        for j in range(len(emp) ):
            # print(emp[j][1])
            if mylist[i]==emp[j][0]:
                    time=time+emp[j][1]
                     
        new.append([i+1,time])     

    
    print(new[10][1])     