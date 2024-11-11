import inspect


def introspection_info(obj):
    dict_1 = {}
    dir_obj = dir(obj)
    dict_1['type'] = type(obj)
    dict_1['attributes'] = [i for i in dir_obj if i[0] != '_']
    dict_1['methods'] = [i for i in dir_obj if i[0] == '_']
    dict_1['module'] = inspect.getmodule(obj)
    dict_1['module'] = inspect.getdoc(obj)
    return dict_1

class MyClass():
    '''возраст человека'''

    def __init__(self, age):
        self.age = age

    def pass_func(self):
        pass


man = MyClass(33)

print(introspection_info(man))
