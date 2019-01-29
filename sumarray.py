def array_of_array_products(arr): 

""" arr = input product of everything except arr[i] 
for every i for empty case, return empty array 
if n=6 i=3 i keep track of the 
sum so far [1,2,[3],4,5] [_,_,] ? [,_, _] [1, 2, 3, 4, 5] ^ ^ ^ 
""" 
    if arr==[]: return arr 
    if len(arr)==1: return [] 
    num=len(arr)
    result=[0 for i in range(num)] 
    rollingProd=1 
    for i in range(1, num): 
    # product so far = for i in range(0, i) sum all the elements 
    # # product after that element = for i in range(i, n) sum all elements 
    # product to return = productbefore * productafter 
    rollingProd*=arr[i-1] 
    result[i]=rollingProd rollingProd=1 
    for i in range(num-1, 0, -1): 
        rollingProd*=arr[i] 
        result[i-1]*=rollingProd 
    return result