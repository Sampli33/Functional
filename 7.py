import functools
import json


def to_json(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = json.dumps(func(*args, **kwargs))
        return result

    return wrapper


@to_json
def list_generate():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


@to_json
def get_dict():
    return {'key': 1, 'name': 'John'}


@to_json
def summarizing(a, b, c):
    return a + b + c


json_list = list_generate()
print(json_list)
json_dict = get_dict()
print(json_dict)
total = summarizing(10, 5, 3.16)
print(total)

# Проверка на формат JSON

json_object = json.loads(json_list)
print(json_object)
json_object1 = json.loads(json_dict)
print(json_object1)
json_object2 = json.loads(total)
print(json_object2)
