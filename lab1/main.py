#!/usr/bin/env python3
import sys

def my_printf(string_param,param):
    a=string_param.find("#k")
    if a==-1:
        print(string_param,end="")
    else:
        print(string_param[0:a],end="")
        print(param,end="")
        print(string_param[a+2:len(string_param)],end="")


my_printf("Hello #k world","param")

# data=sys.stdin.readlines()
#
#
# for i in range(0,len(data),2):
#     my_printf(data[i].rstrip(),data[i+1].rstrip())




