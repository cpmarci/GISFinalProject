'''
Created on May 4, 2017
'''
#!/usr/bin/python
import sys;
import psycopg2;
import xml.etree.ElementTree as ET;

fName = input('Database password: ')
conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= fName)

print ("Opened database successfully")

tree = ET.parse('C:\Data\TrainingDataSet\TrainingDataSet\poly15.txt')
root = tree.getroot()
arr = []
arr.append(root.text)
for child1 in root:
    for child2 in child1:
        for child3 in child2:
            for child4 in child3:
                arr.append(child4.text)
                arr.append(child1.tail)
del arr[-1]                
m = 0
counter = 1
while arr[m]:
    polygonpoints = arr[m+1].split(' ')
    poiintsCount = len(polygonpoints)
    print ('count of polygon points is %s' % (poiintsCount))
    del polygonpoints[-1]

    frr = []
    for i in polygonpoints:
        if str(i) != '':
            frr.append(str(i.split(',')[0]) + ' ' + str(i.split(',')[1]))
        

    #print 'count of polygon points is ', poiintsCount
    #print '\n final array of point is : ', len(frr)
    finalstr = ''
    for i in frr:
        #print i
        finalstr += str(i) + ',' 
        #print arr[1].strip()
    finalstr = finalstr[:-1].strip()
    #print finalstr
         

   
    cur = conn.cursor()
    i = 0
    polyname = str(arr[m])[:-1].strip()
    genericPoly,name1,time1 = polyname.split(":")
    
    #this is testing on how to get the name and the time
    print(polyname)
    print(genericPoly)
    print(name1)
    print(time1)
    #while (arr[i] and arr[i+1]):
    #counter = counter + 1
    #x = arr[i+1].split(',')[0]
    #y = arr[i+1].split(',')[1]
    coordinates = ("Polygon((%s))" % (finalstr))
   # geom = "ST_GeomFromText('POINT(" + str(x) + " " + str(y) + ")',4269)"
    #print x , y  
    cur.execute("INSERT INTO poly15 (pyid,pyname,pyref1,pytime,geom) VALUES (%s,trim(%s),%s,%s,ST_GeomFromText(%s,4269)) ",(counter,polyname,name1,time1,coordinates))
    #print 'counter : ', counter
    #conn.commit()
    #i = i+2

    conn.commit()
    print ("Records created successfully")   
    counter = counter + 1
    m = m + 2

print ('operation completed')
conn.close()