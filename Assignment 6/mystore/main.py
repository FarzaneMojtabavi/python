from operator import index
from sre_constants import JUMP
from pyfiglet import Figlet
def search():
    name = input('enter the name of the product: ')
    t=1
    for i in range(len(products)):
        if products[i]['name']==name:
            print(products[i])
            t=0
    if t==1:
        print('not found')    
def edit_update():
    show_list()
    select_update_product=input('Which product to edit? ')
    for i in range(len(products)):
        if products[i]['name']==select_update_product:
            products[i]['name']= input('Enter new name: ')
            products[i]['price'] = int(input('Enter new price: '))
            products[i]['count'] = int(input('Enter new count: '))
            print('Successfully added to database.')
            print(products[i])
            

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

def buy():
    count=0
    sum=0
    factor={}
    factor_list=[]
    product_purchased=input('What do you buy? ')
    for i in range(len(products)):
        if products[i]['name']==product_purchased:
            def counts():
                count=int(input('How much do you buy from it? '))
                if count<=int(products[i]['count']):
                    sum=count*int(products[i]['price'])
                    print(products[i]['name'],'Number: ', count,'Price payable: ',sum)
                    factor['name']=products[i]['name']
                    factor['number']=count
                    factor['price']=sum
                    factor_list.append(factor)
                    print(factor_list)
                else:
                    print('Only', int(products[i]['count']) ,'are in stock') 
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
    data=myfile.read()
    product_list=data.split('\n')
    for i in range(len(product_list)):
        product_info=product_list[i].split(',')
        mydict={}
        mydict['id']=product_info[0]
        mydict['name']=product_info[1]
        mydict['price']=product_info[2]
        mydict['count']=product_info[3]
        products.append(mydict)
    print('welcome')
calculate_number_products=0    
def show_list():
    for i in range(len(products)):
        print(products[i],) 
    print('Number of product types: ',len(products))    
products=[]    
load()

f=Figlet(font='standard')
print(f.renderText('My Store'))

show_menu()
choise=int(input('please choose a number: '))
def delete():
    show_list()
    select_delete_product=input('Which product to remove? ')
    for i in range(len(products)):
        if products[i]['name']==select_delete_product:
            del products[i]
            # del myfile[i]['name']
            break
        print(products)
        print('deleted')
        show_list()   


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

if choise==1:
   add_product()
elif choise==2:
    edit_update()
elif choise==3:
    delete()
elif choise==4:
    search()
elif choise==5:
    show_list() 
elif choise==6:
    buy()
elif choise==7:
    exit('end')