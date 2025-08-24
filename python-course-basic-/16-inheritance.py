class A:
    def __init__(self):
        print('a')


    def method1(self):
        print('method1')
    def method2(self):
        print('method2')
class B(A):
    def __init__(self):
        print('c')


    def method3(self):
        print('method3')
    def method4(self):
        print('method4')

class C(A ,B):
    def __init__(self):
        super().__init__()
        print('c')


    def method5(self):
        print('5')
# a = A()
# b = B()

# b.method1()
# b.method2()

c = C()