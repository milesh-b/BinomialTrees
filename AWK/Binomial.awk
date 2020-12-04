# Author: Milesh B
# Github: https://github.com/milesh-b
# AWK script to calculate a Vanilla Put option.
# This script can be altered to suit any option.

BEGIN{
#s0=144
#vol=0.315573
#r=0.19062
#x=144
#div=0
#time=1.5
#tree=97
#sim=10000
srand(seed)

t=time/tree
u=exp(vol*sqrt(t))
d=1/u
q=(exp((r-div)*t)-d)/(u-d)

payoff=0

# Tree construction

for(i=1;i<=sim;i++){
stock[i,1]=s0

for(j=2;j<=tree+1;j++){

ran=rand()

if(ran>(1-q)){
stock[i,j]=stock[i,j-1]*u

}

else{
stock[i,j]=stock[i,j-1]*d}

}

# Find Max(0,stock-x) For European put option
if ((x-stock[i,j-1]) > 0){
payoff+= (x-stock[i,j-1])}
}

derivative=(payoff/(i-1))*exp(-r*time)
print "Value of option= ", derivative
}


