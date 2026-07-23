def outer():
    print("outer function started")

    def login():
        print("Login Success")
    def logout():
        pass
    def inner():
        print("Inner Function")

    return inner
    

inner=outer()
print(inner)
print(type(inner))
inner()
inner()