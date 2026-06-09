import json
from functools import wraps
def grammar_doc(docstring: str):
    def decorator(func):
        @wraps(func)
        def wrapper(text: str):
            return func(text)
        wrapper.__doc__=docstring
        return wrapper
    return decorator
@grammar_doc("""
    -Present Perfect: Результат в настоящем.
    -Примеры: I have already done housework;
    -He has just done homework;
    -Have you done yet
""")
def check_present_perfect(text: str)->bool:
    return any(word in text.lower() for word in ["have", "has"])\
            and any(word in text.lower() for word in ["already", "just", "yet"])
@grammar_doc("""
    -Present Continous: Действие происходит в настоящем времени
    -Примеры: I am working  
    -I am not working
    -He is working
    -He is not working
    Are you working?
""")
def check_present_continuous(text: str)->bool:
    return any(word in text.lower() for word in ["is", "am", "are"])\
            and "ing" in text
@grammar_doc("""-Past Simple: Действие происходит в прошлом
-Примеры: I worked yesterday; 
-He was in Turkey 3 years ago...; 
-He went home.""")
def check_past_simple(text: str)->bool:
    return any(word in text.lower() for word in ["yesterday", "ago"]) or text.lower().endswith("ed")
@grammar_doc("""
-Future Simple: действие в будущем.
Примеры: I will study; He will go.
""")
def check_future_simple(text: str)->bool:
    return "will" in text.lower() or "shall" in text.lower()
@grammar_doc("""
    -Present Simple:Факты о человеке; 
    -Примеры: 
    -He studies English;
    -I buy cars. We don't eat burgers
""")
def check_present_simple(text: str)->bool:
    words=text.lower().split()
    return any(word.endswith("s") for word in words) or \
        any(word in words for word in ["does", "do", "don't", "doesn't"])
def run_checks(text: str):
    results={}
    checks=[check_present_perfect, check_present_continuous, check_past_simple, check_future_simple]
    for func in checks:
        results[func.__name__]=func(text)
    return results
with open('text/essay.txt', 'r', encoding='utf-8') as r:
    essay_text=r.read()
with open('words.json', 'r', encoding='utf-8') as n:
    vocabularies=json.load(n)
grammar_results=run_checks(essay_text)
word_results={}
count_found=0
for vocab_name, word_list in vocabularies.items():
    count_found=sum(1 for w in word_list if w.lower() in essay_text.lower())
    word_results[vocab_name]={"found":count_found, "required": 2, "pass": count_found>=2}
    if count_found<2:
        overall_pass=False
word_results["overall_pass"] = overall_pass
results={**grammar_results, **word_results}
with open('print.json', 'w', encoding='utf-8') as out:
    json.dump(results, out, ensure_ascii=False, indent=3)
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


