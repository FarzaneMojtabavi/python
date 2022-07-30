# re=real_number_______and_______im=imaginary_number
def show(x):        print(x['re'],'i+',x['im'])
def sum(a, b):      result = {};        result['re'] = a['re']+b['re'];     result['im'] = a['im'] + b['im'];       return result
def sub(a, b):      result = {};        result['re'] = a['re']-b['re'];     result['im'] = a['im'] - b['im'];       return result
def mul(a, b):      
    result = {};    result['re'] = (a['re']*b['re'])-(a['im']*b['im']);     
    result['im'] = (a['re'] * b['im'])+(a['im'] * b['re']);
    return result
a={'re':22,'im':4};      b={'re':2,'im':3}  ;show(sum(a,b)),     show(sub(a,b)),     show(mul(a,b))