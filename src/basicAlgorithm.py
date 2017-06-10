'''
BASIC ALGORITHM
Test implemenation for project
'''
'''
First attempt 
Without time constraint. Testing off data
General pull all from GIS than filtering it out with a stimple true boolean check
'''
import psycopg2
import time
#start = time.time()

# allows for different users to actually use the data


fName = input('Database password: ')
conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= fName)
cur = conn.cursor()
start = time.time()
# Project information 
testintersect = '''select a.gid,b.gid,ST_Intersects(a.geom, b.geom)
from testdata a, testpoly b '''
projintersect = '''select a.pid,b.pyid,ST_Intersects(a.geom, b.geom)
from points1000 a, poly15 b '''

testwithin = '''select a.gid,b.gid,ST_DWITHIN(a.geom, b.geom, 1000), a.geom
from testdata a, testpoly b '''
projwithin = '''select a.pid,b.pyid,ST_DWITHIN(a.geom, b.geom, 1000)
from points1000 a, poly15 b '''


#Intersection loop beginning
cur.execute(projintersect)
conn.commit()
cur.execute(projintersect)
parseArray = cur.fetchall()
#Creates the container and begins the intersection statement.
container = list()

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
    
    
#print(container)
print(counter)
f.close()

# Within parameter for reading in data taken in by GIS
cur.execute(projwithin)
conn.commit()
cur.execute(projwithin)
parseArray2 = cur.fetchall()

#Give a data example for the output
container2 = list()
print(parseArray2[2])
#Here is our output for within
#Similiar structure to intersection just differing commands
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
    
    

print(counter2)
end = time.time()
print('-------Counter------')
print(counter2)
print('-------Time------')
print(end - start)
A.close()