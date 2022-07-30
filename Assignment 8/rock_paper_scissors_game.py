import random
options=['Rock','Paper','Scissor']
scores={'user':0,'computer':0}
def user_wins():
    print('user wins')
    scores['user']+=1 
def computer_wins():
    print('computer wins')
    scores['computer']+=1
def result():
    print('__result:__________________________') 
    print('user:',user_choice)      
    print('computer:',computer_choice)    
    print('__Score:__________________________') 
    print('computer:' ,scores['computer'])      
    print('user:' ,scores['user'])
    print('==================================') 
print('_____________________________Start Game _____________________________')     
for i in range(4):
    computer_choice=random.choice(options)
    print('computer:',computer_choice)  
    user_choice=input('play the game: ')
    if (user_choice=='Rock' and computer_choice=='Paper') or (user_choice=='Paper' and computer_choice=='Scissor') or (user_choice=='Scissor' and computer_choice=='Rock'):
        computer_wins()
        result()
    elif (user_choice=='Paper' and computer_choice=='Rock') or (user_choice=='Scissor' and computer_choice=='Paper')or (user_choice=='Rock' and computer_choice=='Scissor'):
        user_wins()    
        result()
    else:
        print('equal')
        result()
if scores['computer']>scores['user']:
    print('game winner: Computer /// score: 4 /',scores['computer'])
elif scores['computer']<scores['user']:    
    print('game winner: User /// score: ',scores['user'],'/ 4')
elif scores['computer']==scores['user']:
    print('equal /// score: User:',scores['user'],'/ 4  and Computer:',scores['computer'],'/ 4')