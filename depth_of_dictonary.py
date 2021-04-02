def print_depth(d, start=0):
    for key, value in d.items():
        print(key, start + 1)
        if isinstance(value, dict):
            print_depth(value, start=start + 1)


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
    print_depth(a)
