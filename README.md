# gisFinalProject

#create following tables

# 1. Table for Points500
    
 drop table Points500

 create table Points500 (
    pid Integer,
    Pname varchar(128),
    Prefnum Integer,
    Ptime Integer,
    geom geometry(Point, 4269)
   )


 2. Table for Poly10

 drop table poly10

create table poly10 (
    pyid Integer,
    pyname varchar(128),
    pyref Integer,
    pytime Integer,
    geom geometry(Polygon, 4269)
    )
    
    
 3.)CREATE INDEX (R tree) for poly10
 drop index pyref
create index pyref on poly10 using gist(geom)
vacuum analyze poly10

4.)Create index (R tree) for points 500

create index prefnum on points500 using gist(geom)
vacuum analyze points500

5.)Table for points1000

 drop table Points1000

 create table Points1000 (
    pid Integer,
    Pname varchar(128),
    Prefnum Integer,
    Ptime Integer,
    geom geometry(Point, 4269)
   )


6.)Table for Poly15

 drop table poly15

create table poly15 (
    pyid Integer,
    pyname varchar(128),
    pyref Integer,
    pytime Integer,
    geom geometry(Polygon, 4269)
    )

