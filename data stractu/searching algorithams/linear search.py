#linear search in python 
#Sequential Search: In this, the list or array is traversed sequentially and every element is checked. For example: Linear Search.



a = [40,50,9,45,92,775,0]
#asking input integer from user
b  = int(input('enter searching element'))
for i in range(len(a)):
    if a[i]==b:
        print('item found in  index number of ',i)
        break    
       
else:
    print ('not found')     
       
