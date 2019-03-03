# coding=utf-8
import aaa.string


class P:
    pass


class C(P):
    def __init__(self):
        self.foo = 'fo'
    pass


c = C()
print(C.__call__())
print(super(C,c))
print(P.__bases__)
print(C.__bases__)
a = C()
print(a.__class__())