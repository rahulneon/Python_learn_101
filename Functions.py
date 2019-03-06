from unittest.test.testmock.testpatch import function


def test():
    print("testing funtions")

test()


def test2(a):
    print(a*2)

test2(256848)

def test3(a,b,c):

    d=a+b; print(d*c)

test3(3,3,3)

def give(a,b):
    c=a+b
    return c


def take(c,d):
    e=d+give(int(input("enter a")),int(input("enter b"))) *c
    return e

print(take(4,5))