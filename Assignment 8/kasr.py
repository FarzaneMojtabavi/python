from unittest import result
def mul(x,y):
    result={}
    result['s']= x['s']*y['s']
    result['m']= x['m']*y['m']
    return result
def div(x,y):
    result={}
    result['s']= x['s']*y['m']
    result['m']= x['m']*y['s']
    return result    
def sum(x,y):
    result={}
    result['s']=x['s']*y['m'] + x['m']*y['s'] 
    result['m']=x['m']*y['m']      
    return result
def dec(x,y):
    result={}
    result['s']=x['s']*y['m'] - x['m']*y['s'] 
    result['m']=x['m']*y['m']      
    return result    
def show(x):
    print(x['s'],'/',x['m'])    
    
a={'s':2,'m':3}   
b={'s':5,'m':4} 

show(mul(a,b))
show(sum(a,b))
show(dec(a,b))
show(div(a,b))