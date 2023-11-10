import random
words = ['book', 'tree', 'python', 'bag', 'umbrella', 'dog', 'clock', 'engineer', 'toothpaste', 'shirmoz']
word = random.choice(words) # clock
joon = 5
lenW=len(word)
while joon > 0:
    print('- ' * len(word)) # - - - - -
    user_character = input() # s
    user_character=user_character.lower()
    if user_character in word:
        print('yes')
        lenW=lenW-1
        if lenW==0:
            print('bordi')
            break
    else:
        joon = joon - 1
        print('no')     
