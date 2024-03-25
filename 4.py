import json

json_string = input()

py_list = json.loads(json_string)
py_list.sort(key=lambda x: x[1], reverse=True)
print(py_list)
