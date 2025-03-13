
#while 1 == 1:
#    for d in range(0,100):
#        if(d % 2 == 0):
#            print (str(d) + " is even")
#        else:
#            print(str(d) + " is odd")


def test(name, *args):
    print(name)
    print(args)

test("Hallo", *(1,3,67,2))
