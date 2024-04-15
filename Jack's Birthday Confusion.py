from math import factorial
n=2048
k=1
v=(n-1)/n
while 1-factorial(n)/(factorial(n-k)* n**k ) < 0.75 :
    k+=1
    v*=(n-1)/n
print(k)
