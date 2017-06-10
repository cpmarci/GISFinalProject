# gisFinalProject Instructions


1. Save ProjectDataSet Folder to local computer

Then... 

create following tables and indexes

2. Table for Points500 
   
 drop table Points500

 create table Points500 (
    pid Integer,
    Pname varchar(128),
    Prefnum Integer,
    Ptime Integer,
    geom geometry(Point, 4269)
   )


3. Table for Poly10

 drop table poly10

 create table poly10 (
    pyid Integer,
    pyname varchar(128),
    pyref Integer,
    pytime Integer,
    geom geometry(Polygon, 4269)
    )
    
    
4.)CREATE INDEX (R tree) for poly10
 
 drop index pyref

 create index pyref on poly10 using gist(geom) 
 
 vacuum analyze poly10

5.)Create index (R tree) for points 500

 drop index prefnum

 create index prefnum on points500 using gist(geom)
 
 vacuum analyze points500

6.)Table for points1000

 drop table Points1000

 create table Points1000 (
    pid Integer,
    Pname varchar(128),
    Prefnum1 Integer,
    Ptime Integer,
    geom geometry(Point, 4269)
   )


7.)Table for Poly15

 drop table poly15

 create table poly15 (
    pyid Integer,
    pyname varchar(128),
    pyref1 Integer,
    pytime Integer,
    geom geometry(Polygon, 4269)
    )

8.)CREATE INDEX (R tree) for poly15
 
 drop index pyref
 
 create index pyref1 on poly15 using gist(geom)

 vacuum analyze poly15

9.)Create index (R tree) for points 1000

 drop index prefnum1

 create index prefnum1 on points1000 using gist(geom)

 vacuum analyze points1000

