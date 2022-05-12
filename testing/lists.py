list1 = ['test1', 'test2', 'test3']
list2 = ['test4', 'test5', 'test1']

for one in list1:
    print(f"one: {one}")
    for two in list2:
        print(f"two: {two}")
    if one == two:
        print("yep")