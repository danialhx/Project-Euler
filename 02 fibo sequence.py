def fiboCounter(num):
    n1 = 1
    n2 = 1
    nth = 1
    arr = [n1,n2]
    arr2 = []
    total = 0
    total2 = 0
    i = 0
    
    for i in range(0,num+1):
        
        nth = n1 + n2
        n1 = n2
        n2 = nth
        i = i + 1
        arr.append(nth)
        #print(arr)
        #print(nth, 'lolo')
        
        if (arr[i]%2 == 0):
            total2 = total2 + arr[i]
            arr2.append(arr[i])
            print (arr2, "----", total2)
            
            
fiboCounter(20)