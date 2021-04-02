class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


def dict_depth(d, key='', start=0, li=[]):
    if not d:
        return []
    if isinstance(d, dict):
        for key, value in d.items():
            # print(key, start + 1)
            li.append(str(key) + ' ' + str(start + 1))
            if isinstance(value, dict):
                return dict_depth(value, key, start=start + 1)
            elif isinstance(value, Person):
                dict_depth(value.__dict__, start=start + 1)
        return li
    else:
        return []


if __name__ == '__main__':
    person_a = Person('user', 1, None)
    person_b = Person('user', 2, person_a)

    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user": person_b,
            }
        }
    }

    result_list = dict_depth(a)
    for i in result_list:
        print(i)
