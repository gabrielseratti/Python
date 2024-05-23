def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string


# def solution(n):
#     romans = ''
#     unidades = 0
#     for x in sorted(str(n), reverse=True):
#         if unidades == 0:
#             if x == 1:
#                 romans += 'I';
#             if x == 2:
#                 romans += 'II';
#             if x == 3:
#                 romans += 'III';
        

#     return

print(solution(1330))