import json

 fp1=open('employee.json','r')

employee_list=json.load(fp1)
print(len(employee_list))

for emp in employee_list:
 print(emp['ename'])