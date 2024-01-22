def read_from_file():
    global words_bank
    f=open("Translate.txt","r")
    temp=f.read().split("\n")
    words_bank=[]
    for i in range(0,len(temp),2):
        my_dict={"en":temp[i],"fa":temp[i+1]}
        words_bank.append(my_dict)
    f.close()
def translate_english_to_persian():
    user_text=input("enter your english text: ")
    user_words=user_text.split(" ")
    output=""
    print(user_words)
    for user_word in user_words:
        for word in words_bank:
            if user_word==word["en"]:
                output=output+word["fa"]+" "
                break
        else:
            output=output+user_word+" "
    print(output)
def translate_persian_to_english():
    user_text=input("enter your persian text: ")
    user_words=user_text.split(" ")
    output=""
    print(user_words)
    for user_word in user_words:
        for word in words_bank:
            if user_word==word["fa"]:
                output=output+word["en"]+" "
                break
        else:
            output=output+user_word+" "
    print(output)
def show_menu():
    print("welcome to my translate")
    print("1-translate english to persian")
    print("2-translate persian to english")
    print("3-add a new word to database")
    print("4-exit")

read_from_file()
while True:
    show_menu()
    choice=int(input("enter your choice: "))
    if choice==1:
        translate_english_to_persian()
    elif choice==2:
        translate_persian_to_english()
    elif choice==3:
        en_add = input("English: ")
        fa_add = input("farsi: ")
        new_word = {"en":en_add, "fa":fa_add}
        file = open('translate.txt', 'a') 
        file.write("\n"+en_add+"\n"+fa_add)
        file.close()
        print("updated successfully!")
    elif choice==4:
        exit()