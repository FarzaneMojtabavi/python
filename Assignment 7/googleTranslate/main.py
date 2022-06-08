from pyfiglet import Figlet
f=Figlet(font='standard')
print(f.renderText('Google Translate')) 
def Show_Menu():
        print('1- add new word')
        print('2- translation english2persian')
        print('3- translation persian2english')
        print('4- exit')
# Show_Menu()
my_translate=open('database_translate.txt','r')
words=[]
def load():
        print('Loading...')
        data=my_translate.read()
        Word_list_array=data.split('\n')
        for i in range(len(Word_list_array)):
                word_info=Word_list_array[i].split(',')
                words.append({
                'english': word_info[0],
                'persian': word_info[1],
                })
        print('Upload completed successfully.')        
load()
def add_word():   
    english=input('english: ')
    persian=input('persian: ')
    words.append({'english':english,'persian':persian})
    print('successfully-added new word')
def save_exit():
    f=open('database_translate.txt','w')
    for i in range(len(words)):
        row =str(words[i]['english'])+','+words[i]['persian']+'\n'
        f.write(row)
    print('Save words in the database translate. exit')
    f.close()
    exit()    
def search_English_to_Persian_translation():
    user_keyword = input('enter word: ')
    to_find=1
    for i in range(len(words)):
        if words[i]['english']==user_keyword:
            print(words[i]['persian'])
            to_find=0
    if to_find==1:
        print('not found')    
def search_Persian_to_English_translation():
    user_keyword = input('enter word: ')
    to_find=1
    for i in range(len(words)):
        if str(words[i]['persian'])==user_keyword:
            print(words[i]['english'])
            to_find=0
    if to_find==1:
        print('not found')           
while True:
        Show_Menu()
        number=int(input('select from menu: '))
        if number==1:
                add_word()
        elif number==2:
                search_English_to_Persian_translation()
        elif number==3:
                search_Persian_to_English_translation()
        elif number==4:
                save_exit()