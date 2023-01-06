# hangman game
# import random
# words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock','engineer', 'toothpaste', 'shirmoz']
# word = random.choice(words) # clock
# joon = 3
# w=[]
# len_word = len(word)
# while joon > 0:
#     print('- ' * len(word)) # - - - - -
#     user_character = input() # s
#     if user_character in word:
#         print('yes')
#         len_word = len_word-1
#         w.append(user_character)
#         print("".join(w))
#         if len_word == 0:
#             print('bravo')
#             break
#     else:
#         joon = joon - 1
#         print(joon+1)
#         print('no')     
# *******************************************************************
# araye ba tol n va adad tasadofi gheyre tekrari
# listnumber=[]
# n=int(input('tedad: '))
# for i in range(n):
#     num=int(input('num: '))
#     if num not in listnumber:
#         listnumber.append(num)
# print(listnumber)    
# or
# araye ba adad tasadofi gheyre tekrari
# listnumber=[]
# while True:
#     n=int(input('n: '))
#     if n not in listnumber:
#         listnumber.append(n)
#     else:
#         print('error')  
#         break  
# print(listnumber)    
# *******************************************************************
# yek araye az karbar migire v moshakhas mikone sort has ya na.az kochik b bozorg
# listnumber=[]
# while True:
#     n=int(input('n: '))
#     listnumber.append(n)
#     if n==100:
#         break   
# for i in range(len(listnumber)-1):
#     if listnumber[i]<listnumber[i+1]:
#         s='yes'
#     else:
#         s='no'      
#         break     
# print(listnumber)
# print(s)
# *******************************************************************
# snake
# n=int(input())
# for i in range(n):
#     if i%2==0:
#         print('*',end='')
#     else:
#         print('#',end='')    
