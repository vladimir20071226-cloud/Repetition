import json
# def log_action(func):
#     def wrapper(*args, **kwargs):

# class Book:
#     def __init__(self, name, book):
#         self.name=name
#         self.book=book
# b=Book("Steven King", "It")
# print(b.name)
# class User:
#     def __init__(self, name:str):
#          a=input("Введи символ:")
#          self.name = name if a in name else 'Anonymous'
#          self.a=a
#     @staticmethod
#     def validate_email(email: str) -> bool:
#              return "@"  in email
# print(User.validate_email("vovagmail.com"))
# print(User.validate_email("vova@gmail.com"))
#
# # with open("new.json", "r", encoding="utf-8") as f:
# #     a=json.load(f)
# #     single_list=[]
# #     for i in a:
# #         if i["age"]>15:
# #             i=i["name"]
# #             single_list.append(i)
# #     print(single_list)
# #with open ("abc.json", "w", encoding="utf-8") as w:
# #    json.dump(single_list, w, indent=3)
# with open("another.json", "r", encoding="utf-8") as r:
#      y=json.load(r)
#      dictionary={}
#      for m in y:
#          religion = m.get("religion")
#          country = m.get("country")
#          dictionary.setdefault(religion, []).append(country)
#      print(dictionary)
# with open ("one_else.json", "w", encoding="utf-8") as q:
#      json.dump(dictionary, q, indent=3)

# with open ("text/text.txt", "r", encoding="utf-8") as f:
#     lines=f.readlines()
#     num_lines=len(lines)
#     num_words=0
#     num_letters=0
#     for line in lines:
#         num_words+=len(line.split())
#         num_letters=len(line)-line.count(" ")-line.count("\n")
#     print(f"Количество букв:{num_letters}")
#     print(f"Количество строк:{num_lines}")
#     print(f"Количество слов:{num_words}")
# def func(m, n):
#     for i in range(m, n):
#         if i%17==0 or i%3==0 and i%5==0 or i%10==9:
#             print(i)
# func(1, 20)
# a=int(input("Введите число:"))
# dictionary={}
# #for i in range(a):
# #     a_1=input("Введите слово:")
# #     a_2 = input("Опишите слово:")
# #     dictionary[a_1]=a_2
# # print(dictionary)
# # b=input("Введите число:")
# for i in range(a):
#     a_1=input().split(' ')
#     dictionary[a_1[0]]=a_1[1]
# print(dictionary)
# word=input("Введите:")
# d=dictionary.get(word, "Не то слово")
# print(d)


