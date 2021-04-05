class A:
    def fun1(self):
        print("Inside Fun1 of class A")

    def fun2(self):
        print("Inside Fun2 of class A")


class B(A):
    def fun3(self):
        print("Inside Fun3 of class B")


class C:
    def fun4(self):
        print("Inside Fun4 of class C")


class D(A, C):
    def fun5(self):
        print("Inside Fun5 of class D")
