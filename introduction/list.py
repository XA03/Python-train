varlist=[1,2,3]

varlist.append(4)#[1,2,3,4]
print(varlist)
varlist.extend([5,6,5,2])#[1,2,3,4,5,6]
print(varlist)
varlist.insert(0,999)#[999,1,2,3,4,5,6,5,2]
print(varlist)
varlist.remove(5)#[999,1,2,3,4,6,5,2] , only remove first occurrence.
print(varlist)
x=varlist.pop(0)#x=999 and varlist=[1,2,3,4,6,5,2]
print(varlist,x)
y=varlist.index(2)#y=1 , index only return first occurrence element's index
print(varlist,y)

print(varlist.count(2))
varlist.sort()#[1,2,2,3,4,5,6]
print(varlist)
varlist.reverse()#[6,5,4,3,2,2,1]
print(varlist)

#cpy_varlist=varlist (X) because it is a pointer point to varlist, if you modify cpy_varlist will change varlist.
#cpy_varlist[0]=-1
#print(varlist) [-1,5,4,3,2,2,1]

cpy_varlist=varlist.copy()
cpy_varlist[0]=-1
print("{}\n{}".format(varlist,cpy_varlist))
