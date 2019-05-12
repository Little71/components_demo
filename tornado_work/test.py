class C:
    def f1(self):
        super().f1()

class B:
    def f1(self):
        print('B')

class A(C):
    def f1(self):
        super().f1()

class Foo(A,B):
    def f1(self):
        super().f1()

Foo.__mro__



