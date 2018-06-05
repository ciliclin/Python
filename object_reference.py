#!/usr/bin/env python3

x = "blue"
y = "red"
z = x

print(x,y,z)
z = y
print(x,y,z)
x = z
z = "black"
print(x,y,z)

print(x, type(x))

z = 123
print("z=123")
print("z =", z, type(z))

