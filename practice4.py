class parent():
    def func1(self):
        print("This is parent class function")

class child(parent):
    def func2(self):
        print("This is child class function")

c=child()
c.func1()
c.func2()