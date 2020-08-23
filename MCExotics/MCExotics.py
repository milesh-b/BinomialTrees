#!/usr/bin/env python3

"""
Title: MCExotics
Author: Milesh B
Github: https://github.com/milesh-b

"""


from scipy.stats import norm
import numpy as np

# European
#**********

class MCEuropean:
    def __init__(self,s0,vol,r,x,div,time,tree,sim):
        self.s0=float(s0)
        self.vol=float(vol)
        self.r=float(r)
        self.x=float(x)
        self.div=float(div)
        self.time=float(time)
        self.tree=int(tree)
        self.sim=int(sim)
        self.t=self.time/self.tree
        self.u=np.exp(self.vol*np.sqrt(self.t))
        self.d=1/self.u
        self.q=(np.exp((self.r-self.div)*self.t)-self.d)/(self.u-self.d)

    def call (self):
        payoff=[]
        for j in range(0,self.sim):
            stock=[self.s0]
            for i in range(0,self.tree):
                ran=np.random.uniform(0,1)
                if ran>(1-self.q):
                    stock.append(self.u*stock[-1])
                else:
                    stock.append(self.d*stock[-1])
            # Payoff European call
            payoff.append(max(0,stock[-1]-self.x))
        derivative=np.mean(payoff)*np.exp(-self.r*self.time)
        print(f'Call option value: {derivative:.2f}\n Input parameters:\ns0={self.s0}\nvol={self.vol}\nr={self.r}\nx={self.x}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}\nsim={self.sim}')

    def put (self):
        payoff=[]
        for j in range(0,self.sim):
            stock=[self.s0]
            for i in range(0,self.tree):
                ran=np.random.uniform(0,1)
                if ran>(1-self.q):
                    stock.append(self.u*stock[-1])
                else:
                    stock.append(self.d*stock[-1])
            # Payoff European Put
            payoff.append(max(0,self.x-stock[-1]))
        derivative=np.mean(payoff)*np.exp(-self.r*self.time)
        print(f'Put option value: {derivative:.2f}\n Input parameters:\ns0={self.s0}\nvol={self.vol}\nr={self.r}\nx={self.x}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}\nsim={self.sim}')

# Fixed Strike
#************
class MCFixed:
    def __init__(self,s0,vol,r,x,div,time,tree,sim):
        self.s0=float(s0)
        self.vol=float(vol)
        self.r=float(r)
        self.x=float(x)
        self.div=float(div)
        self.time=float(time)
        self.tree=int(tree)
        self.sim=int(sim)
        self.t=self.time/self.tree
        self.u=np.exp(self.vol*np.sqrt(self.t))
        self.d=1/self.u
        self.q=(np.exp((self.r-self.div)*self.t)-self.d)/(self.u-self.d)

    def call (self):
        payoff=[]
        for j in range(0,self.sim):
            stock=[self.s0]
            for i in range(0,self.tree):
                ran=np.random.uniform(0,1)
                if ran>(1-self.q):
                    stock.append(self.u*stock[-1])
                else:
                    stock.append(self.d*stock[-1])
            # Payoff Fixed call
            payoff.append(max(0,np.max(stock)-self.x))
        derivative=np.mean(payoff)*np.exp(-self.r*self.time)
        print(f'Call option value: {derivative:.2f}\n Input parameters:\ns0={self.s0}\nvol={self.vol}\nr={self.r}\nx={self.x}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}\nsim={self.sim}')

    def put (self):
        payoff=[]
        for j in range(0,self.sim):
            stock=[self.s0]
            for i in range(0,self.tree):
                ran=np.random.uniform(0,1)
                if ran>(1-self.q):
                    stock.append(self.u*stock[-1])
                else:
                    stock.append(self.d*stock[-1])
            # Payoff Fixed Put
            payoff.append(max(0,self.x-np.min(stock)))
        derivative=np.mean(payoff)*np.exp(-self.r*self.time)
        print(f'Put option value: {derivative:.2f}\n Input parameters:\ns0={self.s0}\nvol={self.vol}\nr={self.r}\nx={self.x}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}\nsim={self.sim}')

# Floating Strike
#***************

class MCFloat:
    def __init__(self,s0,vol,r,div,time,tree,sim):
        self.s0=float(s0)
        self.vol=float(vol)
        self.r=float(r)
        self.div=float(div)
        self.time=float(time)
        self.tree=int(tree)
        self.sim=int(sim)
        self.t=self.time/self.tree
        self.u=np.exp(self.vol*np.sqrt(self.t))
        self.d=1/self.u
        self.q=(np.exp((self.r-self.div)*self.t)-self.d)/(self.u-self.d)

    def call (self):
        payoff=[]
        for j in range(0,self.sim):
            stock=[self.s0]
            for i in range(0,self.tree):
                ran=np.random.uniform(0,1)
                if ran>(1-self.q):
                    stock.append(self.u*stock[-1])
                else:
                    stock.append(self.d*stock[-1])
            # Payoff Float call
            payoff.append(max(0,stock[-1]-np.min(stock)))
        derivative=np.mean(payoff)*np.exp(-self.r*self.time)
        print(f'Call option value: {derivative:.2f}\n Input parameters:\ns0={self.s0}\nvol={self.vol}\nr={self.r}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}\nsim={self.sim}')

    def put (self):
        payoff=[]
        for j in range(0,self.sim):
            stock=[self.s0]
            for i in range(0,self.tree):
                ran=np.random.uniform(0,1)
                if ran>(1-self.q):
                    stock.append(self.u*stock[-1])
                else:
                    stock.append(self.d*stock[-1])
            # Payoff Float Put
            payoff.append(max(0,np.max(stock)-stock[-1]))
        derivative=np.mean(payoff)*np.exp(-self.r*self.time)
        print(f'Put option value: {derivative:.2f}\n Input parameters:\ns0={self.s0}\nvol={self.vol}\nr={self.r}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}\nsim={self.sim}')

# Asian Fixed
#************

class MCAsianFixed:
    def __init__(self,s0,vol,r,x,div,time,tree,sim):
        self.s0=float(s0)
        self.vol=float(vol)
        self.r=float(r)
        self.x=float(x)
        self.div=float(div)
        self.time=float(time)
        self.tree=int(tree)
        self.sim=int(sim)
        self.t=self.time/self.tree
        self.u=np.exp(self.vol*np.sqrt(self.t))
        self.d=1/self.u
        self.q=(np.exp((self.r-self.div)*self.t)-self.d)/(self.u-self.d)

    def call (self):
        payoff=[]
        for j in range(0,self.sim):
            stock=[self.s0]
            for i in range(0,self.tree):
                ran=np.random.uniform(0,1)
                if ran>(1-self.q):
                    stock.append(self.u*stock[-1])
                else:
                    stock.append(self.d*stock[-1])
            # Payoff Asian Fixed call
            payoff.append(max(0,np.mean(stock)-self.x))
        derivative=np.mean(payoff)*np.exp(-self.r*self.time)
        print(f'Call option value: {derivative:.2f}\n Input parameters:\ns0={self.s0}\nvol={self.vol}\nr={self.r}\nx={self.x}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}\nsim={self.sim}')

    def put (self):
        payoff=[]
        for j in range(0,self.sim):
            stock=[self.s0]
            for i in range(0,self.tree):
                ran=np.random.uniform(0,1)
                if ran>(1-self.q):
                    stock.append(self.u*stock[-1])
                else:
                    stock.append(self.d*stock[-1])
            # Payoff Asian Fixed Put
            payoff.append(max(0,self.x-np.mean(stock)))
        derivative=np.mean(payoff)*np.exp(-self.r*self.time)
        print(f'Put option value: {derivative:.2f}\n Input parameters:\ns0={self.s0}\nvol={self.vol}\nr={self.r}\nx={self.x}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}\nsim={self.sim}')

#Asian Float
#***********

class MCAsianFloat:
    def __init__(self,s0,vol,r,div,time,tree,sim):
        self.s0=float(s0)
        self.vol=float(vol)
        self.r=float(r)
        self.div=float(div)
        self.time=float(time)
        self.tree=int(tree)
        self.sim=int(sim)
        self.t=self.time/self.tree
        self.u=np.exp(self.vol*np.sqrt(self.t))
        self.d=1/self.u
        self.q=(np.exp((self.r-self.div)*self.t)-self.d)/(self.u-self.d)

    def call (self):
        payoff=[]
        for j in range(0,self.sim):
            stock=[self.s0]
            for i in range(0,self.tree):
                ran=np.random.uniform(0,1)
                if ran>(1-self.q):
                    stock.append(self.u*stock[-1])
                else:
                    stock.append(self.d*stock[-1])
            # Payoff Asian Float call
            payoff.append(max(0,stock[-1]-np.mean(stock)))
        derivative=np.mean(payoff)*np.exp(-self.r*self.time)
        print(f'Call option value: {derivative:.2f}\n Input parameters:\ns0={self.s0}\nvol={self.vol}\nr={self.r}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}\nsim={self.sim}')

    def put (self):
        payoff=[]
        for j in range(0,self.sim):
            stock=[self.s0]
            for i in range(0,self.tree):
                ran=np.random.uniform(0,1)
                if ran>(1-self.q):
                    stock.append(self.u*stock[-1])
                else:
                    stock.append(self.d*stock[-1])
            # Payoff Asian Float Put
            payoff.append(max(0,np.mean(stock)-stock[-1]))
        derivative=np.mean(payoff)*np.exp(-self.r*self.time)
        print(f'Put option value: {derivative:.2f}\n Input parameters:\ns0={self.s0}\nvol={self.vol}\nr={self.r}\ndiv={self.div}\ntime={self.time}\ntree={self.tree}\nsim={self.sim}')





