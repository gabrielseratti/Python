def increment_string(strng):
    head = strng.rstrip('0123456789')
    return head
    # if strng[-1].isalpha():
    #     return strng + '1'
    # else:
    #     return strng[:-1] + f'{(int(strng[-1]) + 1)}'
    

print(increment_string('foobar910'))
    # str = ''
    # count = -1
    # for x in strng:
    #     count += 1
    #     try:
    #         int(x)
    #         if count == len(strng) - 1:
    #             str += strng[-1] + 1
                
    #     except:
    #         str += x


    # return str

