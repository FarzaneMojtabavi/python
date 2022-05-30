from functools import total_ordering
from itertools import count
from operator import index
from sre_constants import JUMP
from numpy import product
from pyfiglet import Figlet
f=Figlet(font='standard')
print(f.renderText('My Store'))

def search_product():
    user_keyword = input('enter id or name: ')
    t=1
    for i in range(len(products)):
        if products[i]['name']==user_keyword or str(products[i]['id'])==user_keyword:
            print(products[i])
            t=0
    if t==1:
        print('not found')    

def show_edit_menu():
    print('0- id')    
    print('1- name')  
    print('2- price')  
    print('3- count')     
    print('4- end edit')  
def edit_update():
    show_list()
    select_update_product=input('Which product to edit? ')
    for i in range(len(products)):
        if products[i]['name']==select_update_product:
            while True:
                show_edit_menu()
                product_information=int(input('Which information will change? \t please choose from edit menu:'))
                if product_information==0:
                    products[i]['id']= input('Enter new id: ')
                elif product_information==1:    
                    products[i]['name']= input('Enter new name: ')
                elif product_information==2:    
                    products[i]['price'] = int(input('Enter new price: '))
                elif product_information==3:    
                    products[i]['count'] = int(input('Enter new count: '))
                elif product_information==4:
                    print('The product editing operation is completed.')
                    break    
                else:
                    print('value error')
                print('Successfully added to database.')
                print(products[i])       

def add_product():   
    id=int(input('id: '))
    name=input('name: ')
    price=float(input('price: '))
    count=int(input('count'))
    products.append({'id':id,'name':name,'price':price,'count':count})
    print('successfully-added new product')
def save_exit():
    f=open('database.txt','w')
    for i in range(len(products)):
        row =str(products[i]['id'])+','+products[i]['name']+','+str(products[i]['price'])+','+str(products[i]['count'])+'\n'
        f.write(row)
    f.close()
    exit()    


def buy():
    basket=[]
    while True:
        id=int(input('please enter product id:'))
        for i in range(len(products)):
            if products[i]['id']==id:
                count=int(input('please enter count:'))
                if products[i][count]>=count:
                    basket.append({
                        'name':products[i]['name'],
                        'price':products[i]['price'],
                        'count':count
                    })
                    products[i]['count']-=count
                    print('add successfully')  
                else:
                    print('not exist')
                    print('we have ',products[i]['count'],'from this product')    
        choise=input('Do you want continue? (y/n)')
        if choise=='N'or choise=='n':
            break       
    print(basket)
    total_price=0
    for i in range(len(basket)):
        total_price+=basket[i]['price']*basket[i]['count']
    print('total price:',total_price)             

def show_menu():
    print('1-add product')
    print('2-edit product')
    print('3-delete product')
    print('4-search')
    print('5-show list')
    print('6-buy')
    print('7-exit')

def load():
    print('loading...')
    myfile=open('database.txt','r')
    product_list=myfile.read().split('\n')
    for i in range(len(product_list)):
        product_info=product_list[i].split(',')
        products.append({
            'id':product_info[0],
            'name':product_info[1],
            'price':int(product_info[2]),
            'count':int(product_info[3])
            })
    print('welcome')
def show_list():
    for i in range(len(products)):
        print(products[i],) 
    print('Number of product types: ',len(products))    
products=[]    
load()

def delete_product():
    show_list()
    select_delete_product=input('Which product to remove? ')
    for i in range(len(products)):
        if products[i]['name']==select_delete_product:
            products.pop(i)
            break
        print(products)
        print('product removed')
    show_list()   


def write_cimi(text,myfile):
    myfile.write(input(text))
    myfile.write(',')


while True:
    show_menu()
    choise=int(input('please choose a number: '))
    if choise==1:
        add_product()
    elif choise==2:
        edit_update()
    elif choise==3:
        delete_product()
    elif choise==4:
        search_product()
    elif choise==5:
        show_list() 
    elif choise==6:
        buy()
    elif choise==7:
        save_exit()