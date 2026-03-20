g={'A':['B','C'],
   'B':['A','C','D'],
   'C':['A','B','D'],
   'D':['B','D']
}

v=list(g)
n=len(v)

col={1:'red',2:'blue',3:'green'}

def ok(x,c,a):
    for y in g[x]:
        if a.get(y)==c:
            return False
    return True

def bt(m,a,i):
    if i==n:
        return True
    x=v[i]
    for c in col:
        if ok(x,c,a):
            a[x]=c
            if bt(m,a,i+1):
                return True
            del a[x]
    return False 



a={}
if bt(3,a,0):
    print("coloring with",3,"colors")
    for x in v:
        print("vertex:",x,":color",col[a[x]])