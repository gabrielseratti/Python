def best_friend(t, a, b):
    return t.count(a)==t.count(a+b)
print(best_friend("we found your dynamite", "d", "y"))
#     lista = []
#     count = 0
#     for x in txt:
#         lista.append(x)
    
#     for y in lista:
#         if count < len(lista):
#             count += 1
#             if y != a:
#                 pass
#             elif count > len(lista):
#                 return False
#             else:
#                 if lista[count] != b:
#                     return False
#                 else:
#                     pass
#     return True     

# print(best_friend("we found your dynamite", "d", "y"))

        # if x == a:
        #     for y in txt:
        #         if y != b:
        #             return False
        #         else:
        #             return True

# def best_friend(txt, a, b):
#     count = 0
#     lista = []
#     for x in txt:
#         if x != ' ' and x != '"':
#             for y in txt:
#                 if y != ' ' and y != '"' and y != ',':
#                     strin = x + y
#                     lista.append(strin)

#     return lista

# print(best_friend("he headed to the store", "h", "e"))