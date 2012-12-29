import types


class A(object):

    def __init__(self):
        print "HOLA"
        self.a = [1,2,3,4,5]

    def set(self,f):
        self.f = types.MethodType(f,self,A)

    def app(self):
        self.f()



def f(self):
    print self.a[0]

a = A()
a.set(f)
a.app()