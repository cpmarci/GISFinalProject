'''
@author: Kyle Wong / C. Philip Marcille
Test implemenation for project
'''
import time
import psycopg2

fName = input('Database password: ')
conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= fName)
start = time.time()
#conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= 'dragon01')
cur = conn.cursor()
testintersect = '''select a.gid,b.gid,ST_Intersects(a.geom, b.geom),a.point, a.time, b.polygon, b.time, ST_asTEXT(a.geom)
from testpointtime a, testpolytime b '''
projintersect = '''select a.pid,b.pyid,ST_Intersects(a.geom, b.geom), a.prefnum, a.ptime, b.pyref, b.pytime, ST_asText(a.geom)
from points500 a, poly10 b WHERE a.ptime >= b.pytime and ST_Intersects(a.geom, b.geom) = True'''

projwithin = '''select a.pid,b.pyid,ST_DWITHIN(a.geom, b.geom, 1000), a.prefnum, a.ptime, b.pyref, b.pytime, ST_asText(a.geom)
from points500 a, poly10 b  WHERE a.ptime >= b.pytime and ST_DWITHIN(a.geom, b.geom, 1000)= True '''
cur.execute(projintersect)
conn.commit()
cur.execute(projintersect)
parseArray = cur.fetchall()

#print(parseArray)
container = list()
print(parseArray[2])

f = open("C:\Data\ProjectOutputIntersect.txt","w+")
counter = 0
for n in range(len(parseArray)):
    holder = parseArray[n]
    if holder[2] == True:
        ##print(holder[2])
        counter = counter + 1
        writeline = str(holder[3])+"-"+str(holder[4]) +":" + str(holder[5]) +"-"+str(holder[6])+"="+str(holder[7]) + "\n"
        f.write(writeline)
        container.append(str(holder[3])+"-"+str(holder[4]) +":" + str(holder[5]) +"-"+str(holder[6])+"="+ str(holder[7]) )
    
    
#print(container)
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
        writeline = str(holder[3])+"-"+str(holder[4]) +":" + str(holder[5]) +"-"+str(holder[6]) +"="+ str(holder[7]) + "\n"
        A.write(writeline)
        container.append(str(holder[3])+"-"+str(holder[4]) +":" + str(holder[5]) +"-"+str(holder[6]) +"="+ str(holder[7]))
    
    
print(counter2)
end = time.time()
print(end - start)
A.close()