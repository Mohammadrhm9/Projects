def remove_all(lst, value):
    while (value in lst):
        index = lst.index(value)
        lst.pop(index)
        if (index < len(lst)):
            lst.insert(index, None)

lst = [1 , '2' , 3.654 , 4 , 5 , 6 , 5 , "Mohammad Amin Rahimi", 8 , 9 , 5]
remove_all(lst, 5)
print(lst)
