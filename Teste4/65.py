def divisible_by_last(n):
    previous_number = 0
    bool_list = []
    for x in str(n):
        if previous_number != 0:
            if int(x) % int(previous_number) == 0:
                    previous_number = int(x)
                    bool_list.append(True)
            else:
                previous_number = int(x)
                bool_list.append(False)
        else:
             previous_number = int(x)
             bool_list.append(False)
    return bool_list

print(divisible_by_last(62487005))