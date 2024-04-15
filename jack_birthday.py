n=2048
k=1
v=(n-1)/n
while 1-v < 0.5 :
    k+=1
    v*=(n-1)/n
print(k)
