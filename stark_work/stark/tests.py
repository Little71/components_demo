from django.test import TestCase

# Create your tests here.


class A:
    def funa(self):
        return 1


a = A()


func = getattr(a,'funa')
print(func())