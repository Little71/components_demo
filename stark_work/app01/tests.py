from django.test import TestCase

# Create your tests here.


# class  A(object):
#
#     x=12
#
#     def xxx(self):
#         print(self.x)
#
#
# class B(A):
#     y=5
#
# b=B()
# b.xxx()

#######################################

#
# class Person(object):
#     def __init__(self,name):
#         self.name=name
#
# alex=Person("alex")
#
# s="name"
#
#
# print(getattr(alex,s))

########################################

class Person(object):
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(self)
        print("eat....")

# 实例方法
# egon=Person("egon")
# egon.eat()

# 函数
# Person.eat(123)












