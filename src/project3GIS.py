'''
@author: Kyle Wong
HW1A

Python with psycopg2 which allows for importing and storing of geometric data from PSQL gis
Thus allowing for parsing and creation of algorithms that seperate and allow for
runnable code to be applied.


This is a simple algorithm that slices off every 4th vertice and adds it to a final container with geoms connected
'''

import psycopg2

fName = input('Database password: ')
conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= fName)

#conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= 'dragon01')
cur = conn.cursor()

getPolyLIne = '''SELECT ST_DumpPoints(ST_ExteriorRing(ST_Buffer(geom, .1)))
 from gadm28 where name_1 = 'Illinois' and name_2 = 'Cook';'''    
cur.execute(getPolyLIne)
conn.commit()

cur.execute(getPolyLIne)

moreReadable = cur.fetchall()

#print(moreReadable)
container = list()
'''Here we create holders for the first and last segment of the parsed geom '''
first = moreReadable[0]
container.append(first)
last = moreReadable[-1]
for n in range(len(moreReadable)):
    if n % 4 == 0:
        container.append(moreReadable[n])
'''appending the container to actually recieve the geomed data'''
container.append(last)

print(container)
cur.close()
conn.close()