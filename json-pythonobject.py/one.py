import json
emp_json_str = '''
    [{"eid":101,"ename":"RG","avali":true}
    {"eid":102,"ename":"SG","avali":false}
    {"eid":103,"ename":"PG","avali":false}
    {"eid":104,"ename":"Modi","avali":true}
     {"eid":105,"ename":"Amith","avali":true}
    ]
'''
emp_list =json.loads(emp_json_str)
print(emp_list)


    
