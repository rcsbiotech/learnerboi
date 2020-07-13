#!/usr/bin/env python

a = 15
b = 10
c = 12
d = 9
f = 16

if all(a > x for x in(b, c, d)):
        print("It works!")
