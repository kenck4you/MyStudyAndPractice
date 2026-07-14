def look_for_key(box):
    for item in box:
        if type(item) == list:
            look_for_key(item)
        elif type(item) == str:
            return item
        else:
            pass

my_box = [[23, 2332], 23, 'KEY']
