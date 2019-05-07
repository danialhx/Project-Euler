print "\nProject Euler 1\n\nIf we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. next try to 1000"

def multiples(num) :
    sum = 0
    arr1 = []
    for i in range(0, num):
        if i % 3 == 0 or i % 5 == 0 :
            #print(i)
            sum += i
            arr1.append(sum)
            print (arr1 , i)
    print(sum)

multiples(10)
