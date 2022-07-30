def operation_sum_sub(a,x,y,b):
    if b=='+':
        a['s']=x['s']+y['s']
        a['m']=x['m']+y['m']
        a['h']=x['h']+y['h']
    elif b=='-':
        a['s']=x['s']-y['s']    
        a['m']=x['m']-y['m']
        a['h']=x['h']-y['h']
#______________________________________________________________        
def operation_bets(operation,dictionary,ifdic,lowof,increase):
    if operation=='sum':
        if dictionary[ifdic]>=60:
            dictionary[lowof]-=60
            dictionary[increase]+=1       
    elif operation=='sub':        
        if dictionary[ifdic]<0:
            dictionary[lowof]-=1
            dictionary[increase]+=60
#______________________________________________________________              
def sum(x,y):
    result={}
    operation_sum_sub(result,x,y,'+')
    operation_bets('sum',result,'s','s','m')
    operation_bets('sum',result,'m','m','h') 
    return result  
#______________________________________________________________      
def sub(x,y):
    result={}
    operation_sum_sub(result,x,y,'-')
    operation_bets('sub',result,'s','m','s') 
    operation_bets('sub',result,'m','h','m') 
    return result     
#______________________________________________________________      
def time_second_to_hours():
    second=int(input('second: '))
    print_tile('hours')
    print('hours: ',end='')
    result = {}
    result['h'] = second // 3600
    result['m'] = (second % 3600) // 60
    result['s'] = (second % 3600) % 60
    return result
#______________________________________________________________      
def time_hours_to_second():
    result = {}
    result['h'] = int(input('hour: '))
    result['m'] = int(input('minute: '))
    result['s'] = int(input('second: '))
    second = ( int(result['h']) * 3600 ) + ( int(result['m']) * 60 ) + ( int(result['s']) ) 
    print_tile('second')
    print('second:' ,second)
#______________________________________________________________      
def print_tile(text):
    print('____',text,'____')
#______________________________________________________________      
def print_line(text):
    print('=',text,'==========')    
#______________________________________________________________      
def show(x):
    print(x['h'],':',x['m'],':',x['s'])
#______________________________________________________________      
t1={'h':2,'m':30,'s':45}
t2={'h':3,'m':17,'s':40}
#______________________________________________________________  
print_line('sum')
show(t1)
show(t2)
print_tile('Sum')
show(sum(t1,t2))
print_line('sub')
show(t1)
show(t2)
print_tile('Sub')
show(sub(t1,t2))
print_line('second')
show(time_second_to_hours())
print_line('hourse')
time_hours_to_second()
#______________________________________________________________  