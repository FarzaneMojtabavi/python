class kasr:
    def __init__(self,s,m):
        self.sorat=s
        self.makhraj=m
    def mul(self,mehman):
        result=kasr(None,None)
        result.sorat=self.sorat*mehman.sorat
        result.makhraj=self.makhraj*mehman.makhraj
        return result
    def div(self,mehman):
        result=kasr(None,None)
        result.sorat=self.sorat*mehman.makhraj
        result.makhraj=self.makhraj*mehman.sorat
        return result
    def sum(self,mehman):
        result=kasr(None,None)
        result.sorat=self.sorat*mehman.makhraj+self.makhraj*mehman.sorat
        result.makhraj=self.makhraj*mehman.makhraj
        return result
    def dec(self,mehman):
        result=kasr(None,None)
        result.sorat=self.sorat*mehman.makhraj-self.makhraj*mehman.sorat
        result.makhraj=self.makhraj*mehman.makhraj
        return result
    def show(self):print(self.sorat,'/',self.makhraj)    
a=kasr(3,5);b=kasr(4,3);a.show();b.show() 
print('____mul____');   c=a.mul(b);   c.show()
print('____div____');   d=a.div(b);   d.show()
print('____sum____');   e=a.sum(b);   e.show()
print('____dec____');   f=a.dec(b);   f.show()