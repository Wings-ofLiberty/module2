my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number_value = (my_list[0])
list_length = len(my_list)
while list_length > 1:
    if number_value > -1:
        print (number_value)
        (list_length) = (list_length -1)
        del(my_list[0])
        number_value = (my_list[0])
        if number_value == 0:
            del (my_list[0])
            number_value = (my_list[0])
    if number_value < -1:
        break


