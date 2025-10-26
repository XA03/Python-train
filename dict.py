var_dict={}
var_dict2=dict()

var_dict={'a':1}; var_dict['b']=24; print(var_dict)#var_dict={'a':1,'b':2}
del var_dict['a']; print(var_dict)#var_dict={'b':2}
var_dict['a']=1; print(len(var_dict),str(var_dict))
del var_dict; print(var_dict)#it should show error messages due to printing a None dictionary.
