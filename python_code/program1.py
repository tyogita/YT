#!/usr/bin/python

#find-pair-with-given-sum-array

arr = [8,7,2,5,3,1]
_sum = 10
flag = 0
for i in range(0, len(arr)-1):
    for j in range(i+1):
        if (arr[i]+arr[j]==_sum):
            print("Pair found" , arr[i] , arr[j])
            flag=1

if (flag==0):
    print("no pair found with sumi =",_sum)
print ("program completed")
