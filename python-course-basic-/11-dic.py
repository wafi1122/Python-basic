employee = {
    'name' : 'wafi',
    'age' : 34,
    'salary' : ' $100',

}
print(employee['name'],employee['age'])
for key in employee:
    print(key + " : " + str(employee[key]))