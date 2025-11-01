var_dict={}
var_dict2=dict()

var_dict={'a':1}; var_dict['b']=24; print("var_dict: {}".format(var_dict))#var_dict={'a':1,'b':24}
var_dict2=var_dict.copy(); print("var_dict2: {}".format(var_dict2))#var_dict2={'a':1,'b':24}
del var_dict['a']; print("var_dict: {}".format(var_dict))#var_dict={'b':24}
var_dict.clear(); print("var_dict: {}".format(var_dict))#var_dict2={'a':1,'b':24}
#del var_dict; print(var_dict) #it should show error messages due to printing a None dictionary.

x=['a','b','c']
var_dict_fky=dict.fromkeys(x,1); print(var_dict_fky)
x=var_dict_fky.get('a'); print(x)
x=var_dict_fky.items(); print(x)
var_dict_fky.pop("a"); print(var_dict_fky)
x=var_dict_fky.popitem(); print(x)
x=var_dict_fky.setdefault('b'); print(var_dict_fky,x)
x=var_dict_fky.setdefault('a'); print(var_dict_fky,x)
var_dict_fky.update({'a':1}); print(var_dict_fky)
print(var_dict_fky,"",var_dict_fky.values())