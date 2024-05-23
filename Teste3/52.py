def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False

# def comp(array1, array2):
#     if array1 is None or array2 is None:
#         return False
#     else:
#         for x in array1:
#             array1.remove(x)
#             if x*x in array2:
#                 array2.remove(x*x)
#             else:
#                 return False
		
#         return True

print(comp([121, 144, 19, 161, 19, 144, 19, 11] , 
		   [121, 14641, 20736, 361, 25921, 361, 20736, 361]))