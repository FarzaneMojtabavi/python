PRODUCTS=[]
import qrcode
def reed_from_database():
    f=open("database.txt","r")
    for line in f:
        result=line.split(",")
        my_dict={"code":result[0],"name":result[1],"price":result[2],"count":result[3]}
        PRODUCTS.append(my_dict)
    f.close()
    
def write_to_database():
    with open('database.txt', 'a') as f:
        last_product = PRODUCTS[-1] 
        line = f"{last_product['code']},
        {last_product['name']},
        {last_product['price']},
        {last_product['count']}\n"
        f.write(',')
        f.write(line)
def write_cimi(text,myfile):
    myfile.write(input(text))
    myfile.write(',')
def add_product():
    myfile=open('database.txt','a')
    myfile.write('\n')
    write_cimi('id: ',myfile)
    write_cimi('name: ',myfile)
    write_cimi('price: ',myfile)
    write_cimi('count: ',myfile)
    print('Successfully added to database.')
def show_menu():
    print('1- Add')
    print('2- Edit')
    print('3- Remove')
    print('4- Search')
    print('5- Show List')
    print('6- Buy')
    print('7- qrCode')
    print('8- Exit')

print("Welcome to farzane store")
print("Loading...")
reed_from_database()
print("Data loaded.")

def add():
    code=input("enter code: ")
    name=input("enter name: ")
    price=input("enter price: ")
    count=input("enter count: ")
    new_product={'code':code,'name':name,'price':price,'count':count}
    PRODUCTS.append(new_product)
    
def edit():
    show_list()
    select_update_product=input('Which product to edit? ')
    
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['code']==select_update_product:
            editfor=input("kodom mored?")
            if  PRODUCTS[i]['name']==editfor:
                PRODUCTS[i]['name']= input('Enter new name: ')
            elif PRODUCTS[i]['price']==editfor:
                PRODUCTS[i]['price'] = int(input('Enter new price: '))
            elif PRODUCTS[i]['count']==editfor:
                PRODUCTS[i]['count'] = int(input('Enter new count: '))
            print('Successfully added to database.')
            for product in PRODUCTS:
                print(product[i])
def remove():
    show_list()
    select_delete_product=input('Which product to remove? ')
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name']==select_delete_product:
            del PRODUCTS[i]
            break
        print(PRODUCTS)
        print('deleted')
        show_list()  
def search():
    user_input=input("type your keyword: ")
    for product in PRODUCTS:
        if product["code"]==user_input or product["name"]==user_input:
            print(product["code"],"\t\t",product["name"],"\t\t",product["price"])
            break
    else: print('not found')
def show_list():
    print("code\t\tname\t\tprice")
    for product in PRODUCTS:
        print(product["code"],"\t\t",product["name"],"\t\t",product["price"])
def buy():
    count=0
    sum=0
    factor={}
    factor_list=[]
    product_purchased=input('What do you buy? ')
    for i in range(len(PRODUCTS)):
        if PRODUCTS[i]['name']==product_purchased:
            def counts():
                count=int(input('How much do you buy from it? '))
                if count<=int(PRODUCTS[i]['count']):
                    sum=count*int(PRODUCTS[i]['price'])
                    print(PRODUCTS[i]['name'],'Number: ', count,'Price payable: ',sum)
                    factor['name']=PRODUCTS[i]['name']
                    factor['number']=count
                    factor['price']=sum
                    factor_list.append(factor)
                    print(factor_list)
                else:
                    print('Only', int(PRODUCTS[i]['count']) ,'are in stock') 
                    counts() 
            counts()
            
        elif len(factor_list)>0:
            something_else=input('it is registered. Do not want anything else?') 
            if something_else=='no':
                exit()
            elif something_else=='yes':
                buy() 
        else:     
            something_else=input('We do not have this product. Do not want anything else?') 
            if something_else=='no':
                exit()
            elif something_else=='yes':
                buy()
def qrCode():
    code=int(input("Pls Enter Product code :" ))
    for i in range(len(PRODUCTS)):
            if PRODUCTS[i]['code']==code:
                product='code : '+str(+PRODUCTS[i]['code'])
                +', name : '+PRODUCTS[i]['name']
                +', price : '+str(PRODUCTS[i]['price'])
                +', count : '+str(PRODUCTS[i]['count'])
                img=qrcode.make(product)
                img.save("product.png")

while True:
    show_menu()
    choice=int(input("enter your choise: "))
    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        remove()
    elif choice==4:
        search()
    elif choice==5:
        show_list()
    elif choice==6:
        buy()
    elif choice==7:
        qrCode()
    elif choice==8:
        write_to_database()
        exit(0)
    else:
        print("Enter correctly.")  
