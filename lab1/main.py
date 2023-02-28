import sys

def my_printf(string_param,param):
    a=string_param.find("#k")
    if a==-1:
        print(string_param)
    else:
        print(string_param[0:a])
        print(param)
        print(string_param[a+2:len(string_param)])




