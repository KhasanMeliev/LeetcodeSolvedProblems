def func(arr):
    res = 0
    for i in arr:
        divisor=0
        subRes = 0
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                if i//j==j:
                    divisor=10
                divisor+=2
                subRes=(j+i//j)+1+i
            if divisor>2:
                break
            
        if divisor==2:
            res+=subRes
        

    return res

print(func([21,4,7,16])) #32