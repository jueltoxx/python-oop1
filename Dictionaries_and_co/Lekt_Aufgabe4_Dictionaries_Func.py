sample_dict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

def returnSalary(dict):
    name = dict.get('name')
    salary = dict.get('salary')
    return name, salary

result = returnSalary(sample_dict)
print(result)
