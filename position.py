def login(name,status):
    if name=='PG' and status==True:
        return "Login Success"
    else:
        return "Login Failed"


msg1=login('RG',False)
print(msg1)

msg2=login('SG',False)
print(msg2)

msg3=login('PG',True)
print(msg3)
