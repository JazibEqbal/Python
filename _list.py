def remove_duplicates(l):
    _set = set()
    # _l= []
    for item in l:
        if item not in _set:
            _set.add(item)

    print(list(_set))

_list= [1, 6, 7, 7, 7, 9, 9, 1, 6]
remove_duplicates(_list)