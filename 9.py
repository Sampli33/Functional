import functools
import json
import xmltodict
import yaml


def to_format(output_format=None):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            if output_format == 'JSON':
                return json.dumps(result)
            elif output_format == 'XML':
                return xmltodict.unparse({'root': result}, pretty=True, full_document=False)
            elif output_format == 'YAML':
                return yaml.safe_dump(result)
            else:
                return json.dumps(result)

        return wrapper

    return decorator


@to_format()
def parameterless():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


@to_format('JSON')
def to_json():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


@to_format('XML')
def to_xml():
    return {"first_name": "Ivan", "last_name": "Ivanov", "city": "Moscow", "date": '1999'}


@to_format('YAML')
def to_yaml():
    return {'key': 1, 'name': 'John'}


print(parameterless())
print(to_json())
print(to_xml())
print(to_yaml())
