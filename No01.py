import time 
l=time.time()
for i in range(10001):
    print(i)
r=time.time()
print(r-l)
mm=time.time()
mmm=[i for i in range(10001)]
print(mmm)
nn=time.time()
print(nn-mm)

