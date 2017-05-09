'''
@author: Kyle Wong
Test implemenation for project
'''

import psycopg2

conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= 'dragon01')
cur = conn.cursor()
testintersect = '''select a.gid,b.gid,ST_DWITHIN(a.geom, b.geom, 1000), a.geom
from testdata a, testpoly b '''
projintersect = '''select a.pid,b.pyid,ST_DWITHIN(a.geom, b.geom, 1000)
from points500 a, poly10 b '''
cur.execute(testintersect)
conn.commit()
cur.execute(testintersect)
parseArray = cur.fetchall()

#print(parseArray)
container = list()
print(parseArray[2])
first = parseArray[2]
print(first[3])
f = open("C:\Data\ProjectOutputWithin.txt","w+")
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