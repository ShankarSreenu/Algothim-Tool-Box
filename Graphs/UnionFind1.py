sets=[]
def createset(u,v):
    sets.append([u,v])

def find(u):
    for i in range(0,len(sets)):
        for j in range(0,len(sets[i])):
            if sets[i][j]==u:
                return i
    return None
def union(u,v):
    a=find(u)
    b=find(v)
    print(a,b)
    if a!=None and b!=None and a==b:
        print("cycle at",u,v)
        return True
    if a==None and b==None:
        createset(u,v)
    elif a==None and b!=None:
        sets[b].append(u)
    elif b==None and a!=None:
        sets[a].append(v)
    elif a!=None and b!=None:
        sets[a]=sets[b]+sets[a]
        sets.pop(b)


arr=[[30,44],[34,47],[22,32],[35,44],[26,36],[2,15],[38,41],[28,35],[24,37],[14,49],[44,45],[11,50],[20,39],[7,39],[19,22],[3,17],[15,25],[1,39],[26,40],[5,14],[6,23],[5,6],[31,48],[13,22],[41,44],[10,19],[12,41],[1,12],[3,14],[40,50],[19,37],[16,26],[7,25],[22,33],[21,27],[9,50],[24,42],[43,46],[21,47],[29,40],[31,34],[9,31],[14,31],[5,48],[3,18],[4,19],[8,17],[38,46],[35,37],[17,43]]
for val in arr:
    union(val[0],val[1])
print(sets)