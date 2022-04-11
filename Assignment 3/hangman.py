import random
import colorama
from colorama import Fore
words = ['Tree', 'wall', 'flower', 'butterfly', 'fish',
         'cinema', 'buy', 'pay', 'wings', 'happy', 'dinner']
word_rand = random.choice(words)
n_live = 3
exits = 0
len_word = len(word_rand)
while n_live > 0:
    print('- ' * len(word_rand))
    user_character = input()
    if user_character in word_rand:
        print('yes')
        len_word = len_word-1
        if len_word == 0:
            print(Fore.BLUE,'bravo')
            break
    else:
        n_live = n_live - 1
        exits = exits+1
        print('no')
