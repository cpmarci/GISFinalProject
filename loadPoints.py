'''
Created on May 4, 2017

@author: phili_000
'''
#!/usr/bin/python
import sys;
import psycopg2;
import xml.etree.ElementTree as ET;


counter = 0
tree = ET.parse('C:\Data\TrainingDataSet\TrainingDataSet\points500.txt')
root = tree.getroot()
arr = []
arr.append(root.text)
for child in root:
    for child2 in child:        
        arr.append(child2.text)
        arr.append(child.tail)

"""
for i in arr:
     counter = 1 + counter
     print i
     #print 'counter : ',counter

"""
conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= 'jeep1999')
print ("Opened database successfully")

cur = conn.cursor()
i = 0
counter = 0
while (arr[i] and arr[i+1]):
    counter = counter + 1
    x = arr[i+1].split(',')[0]
    y = arr[i+1].split(',')[1]
    coordinates = "POINT(%s %s)" % (x,y)
   # geom = "ST_GeomFromText('POINT(" + str(x) + " " + str(y) + ")',4269)"
    #print x , y  
    cur.execute("INSERT INTO Points500 (pid,Pname,geom) VALUES (%s,trim(%s),ST_GeomFromText(%s,4269)) ",(counter,str(arr[i].strip())[:-1],coordinates))
    print ('counter : ', counter)
    conn.commit()
    i = i+2

conn.commit()
print ("Records created successfully")
conn.close()
