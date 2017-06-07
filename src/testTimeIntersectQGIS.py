'''
Test implemenation for project
This is finding all practice points that intersect our practice polygon.
WE Load the practice data into testIntersection, this is not used for any of our actual algorithms
For inserting it into qgis for TESTING ONLY IF WOULD WORK.  
'''

import psycopg2
#password for accessing database request
fName = input('Database password: ')
conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= fName)

cur = conn.cursor()
cur = conn.cursor()

#This is for getting intersection of test points and test polygons to check basic attempt for project
#testintersect = '''select a.gid,b.gid,ST_Intersects(a.geom, b.geom),ST_asTEXT(a.geom)
#from testdata a, testpoly b '''

testintersect = '''select a.gid,b.gid,ST_Intersects(a.geom, b.geom),a.point, a.time, b.polygon, b.time, ST_asTEXT(a.geom)
from testpointtime a, testpolytime b WHERE a.time >= b.time and ST_Intersects(a.geom, b.geom) = True'''
#projintersect = '''select a.pid,b.pyid,ST_Intersects(a.geom, b.geom), a.prefnum, a.ptime, b.pyref, b.pytime, ST_asText(a.geom)
#from points500 a, poly10 b WHERE a.ptime >= b.pytime and ST_Intersects(a.geom, b.geom) = True'''




cur.execute(testintersect)
conn.commit()
cur.execute(testintersect)
parseArray = cur.fetchall()

#Parsing data to get correct test values seperated to request an insert into
container = list()
first = parseArray[2]
#writing to a test file
f = open("C:\Data\ProjectTESTOutputIntersect.txt","w+")
counter = 0
#looping through for each insert into while not nil
for n in range(len(parseArray)):
    holder = parseArray[n]
    print("---------Holder-------")
    print(holder)
    #conditional to state if intersects add, else do nothing
    if holder[2] == True:
        counter = counter + 1
        writeline = str(holder[0])+":"+str(holder[1]) + "\n"
        f.write(writeline)
        container.append(str(holder[0])+":"+str(holder[1]))
        holderTemp = str(holder[7])
        tempOne = "INSERT INTO testTimeIntersect (geom) VALUES (ST_GeomFromText("+ "'" + holderTemp + "'" + ", 4269))"
        cur.execute(tempOne)
        conn.commit()
#commiting the request above, printing for checks below.  Complete once finished,
#printing the full every point to poly that meets conditional intersect
print("Point:Poly that intersect")
print(container)
#print total amount added
print("Total amount of intersects in test data")
print(counter)
print("Completed")
f.close()