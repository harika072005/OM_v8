numbers =[10,20,30,40]
def add_one(num):
    return num+1

map_obj= map(add_one, numbers)
new_numbers =list(map_obj)
print(new_numbers)