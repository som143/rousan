# import json
# li = [[[[[
#          { "id" : "qwerty",
#             "nestednestedlist" : [
#                 { "id" : "xyz", "keyA" : "blah blah blah" },
#                 { "id" : "fghi", "keyZ" : "blah blah blah" }],
#             "anothernestednestedlist" : [
#                 { "id" : "asdf", "keyQ" : "blah blah" },
#                 { "id" : "yuiop", "keyW" : "blah" }] 
#          } 
#     ]]]]]
# # print(li[0][0])
# # while type(li)==list:
# #     li = li[0]

# # def get_item(input):
# #     if type(input[0])!=list:
# #         return input[0]
# #     else:
# #         return get_item(input[0])


# # print(get_item(li))
# def recursive_dict(v):
#     if isinstance(v, dict):
#         return v
#     for val in v:
#        return recursive_dict(val)
        
# print(recursive_dict(li))
