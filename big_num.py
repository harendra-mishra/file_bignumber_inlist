def big_number(list):
    big = 0
    big_count = 0
    letter = " "
    for num in list[:1]:
        big = num[1]
        letter = num[0]
        for numb in list[1:]:
            if numb[1] > big:
                big = numb[1]
                letter = numb[0]

    for num in list:
        if num[1] == big:
            big_count += 1

    if big_count > 1:
        return print("more than one big number in the list")
    else:
        return print(f'[{letter}, {big}]')
        # print(letter)
        
list1 = [["a", 9], ["b", 6], ["c", 4] , ["d", 3]]
list2 = [["a", 9], ["b", 6], ["c", 9] , ["d", 3]]
list3 = [["a", 9], ["b", 6], ["c", 9] , ["d", 3], ["e", 10]]
list4 = [["a", 24], ["b", 76], ["c", 79] , ["d", 34], ["e", 102]]

big_number(list1)
big_number(list2)
big_number(list3)
big_number(list4)