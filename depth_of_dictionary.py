def dict_depth(d, key='', start=0, li=[]):
    if not d:
        return []
    if isinstance(d, dict):
        for key, value in d.items():
            # print(key, start + 1)
            li.append(str(key) + ' ' + str(start + 1))
            if isinstance(value, dict):
                return dict_depth(value, key, start=start + 1)
        return li
    else:
        return []


if __name__ == '__main__':
    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }
    result_list = dict_depth({})
    for i in result_list:
        print(i)
