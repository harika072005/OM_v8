def login_req(func):
    def inner(name,status):
        if status==False:
            print("Login Req")
        else:
            return func(name,status)
        return inner    
def home_page(name,status):
    print("home_page")
def product_page(name,status):
    print("product_page")
@login_req
def profile_page(name,status):
    print("profile_page")
@login_req    
def order_page(name,status):
    print("order_page")

home_page("RG",True)
product_page("RG",False)
login_req("RG",False)
login_req("RG",False)    
    