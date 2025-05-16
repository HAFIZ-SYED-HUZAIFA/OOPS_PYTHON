class A :
    def show(Self):
        print("i am A")
class B(A):
    
    def show(Self):
        print("i am B")

class C(A):
        def show(Self):
            print("i am C")

class D(B,C):
     pass

d = D()
d.show()
print(D.mro())