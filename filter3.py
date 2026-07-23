number=[1,2,3,4,5,6,7,8,9,10]
def verify(n):
    return n%2==0
print(list(filter(verify,number)))