# # task 1
# def func(s):
#         return ''.join([c*2 for c in s])
# user_input = str(input("-> "))
# print(func(user_input))   
# solved:



# task 2
# def func(file):
#         with open(file, 'r+') as file:
#             c = file.read()
#         t = c.lower().split().count("the")
#         return t
# file = "notes.txt"
# s = func(file)
# print(f"The word 'the' occurs {s} times.")
# solved:




# task 3
# def func(file):
#         with open(file, 'r') as file:
#             c = file.read()
#         s = c.split()
#         t = sum(1 for word in s if word.endswith('e'))
#         return t
# file = "notess.txt"
# e = func(file)
# print(f"The number of words ending with 'e' is {e}.")
# solved:



# task 4
# def func(file):
#         with open(file, 'r+') as file:
#             c = file.read()
#         w = c.split()
#         s1 = w.count("this")
#         s = w.count("these")
#         return s1, s
# file = "my_file.txt"
# s1, s = func(file)
# print(f"The word 'this' occurs {s1} times.")
# print(f"The word 'these' occurs {s} times.")
# solved:




# task 5
# def func(n):
#         if n < 0:
#             return "invalid"
#         elif n == 1:
#             return "Google"
#         else:
#             return f"G{'o' * n}gle"
# user_input = int(input("-> "))
# print(func(user_input))
# solved:


# task 6
# def func(s, t):
#     return any(s in i for i in t)

# list_input = input("Enter a list of words separated by commas: ")
# lis = list_input.split(',')
# lis = [word.strip() for word in lis]
# search_string = input("Enter the string to search for: ")
# print(func(search_string, lis))
# solved:




# task 7
# def func(n):
#     s = n // 6
#     t = n + s
#     return t
# user_input = int(input("-> "))
# print(func(user_input)) 
# solved:



# task 8
# def func(s):
#     if len(s) == 0:
#         return ""
#     return s[0] + s[-1]
# user_input = str(input("-> "))
# print(func(user_input))
# solved:



# task 9
# def func(a):
#     return a.endswith('s')

# user_input = str(input("-> "))
# print(func(user_input))
# solved: