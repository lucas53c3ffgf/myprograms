def factor(x):
    result = []
    for x in range(1,x+1):
        if x % 2 == 0:
            result.append(x)


N = input("Enter a number")
table = 
for N in range(2,N+1):
    table[N] = facotrs(n)







# single solution 
def collatz_seq(num):
    size = 1 
    start = num 
    while start > 1:
        if start % 2 == 0:
            start = start // 2 
        else:
            start *= 3 
            start += 1 
        size += 1 
    return size 

# method 2 
cache = {1:1}
def c_seq2(num):
    if num in chache: 
        size = 1 
        start = num 
        while start>1:
            if start & 2 == 0 :
                 

         start += 1
    if start in chche: 
        cache[num] = size + cache[start]
        return size = cache[start]
    else:
        size +=1 
    cache[num] = size 
    return cache[num]

