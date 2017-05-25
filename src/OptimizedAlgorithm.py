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
start = time.time()
fName = input('Database password: ')
conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= fName)
cur = conn.cursor()

first = 5
testdata = 25
testpoly = 8
points500 =39289
poly10 = 30
testintersect = ('''select a.gid,b.gid,a.point, a.time, b.polygon, b.time, ST_asTEXT(a.geom)
from testpointtime a, testpolytime b WHERE a.gid={0} and a.time > b.time and ST_Intersects(a.geom, b.geom) = True '''. format(first))

projintersect = '''select a.pid,b.pyid,ST_Intersects(a.geom, b.geom), a.prefnum, a.ptime, b.pyref, b.pytime, ST_asText(a.geom)
from points500 a, poly10 b where a.ptime < b.pytime'''


container = list()
for i in range(testdata):
    testintersect2 = ('''select a.gid,b.gid,a.point, a.time, b.polygon, b.time, ST_asTEXT(a.geom)
    from testpointtime a, testpolytime b WHERE a.gid={0} and a.time > b.time and ST_Intersects(a.geom, b.geom) = True '''. format(i))
    cur.execute(testintersect2)
    conn.commit()
    cur.execute(testintersect2)
    parseArray = cur.fetchall()
    print(parseArray)
    
    if len(parseArray) != 0:
            print(str(parseArray[1])+"-"+str(parseArray[2]))
    
end = time.time()



print(end- start)