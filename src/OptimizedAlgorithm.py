'''
Test implemenation for project
Poly 10 30 instances
points 500 39289
testdata 25 instances
testpoly 8 instances


This is our Individual Per PID algorithm that cycles through
Time takes over 20 Minutes
This was our 3 attempt at an algorithm
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
#testintersect = ('''select a.gid,b.gid,a.point, a.time, b.polygon, b.time, ST_asTEXT(a.geom)
#from testpointtime a, testpolytime b WHERE a.gid={0} and a.time > b.time and ST_Intersects(a.geom, b.geom) = True '''. format(first))

#projintersect = ('''select a.pid,b.pyid,ST_Intersects(a.geom, b.geom), a.prefnum, a.ptime, b.pyref, b.pytime, ST_asText(a.geom)
#from points500 a, poly10 b WHERE a.pid={0} and a.ptime > b.pytime and ST_Intersects(a.geom, b.geom) = true'''. format(first))

#projintersect3 = ('''select a.pid,b.pyid,ST_Intersects(a.geom, b.geom), a.prefnum, a.ptime, b.pyref, b.pytime, ST_asText(a.geom)
#from points500 a, poly10 b where a.pid{0} a.ptime > b.pytime and ST_Intersects(a.geom, b.geom) = true'''. format(first))


f = open("C:\Data\ProjectOutputIntersect.txt","w+")
container = list()
counter = 0
for i in range(points500):
    #testintersect2 = ('''select a.gid,b.gid,a.point, a.time, b.polygon, b.time, ST_asTEXT(a.geom)
    #from testpointtime a, testpolytime b WHERE a.gid={0} and a.time >= b.time and ST_Intersects(a.geom, b.geom) = True '''. format(i))
    projintersect2 = ('''select a.pid,b.pyid, a.prefnum, a.ptime, b.pyref, b.pytime, ST_asText(a.geom)
    from points500 a, poly10 b WHERE a.pid={0} and a.ptime >= b.pytime and ST_Intersects(a.geom, b.geom) = True'''. format(i))
    cur.execute(projintersect2)
    conn.commit()
    cur.execute(projintersect2)
    parseArray = cur.fetchall()
    
    
    if len(parseArray) != 0:
    # print(str(parseArray[2])+"-"(+str(parseArray[3]) +":" + str(parseArray[4]) +"-"+str(parseArray[5]))
        holder = parseArray[0]
        counter = counter + 1
        writeline = str(holder[2])+"-"+str(holder[3]) +":" + str(holder[4]) +"-"+str(holder[5]) + "\n"
        f.write(writeline)
        print(str(holder[2])+"-"+str(holder[3]) +":" + str(holder[4]) +"-"+str(holder[5]))


print(counter)
A = open("C:\Data\ProjectOutputWithin.txt","w+")
counter2 = 0
for k in range(testdata):
    testwithint2 = ('''select a.gid,b.gid,a.point, a.time, b.polygon, b.time, ST_asTEXT(a.geom)
    from testpointtime a, testpolytime b WHERE a.gid={0} and a.time >= b.time and ST_DWITHIN(a.geom, b.geom, 1000) = True '''. format(k))
    cur.execute(testwithint2)
    conn.commit()
    cur.execute(testwithint2)
    parseArray2 = cur.fetchall()
    if len(parseArray2) != 0:
        # print(str(parseArray[2])+"-"(+str(parseArray[3]) +":" + str(parseArray[4]) +"-"+str(parseArray[5]))
        holder2 = parseArray2[0]
        counter2 = counter2 + 1
        writeline2 = str(holder2[2])+"-"+str(holder2[3]) +":" + str(holder2[4]) +"-"+str(holder2[5]) + "\n"
        A.write(writeline)
        #print(str(holder2[2])+"-"+str(holder2[3]) +":" + str(holder2[4]) +"-"+str(holder2[5]))
        #print(type(parseArray[0]))
end = time.time()
print(counter2)
print(end- start)
f.close()