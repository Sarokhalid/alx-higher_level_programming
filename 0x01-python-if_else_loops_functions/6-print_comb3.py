#!/usr/bin/python3
for i in range(10):
    for q in range(10):
        print("{}{}".format(i,q), end=", " if q < 9 else "\n")
