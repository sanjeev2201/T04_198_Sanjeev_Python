def even_odd(lst):
    even_list = []
    odd_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return even_list, odd_list


n = range(1, 50)
Even_List, Odd_List = even_odd(n)
print("even Number:{}".format(Even_List))
print("Odd Number:{}".format(Odd_List))
