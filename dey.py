import random,os,sys,time,numpy as np
from os import system
laki=["farrel","sapta","syahraza","norman","alfath","aksara","zovie","khaza","satrio","akbar","hadi","ararya","naupal","eben","afqi","rizqy","maulana","bangbang"]
perempuan=["aulya","nasya","rizka","nayla","amelia","angel","gheffira","najwa","valentina","salma","aliya","kaila","septiani","clarissa","nizwah","afifah","alvina","cheryl"]

def typewriter(any):
    for char in (any):  
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06)

def typewriter2(any):
    for char in (any):  
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def typewriter3(any):
    for char in (any):  
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.00000001)

def ulangx():
    lakipack()
    time.sleep(1)

def ulangy():
    cewepack()
    time.sleep(1)

# Laki Laki
def lakipack():
    x=list(random.sample(laki,18))
    xsplit = np.array_split(x, 9)
    x2 = ' '.join([str(elem) for elem in xsplit])
    typewriter2(x2)
    print("")
    typewriter("Ulang? ")
    u=str.lower(input(""))
    print("\n")
    if u=="ya":
        ulangx()
    if u=="ga":
        mulai()
