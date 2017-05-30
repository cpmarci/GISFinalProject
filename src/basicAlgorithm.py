'''
Test implemenation for project
'''
'''adding a line'''
import psycopg2
import time
start = time.time()

#conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= 'dragon01')
conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= 'jeep1999')
cur = conn.cursor()
testintersect = '''select a.gid,b.gid,ST_Intersects(a.geom, b.geom)
from testdata a, testpoly b '''
projintersect = '''select a.pid,b.pyid,ST_Intersects(a.geom, b.geom)
from points500 a, poly10 b '''

testwithin = '''select a.gid,b.gid,ST_DWITHIN(a.geom, b.geom, 1000), a.geom
from testdata a, testpoly b '''
projwithin = '''select a.pid,b.pyid,ST_DWITHIN(a.geom, b.geom, 1000)
from points500 a, poly10 b '''


#Intersection set
cur.execute(projintersect)
conn.commit()
cur.execute(projintersect)
parseArray = cur.fetchall()
#Test prints for parsing data
#print(parseArray)
container = list()
#print(parseArray[2])
##first = parseArray[2]
##print(first[2])
f = open("C:\Data\ProjectOutputIntersect.txt","w+")
counter = 0
for n in range(len(parseArray)):
    holder = parseArray[n]
    if holder[2] == True:
        ##print(holder[2])
        counter = counter + 1
        writeline = str(holder[0])+":"+str(holder[1]) + "\n"
        f.write(writeline)
        container.append(str(holder[0])+":"+str(holder[1]))
    
    
print(container)
print(counter)
f.close()

# Within parameter for reading in data taken in by GIS
cur.execute(projwithin)
conn.commit()
cur.execute(projwithin)
parseArray2 = cur.fetchall()

#print(parseArray)
container2 = list()
print(parseArray2[2])
#first = parseArray2[2]
#print(first[3])
A = open("C:\Data\ProjectOutputWithin.txt","w+")
counter2 = 0
for n in range(len(parseArray2)):
    holder = parseArray2[n]
    if holder[2] == True:
        ##print(holder[2])
        counter2 = counter2 + 1
        writeline = str(holder[0])+":"+str(holder[1]) + "\n"
        A.write(writeline)
        container2.append(str(holder[0])+":"+str(holder[1]))
    
    
print(container2)
print(counter2)
end = time.time()
print(end - start)
A.close()