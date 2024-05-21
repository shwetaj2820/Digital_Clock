#PYTHON DOCUMENTATION FOR LEETCODE
import math
#Variables are typed dynamically
n=0
print("n =",n)

#multiple variable assignments
n,m,x,y = 1,2.567,False, None  #None means 'NULL'

#increment / decrement :
n=12
n=n+1 #allowed
n += 1 #allowed
# n++  not allowed
print(n)

#if statements:
n=1
if n>1:
    print("n>1")
elif n==2:
    print("n==2")
else:
    print("n==1")

#while loop
n=9
while n>0:
    print(n)
    n-=1

#for loop
print("for loop1")
for i in range(5):
    print(i)
    i=i+1 #output : 0 1 2 3 4

print("for loop2")
for i in range(2,5):
    print(i)
    i=i+1 #output : 2 3 4

print("for loop3")
for i in range(5,1,-1): # -1 is used for decrementing i
    print(i)
    i=i+1 #output : 5 4 3 2

#division: (decimal by default)
print(5/2) # 2.5
print(5//2) # 2
print(-3/2) # -1.5
print(-3//2) # -2
print(int(-3//2)) # -2

#modulus:
print(10%3) #1
print(-10%3) #2 .. unexpected output
print(math.fmod(-10,3)) # -1.0

print(math.floor(3/2)) #1
print(math.ceil(3/2)) #2
print(math.sqrt(2)) #1.414235...
print(math.pow(2,3)) #8.0

#max and min integers (python numbers are infinite so they never overflow )
print(float("inf"))
print(float("-inf"))
#numbers are always less than infinity
print(math.pow(2,200)<float("inf"))

#ARRAYS (called lists in python)
arr = [1,2,3]
print(arr)
#dynamic array
arr.append(4)
print(arr)
arr.pop()
print(arr)
arr.insert(1, 7) # 1 is the index and 7 is the element
print(arr)
arr[0] = 100 #reassingmment is possible
print(arr)

#initialize arr of size n with default value of 1
n=5
arr = [1] * n
print(arr)
print(len(arr))

# -1 is not out of bounds. It gives the last value
arr = [1,2,3,4]
print(arr[-1], arr[-2], arr[-3], arr[-4])

# sublists (slicing)
print(arr[1:3]) #output is from index 1 to 2
print(arr[0:3]) #index 0 to 3 hence entire array

#unpacking - assignning the array elements to variables
a, b,c = [1,2,3]
print(a,b,c)

#loop through arrays
nums = [2,4,5]
 #using index
for i in range(len(nums)):
    print(nums[i])

#without index
for i in nums:
    print(i)

#with index and value
for i, n in enumerate(nums): #i is index and n is value.
    print(i,n)

#loop through multiple arrays simultaneously(with unpacking)
nums1 = [1,3,5]
nums2 = [4,5,6]
for n1, n2 in zip(nums1,nums2):
    print(n1,n2)

#reversing an array
nums1 = [1,2,3]
nums1.reverse()
print(nums1)

#sorting array:
arr = [100,1,2,3,4]
arr.sort()
print(arr)
arr.sort(reverse = True)
print(arr)

#sorting list of strings (alphabetically)
arr = ['a','x','c','b']
arr.sort()
print(arr)

#custom sort (by length of string)
arr = ["anc","fk","fkghw","d","dfhsk","wefx"]
arr.sort(key = lambda x: len(x))
"""key = lambda x: len(x): This specifies a key function that is used to determine the sorting order.
lambda x: This is an anonymous function (a function defined without a name) that takes one argument x.
len(x): This is the body of the lambda function. It returns the length of the string x."""
print(arr)

#list comprehension
arr = [i for i in range(5)] #arr = [0,1,2,3,4]
print(arr)

arr = [i+i for i in range(5)] #arr = [0,2,4,6,8]
print(arr)

# 2D lists
arr = [[0]*4 for i in range(4)]
print(arr)

#strings:(similar to arrays)
s = "abc"
print(s[0:2]) #slicing : "ab"

#strings are immutable
#s[0]='A' produces error (TypeError)

s += "def"
print(s) #abcdef

#string <-> integer conversion
print(int("123") + int("123"))
print(str(123) + str(123))


#finding ascii value of a character
print(ord("a")) #ascii value = 97

#combine a list of strings(with empty delimitor)
strings = ["ab","cd"]
print(" ".join(strings))
print(",".join(strings))

#queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3) #append from right
print(queue)

queue.popleft() #pop from left
print(queue)

queue.appendleft(1) #append from left
print(queue)

queue.pop() #pop()means pop from right
print(queue)

#HASHSET - searching in constant time
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)
print(len(mySet))

#checking if value present or not in the hashset:
print(1 in mySet) 
print(2 in mySet)
print(3 in mySet)
mySet.remove(2)
print(mySet)

#list to set:
print(set([1,2,3,3,3]))

#set comprehension
mySet = {i for i in range(5)}
print(mySet)

#dictionary (hashmap)
myMap = {}
myMap["a"] = 12
myMap["b"] = 34
print(myMap)
print(len(myMap))
myMap["a"] = 56 #modifying values of keys
print(myMap['a']) #we can use " or ' 
print("a" in myMap) #check if key is present/not
myMap.pop("a")
print(myMap)

myMap={'a':78,'b':8} #method 2 : initializing hashmap
print(myMap)

#dictionary comprehecsion
myMap={i:2*i for i in range(3)} # i represents key and 2*i represents value
print(myMap)

print("looping through map")
for val in myMap.values():
    print(val) #prints values

for key in myMap:
    print(key,myMap[key]) #prints keys,values

for key,val in myMap.items():
    print(key,val) #prints keys,values

print("tuples (immutable)  are like arrays")
tup = (1,2,3)
print(tup)
print(tup[0])
print(tup[-1]) #prints last element

#modification is not allowed: tup[0]=3 wrong

#use of tuples: as a key for hashmap/hashset
myMap = {(1,2):3} #mapping the pair of keys (1,2) to 3
print(myMap[(1,2)]) # printing values

mySet = set()
mySet.add((1,2)) #adding tuple in set
print((1,2) in mySet)

#list cannot be key_ hence list is unhashable
#not allowed: mySet = {[1,2]:3}; mySet = [[1,2]:3]

#HEAPS:
import heapq
minHeap = []
heapq.heappush(minHeap,3)
heapq.heappush(minHeap,2)
heapq.heappush(minHeap,4)
print(minHeap)

#min is always at index 0
print(minHeap[0])

while len(minHeap):
    print("heap value:",heapq.heappop(minHeap))

#maxheap is not by default; work around is to use min heap and multiply by -1 when push and pop
maxHeap = []
heapq.heappush(maxHeap,-3)
heapq.heappush(maxHeap,0)
heapq.heappush(maxHeap,-9)

#maximum element is always at index 0 in the maxheap
print(-1 * maxHeap[0])

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))

#build heap from initial values:
arr = [2,1,5,3,8,0]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr)) #output : 0 1 2 3 5 8

#functions:
def myFun(n,m):
    return n*m

print(myFun(3,4))

#nested functions have access to outer variables
def outer(a,b):
    c = 'c'

    def inner():
        return a+b+c
    
    return inner()
print(outer("a","b"))

#can modify objects but not reassign (unless using nonlocal keyword)
print("using helper functions")
def double(arr,val):
    def helper():
        #modifying array(works)
        for i,n in enumerate(arr):
            arr[i] *= 2

        #will only modify val in the helper scope
        #val *= 2

        #this will modify val outside helper scope
        nonlocal val
        val *= 2

    helper()
    print(arr,val)
nums=[1,2]
val=3
double(nums,val) 

#CLASS:
class MyClass:
    #constructor
    def __init__(self,nums):
        #creating member variables
        self.nums = nums
        self.size = len(nums)

    #self keyword is always required as parameter
    def getLength(self):
        return self.size
    
    def getDoubleLength(self):
        return 2*self.getLength()
    

