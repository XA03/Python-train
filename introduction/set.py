var_set={'a','b','c',1,2,3}

print(var_set)

var_set.add('uuh'); print("var_set=",var_set,sep="")
var_set_cpy=var_set.copy(); print("var_set_cpy=",var_set_cpy,sep="")
var_set.clear(); print("var_set=",var_set,sep="")

var_set.add('uuh'); print("\nvar_set=",var_set,sep="",end=""); 
x=var_set_cpy.difference(var_set); print(" set.difference will return two sets difference:\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,"\nvar_set_cpy differ var_set=",
x,sep="")


print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,end="")
var_set.difference_update(var_set_cpy); 
print("\nset.difference_update() will remove two set intersection in set :var_set differ var_set_cpy \n","var_set=",var_set
,"\nvar_set_cpy=",var_set_cpy,sep="")

var_set.add(1);var_set.add(2);var_set.add(3)
print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,end="")
x=var_set.intersection(var_set_cpy)
print("\nset.intersection will return two sets intersection\n","var_set=",var_set
,"\nvar_set_cpy=",var_set_cpy,"\nvar_set and var_set_cpy=",x,sep="")

print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,end="")
var_set_cpy.intersection_update(var_set)
print("\nset.intersection_update() will make left-operand be assigned to the two sets intersection\n","var_set=",var_set
,"\nvar_set_cpy=",var_set_cpy,"\nvar_set and var_set_cpy=",x,sep="")



x=var_set.isdisjoint(var_set_cpy);print("setA.isdisjoint(setB) will return a bool value indicating whether setA has a intersection.\n")
print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,sep="")
print("var_set.isdisjoint(var_set_cpy) is ",x)

var_set={5,6,7}
x=var_set.isdisjoint(var_set_cpy)
print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,sep="")
print("var_set.isdisjoint(var_set_cpy) is ",x)

var_set={1,2}
x=var_set.issubset(var_set_cpy);print("setA.issubset(setB) will return a bool value indicating whether setA is a subset of setB.")
print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,sep="")
print("var_set.issubset(var_set_cpy) is ",x)

x=var_set_cpy.issuperset(var_set);print("setA.issubset(setB) will return a bool value indicating whether setA is a superset of setB.")
print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,sep="")
print("var_set_cpy.issuperset(var_set) is ",x)

x=var_set.pop();print("setA.pop() will remove random item in setA. But the experiment is always pop 1.")
print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,sep="")
print("var_set.pop()=",x,sep="")


var_set.remove(2);print("setA.remove(val) will remove val in set and show error messages when remove empty set. But discard(val) will not show that.")
print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,sep="")

var_set={1,2,3,4,5,6};var_set_cpy={1,2,3,7,8,9}
x=var_set.symmetric_difference(var_set_cpy);print("setA.symmetric_difference(setB) will return a the symmetric difference between setA and setB")
print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,sep="")
print("var_set.symmetric_difference(var_set_cpy)=",x,sep="")


print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,sep="")
x=var_set.symmetric_difference_update(var_set_cpy);print("setA.symmetric_difference_update(setB) will update the setA to the symmetric_difference between setA and setB",end="")
print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,sep="")

var_set={1,2,3};var_set_cpy={4,5,6}
print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,sep="")
x=var_set.union(var_set_cpy);print("setA.union(setB) return the union set between setA and setB.")
print("var_set.union(var_set_cpy)=",x,sep="")

print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,sep="")
var_set.update(var_set_cpy);print("setA.update(setB) will update setA to the union set between setA and setB")
print("\nvar_set=",var_set,"\nvar_set_cpy=",var_set_cpy,sep="")