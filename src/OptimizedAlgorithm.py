'''
@author: Kyle Wong
Test implemenation for project
Poly 10 30 instances
points 500 39289
testdata 25 instances
testpoly 8 instances
'''
import time
import psycopg2
#start = time.time()

#changing this again so we can both push without rewriting over everything time and again.
fName = input('Database password: ')
conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= fName)
cur = conn.cursor()
start = time.time()


testintersect = '''select a.gid,b.gid,ST_Intersects(a.geom, b.geom),a.point, a.time, b.polygon, b.time, ST_asTEXT(a.geom)
from testpointtime a, testpolytime b '''

projintersect = '''select a.pid,b.pyid,ST_Intersects(a.geom, b.geom), a.prefnum, a.ptime, b.pyref, b.pytime, ST_asText(a.geom)
from points500 a, poly10 b where a.ptime < b.pytime'''
cur.execute(testintersect)
conn.commit()
cur.execute(testintersect)
parseArray = cur.fetchall()

#print(parseArray)
container = list()
print(parseArray[2])
first = parseArray[2]
print(first[3])
f = open("C:\Data\ProjectOutputIntersect.txt","w+")
counter = 0
for n in range(len(parseArray)):
    holder = parseArray[n]
    if holder[2] == True:
        ##print(holder[2])
        counter = counter + 1
        writeline = str(holder[3])+"-"+str(holder[4]) +":" + str(holder[5]) +"-"+str(holder[6]) + "\n"
        f.write(writeline)
        container.append(str(holder[3])+"-"+str(holder[4]) +":" + str(holder[5]) +"-"+str(holder[6]))
    
    
print(container)
print(counter)
end = time.time()

print(end- start)
f.close()