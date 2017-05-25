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


container = list()
for i in range(testdata):
    testintersect2 = ('''select a.gid,b.gid,a.point, a.time, b.polygon, b.time, ST_asTEXT(a.geom)
    from testpointtime a, testpolytime b WHERE a.gid={0} and a.time > b.time and ST_Intersects(a.geom, b.geom) = True '''. format(i))
    cur.execute(testintersect2)
    conn.commit()
    cur.execute(testintersect2)
    parseArray = cur.fetchall()
    
    
    if len(parseArray) != 0:
           # print(str(parseArray[2])+"-"(+str(parseArray[3]) +":" + str(parseArray[4]) +"-"+str(parseArray[5]))
           holder = parseArray[0]
           print(parseArray[0])
           print(str(holder[2])+"-"+str(holder[3]) +":" + str(holder[4]) +"-"+str(holder[5]))
           print(type(parseArray[0]))
end = time.time()



print(end- start)