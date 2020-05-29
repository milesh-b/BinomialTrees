"""
Title: BinomialTrees
Author: Milesh B
Github: https://github.com/milesh-b

"""

import numpy as np
np.set_printoptions(precision=4)


class CRR:
    def __init__(self,s0,vol,time,tree):
        self.s0=float(s0)
        self.vol=float(vol)
        self.time=float(time)
        self.tree=int(tree)
        self.dim=int(2**self.tree)
        self.t=self.time/self.tree
        self.u=np.exp(self.vol*np.sqrt(self.t))
        self.d=1/self.u
    def price(self):        
        price_tree=np.zeros([self.dim,self.tree+1])
        price_tree[0,0]=self.s0

        for i in range(0,(self.tree)):
            count=0
            for j in range(0,int(self.dim/2)):
                price_tree[count,i+1]=price_tree[j,i]*self.u
                count=count+1
                price_tree[count,i+1]=price_tree[j,i]*self.d
                count=count+1

        return (price_tree)


class European(CRR):
    def __init__(self,s0,vol,rf,x,div,time,tree):
        super().__init__(s0,vol,time,tree)
        self.rf=float(rf)
        self.x=float(x)
        self.div=float(div)
        self.q=(np.exp((self.rf-self.div)*self.t)-self.d)/(self.u-self.d)

# European Call
#*************
    def call_show(self):        
        opt_tree=np.zeros([self.dim,self.tree+1])
        for j in range(0,self.dim):
            opt_tree[j,self.tree]=max(0,(CRR.price(self)[j,self.tree])-self.x)

        for i in range(self.tree,0,-1):
            count=0
            for j in range(0,int(self.dim/2)):
               opt_tree[j,i-1]=np.exp(-self.rf*self.t)*(self.q*opt_tree[count,i]+(1-self.q)*opt_tree[count+1,i])
               count= count+2
        return(opt_tree)
       
    def call(self):
        self.val=European.call_show(self)[0,0]
        print(f'Call option value: {self.val:.2f}\nInput parameters:\ns0={self.s0}\nvol={self.vol}\nrf={self.rf}\nx={self.x}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}')

# European Put
#*************
    def put_show(self):        
        opt_tree=np.zeros([self.dim,self.tree+1])
        for j in range(0,self.dim):
            opt_tree[j,self.tree]=max(0,(self.x-CRR.price(self)[j,self.tree]))

        for i in range(self.tree,0,-1):
            count=0
            for j in range(0,int(self.dim/2)):
               opt_tree[j,i-1]=np.exp(-self.rf*self.t)*(self.q*opt_tree[count,i]+(1-self.q)*opt_tree[count+1,i])
               count= count+2
        return(opt_tree)

    def put(self):
        self.val=European.put_show(self)[0,0]
        print(f'Put option value: {self.val:.2f}\nInput parameters:\ns0={self.s0}\nvol={self.vol}\nrf={self.rf}\nx={self.x}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}')
        
        
class American(CRR):
    def __init__(self,s0,vol,rf,x,div,time,tree):
        super().__init__(s0,vol,time,tree)
        self.rf=float(rf)
        self.x=float(x)
        self.div=float(div)
        self.q=(np.exp((self.rf-self.div)*self.t)-self.d)/(self.u-self.d)

# American Call
#*************
    def call_show(self):
        opt_tree=np.zeros([self.dim,self.tree+1])
        for j in range(0,self.dim):
            opt_tree[j,self.tree]=max(0,(CRR.price(self)[j,self.tree]-self.x))

        for i in range(self.tree,0,-1):
            count=0
            for j in range(0,int(self.dim/2)):
                option_val=np.exp(-self.rf*self.t)*(self.q*opt_tree[count,i]+(1-self.q)*opt_tree[count+1,i])
                price_val=CRR.price(self)[j,i-1]-self.x
                if CRR.price(self)[j,i-1]>0:
                     opt_tree[j,i-1]= max(option_val,price_val)
                count=count+2

        return (opt_tree)

    def call(self):
        self.val=American.call_show(self)[0,0]
        print(f'Call option value: {self.val:.2f}\nInput parameters:\ns0={self.s0}\nvol={self.vol}\nrf={self.rf}\nx={self.x}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}')   

# American Put
#*************
    def put_show(self):
        opt_tree=np.zeros([self.dim,self.tree+1])
        for j in range(0,self.dim):
            opt_tree[j,self.tree]=max(0,(self.x-CRR.price(self)[j,self.tree]))

        for i in range(self.tree,0,-1):
            count=0
            for j in range(0,int(self.dim/2)):
                option_val=np.exp(-self.rf*self.t)*(self.q*opt_tree[count,i]+(1-self.q)*opt_tree[count+1,i])
                price_val=self.x-CRR.price(self)[j,i-1]
                if CRR.price(self)[j,i-1]>0:
                     opt_tree[j,i-1]= max(option_val,price_val)
                count=count+2

        return (opt_tree)

    def put(self):
        self.val=American.put_show(self)[0,0]
        print(f'Put option value: {self.val:.2f}\nInput parameters:\ns0={self.s0}\nvol={self.vol}\nrf={self.rf}\nx={self.x}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}')
