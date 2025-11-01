var_tuple=(1,2,3,4,5,'a','b','c',5,'c','c','c')

print(var_tuple,"\nvar_tuple[0]=",var_tuple[0],"\nvar_tuple[6]=",var_tuple[6])
x=var_tuple.count('c'); print("tuple.count(val) will record the number of val in tuple=",x,sep="")
x=var_tuple.index('c'); print("tuple.index(val) will show first occurrence of val=",x,sep="")