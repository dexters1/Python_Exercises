class A():
    def __init__(self, ime, prezime):
        self.ime = ime
        self.prezime = prezime
    def __mul__(self, b):
        return self.ime + b.ime

def makeFunc(f):
    def funcInside(*args, **kwargs):
        print("Hello from func")
        return f(*args, **kwargs)
    return funcInside

@makeFunc
def test():
    print ("5")

test()

B = A("Igor", "ILIC")
C = A("Igir", "ILIC")

print(B*C)
