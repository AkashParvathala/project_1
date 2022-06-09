def binary(arr,l,h,n):
    while(l<=h):
        mid=(l+h)//2
        if(arr[mid]==n):
            return mid
        elif(arr[mid]>n):
           return binary(arr,l,mid-1,n)
        else:
            return binary(arr,mid+1,h,n)
    return -1
arr=[1,2,4,5,6,9,10]
print(arr)
n = int(input("Enter your number to search in the given list  : "))
x=binary(arr,0,len(arr)-1,n)
if(x!=-1):
    print(f"The  index value of {n} at",x)
else:
    print("The given number Not Found") 
