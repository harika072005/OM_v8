def smart_div(func):
    def inner(a,b):
        if b==0:
            print("can't Divide by zero")
        else:
            return func(a,b)
        return inner  
@ smart_div
def cla_div(a,b):
    print(a/b)


print("GM")    
cla_div(10,5)
    
cla_div(10,0)
print("GM")
