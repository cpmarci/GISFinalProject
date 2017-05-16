'''
@author: Kyle Wong
Test implemenation for project
'''

import psycopg2

conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'postgres',password= 'jeep1999')
cur = conn.cursor()
testintersect = '''select pyref, pytime, geom from poly10'''

cur.execute(testintersect)
conn.commit()
cur.execute(testintersect)
parseArray = cur.fetchall()

#print(parseArray)
container = list()


f = open("C:\Data\ProjectOutputIntersect.txt","w+")
counter = 0

#This is for filling in hash map

poly1 = {}
poly2 = {}
poly3 = {}
poly4 = {}
poly5 = {}
poly6 = {}
poly7 = {}
poly8 = {}
poly9 = {}
poly10 = {}


for n in range(len(parseArray)):
    holder = parseArray[n]
    if str(holder[0]) == str(1):
        poly1.setdefault(str(holder[1]), [])
        poly1[str(holder[1])].append(holder[2])
    elif str(holder[0]) == str(2):
        poly2.setdefault(str(holder[1]), [])
        poly2[str(holder[1])].append(holder[2])
     #   print("adding to dictionary")
      #  print(str(poly1[str(holder[1])].append(holder[2])))    
    elif str(holder[0]) == str(3):
        poly3.setdefault(str(holder[1]), [])
        poly3[str(holder[1])].append(holder[2])
        #print("adding to dictionary")
       # print(str(poly1[str(holder[1])].append(holder[2])))   
    elif str(holder[0]) == str(4):
        poly4.setdefault(str(holder[1]), [])
        poly4[str(holder[1])].append(holder[2])
       # print("adding to dictionary")
       # print(str(poly1[str(holder[1])].append(holder[2])))     
    elif str(holder[0]) == str(5):
        poly5.setdefault(str(holder[1]), [])
        poly5[str(holder[1])].append(holder[2])
        #print("adding to dictionary")
        #print(str(poly1[str(holder[1])].append(holder[2])))  
    elif str(holder[0]) == str(6):
        poly6.setdefault(str(holder[1]), [])
        poly6[str(holder[1])].append(holder[2])
        #print("adding to dictionary")
        #print(str(poly1[str(holder[1])].append(holder[2])))       
    elif str(holder[0]) == str(7):
        poly7.setdefault(str(holder[1]), [])
        poly7[str(holder[1])].append(holder[2])
        #print("adding to dictionary")
        #print(str(poly1[str(holder[1])].append(holder[2])))         
    elif str(holder[0]) == str(8):
        poly8.setdefault(str(holder[1]), [])
        poly8[str(holder[1])].append(holder[2])
        #print("adding to dictionary")
        #print(str(poly1[str(holder[1])].append(holder[2])))         
    elif str(holder[0]) == str(9):
        poly9.setdefault(str(holder[1]), [])
        poly9[str(holder[1])].append(holder[2])
        #print("adding to dictionary")
        #print(str(poly1[str(holder[1])].append(holder[2])))         
    elif str(holder[0]) == str(10):
        poly10.setdefault(str(holder[1]), [])
        poly10[str(holder[1])].append(holder[2])



print("----------------------------------")
print("poly1 dictionary")
for keys,values in poly1.items():
    print(keys)
    print(values)
    
print("----------------------------------")
print("poly2 dictionary")
for keys,values in poly2.items():
    print(keys)
    print(values)
    
print("----------------------------------")
print("poly3 dictionary")
for keys,values in poly3.items():
    print(keys)
    print(values)
    
print("----------------------------------")
print("poly4 dictionary")
for keys,values in poly4.items():
    print(keys)
    print(values)
    
print("----------------------------------")
print("poly5 dictionary")
for keys,values in poly5.items():
    print(keys)
    print(values)
    
print("----------------------------------")
print("poly6 dictionary")
for keys,values in poly6.items():
    print(keys)
    print(values)
    
print("----------------------------------")
print("poly7 dictionary")
for keys,values in poly7.items():
    print(keys)
    print(values)
    
print("----------------------------------")
print("poly8 dictionary")
for keys,values in poly8.items():
    print(keys)
    print(values)
    
print("----------------------------------")
print("poly9 dictionary")
for keys,values in poly9.items():
    print(keys)
    print(values)
    
print("----------------------------------")
print("poly10 dictionary")
for keys,values in poly10.items():
    print(keys)
    print(values)
    
print("----------------------------------")



f.close()