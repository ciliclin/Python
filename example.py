#!/usr/bin/python3

import os
import sys

print("===============Object reference==============")
a = 1
print("a=1, then a: ", a)
b = 5
print("b=5, then b: ", b)
b = a
print("b=a, then b: ", b)
a = 10
print("a=10, then a: ", a, " b: ", b)
print()

print("====================================")
cwd = os.getcwd()
print("Show current working directory: ", cwd)
print()

print("====================================")
test_path = ""
if test_path == "" and os.path.exists("/root/_github/Python"):
    test_path = "/root/_github/Python"
print("Check if the path /root/_github/Python is existed")
if test_path == "":
    print("test_path is NULL")
else:
    print(test_path, " is existed")
print()

print("================Logical operators====================")
five = 5
two = 2
zero = 0
null = 0

if False:
    ans = input("Type the result for \"five and two\": ")
    if(int(ans) == (five and two)):
        print("Correct")
    else:
        print("Wrong")

    print()

    ans = input("Type the result for \"two and five\": ")
    if(int(ans) == (two and five)):
        print("Correct")
    else:
        print("Wrong")

    print()

    ans = input("Type the result for \"zero and two\": ")
    if(int(ans) == (zero and two)):
        print("Correct")
    else:
        print("Wrong")

    print()

    ans = input("Type the result for \"two and zero\": ")
    if(int(ans) == (two and zero)):
        print("Correct")
    else:
        print("Wrong")

    print()

    ans = input("Type the result for \"two or five\": ")
    if(int(ans) == (two or five)):
        print("Correct")
    else:
        print("Wrong")

    print()

    ans = input("Type the result for \"five or two\": ")
    if(int(ans) == (five or two)):
        print("Correct")
    else:
        print("Wrong")

    print()

    ans = input("Type the result for \"zero or five\": ")
    if(int(ans) == (zero or five)):
        print("Correct")
    else:
        print("Wrong")

    print()

    ans = input("Type the result for \"five or zero\": ")
    if(int(ans) == (five or zero)):
        print("Correct")
    else:
        print("Wrong")

print()

print("==============Argument transfer===================")
print("==Immutable argument==")
def chgint(num):
    print("chgint num: ", num)
    num = 2
    print("chgint num: ", num)
    print("chgint a: ", a)
    return

a = 10
print("a: ", a)
    
chgint(a)
print("a: ", a)
print()

print("==Mutable argument==")
def chgname(name):
    name.append('asd')
    return

myname = [1, 2, 3]
print("myname: ", myname)

chgname(myname)
print("chgname myname: ", myname)
print()

print("============String Escapes===============")
print("1. Hello world!\nNice to meet you")
print("2. Hello world!\\\"\'Nice to meet you")
print("3. Hello world!\aNice to meet you")
print("4. Hello world!\bNice to meet you")
print("5. Hello world!\fNice to meet you")
print("6. Hello world!\tNice to meet you")
print("7. Hello world!\rNice to meet you")
print("8. Hello world!\vNice to meet you")

print()

print("==============String==================")
string = "this is wonderful world"
for index in range(0, 7, 2):
    print(string[index])
    
for char in string:
    print(char)

print()

print("====================================")
print()
