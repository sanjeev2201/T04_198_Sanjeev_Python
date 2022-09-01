'''List properties'''

'''
List properties:
==================
# 1. List is mutable
# 2. List allows duplicate elements
# 3. Maintains Insertion order
# 4. List will allow both homogeneous and heterogenous data
# 5. Follows indexing mechanism while storing elements(Sequence)
'''
#Exercise 1: Reverse a list in Python
#[500, 400, 300, 200, 100]
list1 = [100, 200, 300, 400, 500]
print("************* First way ***********************")
list1.reverse()
print(list1)
print("****************** second way ************************")
list1 = [100, 200, 300, 400, 500]
for i in list1[ : :-1]:
    print(i,end=",")
print()
print("****************** Third way ************************")
list1 = [100, 200, 300, 400, 500]
i=len(list1)-1
list2=[]
while(i>=0):
    x=list1[i]
    list2.append(x)
    i-=1
print(list2)
"Exercise 2: Concatenate two lists index-wise"
print()
#output:['My', 'name', 'is', 'Kelly']
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
newlist=zip(list1,list2)
for val1,val2 in newlist:
    obj="".join(val1+val2)
    print(obj,end=",")
print()
print("************** second way**********")
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result=[i+j for i,j in zip(list1,list2)]
print(result)

print("************** Third way**********")
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result=list(map(lambda i,j:i+j,list1,list2))
print(result)


#Concatenate two lists in the following order
#output=['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result=[i+j for i in list1 for j in list2]
print(result)

""" output:
10 400
20 300
30 200
40 100"""
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for i,j in zip(list1,list2[ : :-1]):
    print("{} {}".format(i,j))

"""Remove empty strings from the list of strings"""
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in list1:
    if i=="None":
        continue
    else:
        print(i,end=" ")

"""You have given a Python list. Write a program to find value 20 in the list, 
        and if it is present, replace it with 200.
        Only update the first occurrence of an item."""
print("*"*50)
print("*           first way           *")
list1 = [5, 10, 15, 20, 25, 50, 20]
for i in range(len(list1)):
    if list1[i]==20:
        list1[i]=200
print(list1)
print("*      second way                 *")
list1 = [5, 10, 15, 20, 25, 50, 20]
index=list1.index(20)
list1[index]=200
print(list1)

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)

#Given a Python list, write a program to remove all occurrences of item 20.
print("****************** First way **************")
list1 = [5, 20, 15, 20, 25, 50, 20]
for i in list1:
    if i==20:
        continue
    print(i, end=" ")
print()
print("****************** second way **************")
list1 = [5, 20, 15, 20, 25, 50, 20]
for i in list1:
    if i!=20:
        print(i, end=" ")
print()
print("****************** third way **************")
list1 = [5, 20, 15, 20, 25, 50, 20]
res=[i for i in list1 if i!=20]
print(res)
print("****************** fourth way **************")
list1 = [5, 20, 15, 20, 25, 50, 20]
while 20 in list1:
    list1.remove(20)
print(list1)
print("********* first way *****************")
list1=['a','b','c','d','e']
list2=[20,40,60,80,100]
dict={}
for i in range(len(list1)):
    dict[list1[i]]=list2[i]
print(dict)
print("********* second way *****************")
list1=['a','b','c','d','e']
list2=[20,40,60,80,100]
dict={k:v for k,v in zip(list1,list2)}
print(dict)

print("****************** first way *****************")
list1= {'a': 20, 'b': 40, 'c': 60, 'd': 80, 'e': 100}
dict={}
for k,v in list1.items():
    dict[v]=k
print(dict)

print("****************** second way *****************")
list1= {'a': 20, 'b': 40, 'c': 60, 'd': 80, 'e': 100}
dict={}
for k,v in list1.items():
    dict.update({v:k})
print(dict)

list1 = {'a': 20, 'b': 40, 'c': 60, 'd': 80, 'e': 100}
key=[]
value=[]
for k,v in list1.items():
    key.append(k)
    value.append(v)
print(key)
print(value)

list1 = [10, 20, 30, 40, 50]
res={i:i**2 for i in list1}
print(res)

""" Write a Python program to sum all the items in a list"""
list1 = [10, 20, 30, 40, 50]
sum=0
for i in list1:
    sum+=i
print("sum of items in list:",sum)
"""Write a Python program to get the largest number from a list."""
list1=[1, 2, -8, 0,4,9,-9]
max_no=list1[0]
for i in list1:
    if i>=max_no:
        max_no=i
print("max number in list:",max_no)
"""Write a Python program to count the number of strings
 where the string length is 2 or more 
 and the first and last character are same from a given list of strings."""
list1=['abc', 'xyz', 'aba', '1221','11','121']
counter=0
for i in list1:
    if len(i)>=2:
        if i[0]==i[-1]:
            counter+=1
print("count of data:",counter)

list1=['abc', 'xyz', 'aba', '1221','11','121']
counter=0
for i in list1:
    if len(i)>=2 and list1[0]==list1[-1]:
            counter+=1
print("count of data:",counter)


"""Write a Python program to get a list, 
sorted in increasing order by the last element 
in each tuple from a given list of non-empty tuples"""
list1= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

""" Remove duplicates from a list """
a = [10,20,30,20,10,50,60,40,80,50,40]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
print("*********** second way *****************")
a = [10,20,30,20,10,50,60,40,80,50,40]
b=set(a)
c=list(b)
print(c)

#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
"Expected Output : ['Green', 'White', 'Black']"
list1= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for i in range(len(list1)):
    if i !=0 and i!= 4 and i!= 5:
        print(list1[i],end=" ")
print("************ line no 215**************")
"""Find the second largest number in a list"""
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
lst=[]
for i in a:
    if i  not in lst:
        lst.append(i)
for i in range(len(lst)-1,0,-1):
    for j in range(i):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)
print("second largest number:{}".format(lst[-2]))
print("************ second method *******************")
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
a=set(a)
a=list(a)
a.sort()
print(" second largest number:",a[-2])

"""Write a Python program to get the difference between the two lists"""
list1 = [1, 3, 5, 7, 9]
list2=[1, 2, 4, 6, 7, 8]
lst=list(set(list1)^set(list2))
print(lst)

#Write a Python program to convert a list of characters into a string.
lst=['P','Y','T','H','O','N']
s=""
for i in lst:
    s=s+"".join(i)
print(s)

#Replace the last element in a list with another list
list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]
list1[-1: ] = list2
print(list1)

"Write a Python program to combine two given sorted lists using heapq module"
list1 = [ 1, 3, 5, 7, 9, 11]
list2 = [0, 2, 4, 6, 8, 10]
lst = list1 + list2
for i in range(len(lst)-1,0,-1):
    for j in range(i):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)

"Sum of elements"

list1 = [ 1, 3, 5, 7, 9, 11]
sum=0
for i in list1:
    sum+=i
print("sum of element",sum)

"multiply of elements"
list1 = [ 1, 3, 5, 7, 9, 11]
mul=1
for i in list1:
    mul=mul*i
print("multiply in list element:",mul)
"Largest number from list"
list1 = [ 1, 3, 5, 7, 9, 11]
max_no=list1[0]
for i in list1:
    if i>max_no:
        max_no=i
print("largest number in list:",max_no)
"Smallest number from list"
list1 = [-7,12,1, 3, 5, 7, 9, 11]
min_no=list1[0]
for i in list1:
    if i<min_no:
        min_no=i
print("minimum no in list:",min_no)

"Remove duplicates"
list1 = [-7,12,1, 3, 5, 7, 9, 11,-7,12,5]
new_list=[]
for i in list1:
    if i not in new_list:
        new_list.append(i)
print("new list:",new_list)

"Find common element from 2 lists"
list1 = [ 1, 3, 5, 7, 9, 11]
list2 = [-7, 12, 1, 3, 5, 7, 9, 11, -7, 12, 5]
for i in list2:
    if i in list1:
        print(i,end=" ")
print()
print("      second way         ")
list1 = [ 1, 3, 5, 7, 9, 11]
list2 = [-7, 12, 1, 3, 5, 7, 9, 11, -7, 12, 5]
new_list=list(set(list1) & set(list2))
print(new_list)

"Remove specified index from list and print"
list1 = [-7, 12, 1, 3, 5, 7, 9, 11, -7, 12, 5]
list1.pop(5)
print(list1)

list1 = [-7, 12, 1, 3, 5, 7, 9, 11, -7, 12, 5]
del list1[5]
print(list1)

print("************ second way **************")
list1 = [-7, 12, 1, 3, 5, 7, 9, 11, -7, 12, 5]
for i in range(len(list1)):
    if i==5:
        continue
    print(list1[i],end=" ")
print()
"Remove even elements and print list"
list1 = [-7, 12, 1, 3, 5,2,18,24, 7, 9,88, 11, -7, 12, 5]
result=[i for i in list1 if i%2==0]
print("even number:",result)

"List of characters into string"
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
for char in s:
    print(char,end="")

print()
"Difference betweeen 2 lists"
li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]
new_list=list(set(li1)-set(li2))+list(set(li2)-set(li1))
print(new_list)

"Frequency of elements"
list1 = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
d={}
for i in list1:
    d[i] = d.get(i, 0)+1
for k,v in d.items():
    print("\t {} element is {} times".format(k, v))

"Count the number of elements in a list within a specified range"
list1 = [10,20,30,40,40,40,70,80,99]
count = 0
for i in list1:
    if i>=40 and i<=100:
        count+=1
print("count element exit between 40 and 100: ",count)

"Check a list contains sublist"
test_list = [9, 4, 5, 8, 10]
sub_list = [10, 5, 4]
result=False
if set(sub_list).issubset(set(test_list)):
    result=True
if result:
    print("yes,list2 is subset of list1")
else:
    print("No,list2 is not subset of list1")

test_list = [9, 4, 5, 8, 10]
sub_list = [10, 5, 4,11]
result=False
if set(sub_list).issubset(set(test_list)):
    result=True
if result:
    print("yes,list2 is subset of list1")
else:
    print("No,list2 is not subset of list1")

"Variable unique identification number"
a=[10,20,30,40]
for i in a:
    print(i,type(i),id(i))

"Finding common items from two lists"
list1 = [9, 4, 5, 8, 10]
list2 = [10, 5, 4]
for i in list1:
    if i in list2:
        print(i,end=" ")
print()
" Converting multiple integers into single integer "
l = [11, 33, 50]
for i in l:
    print(i,end="")
print()
print("***************** second way***********")
list1=[11,33,50]
x=int("".join(map(str,list1)))
print("single integer:",x)

"Create multiple list"
listA = ['Mon', 'Tue', 'Wed']
listB = ['2 pm', '11 am','1 pm']
listC = [1, 3, 6]
newlist=listA + listB + listC
print(newlist)


"Find missing and additional values in two lists"
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
list3=list(set(list1)-set(list2))
print("additional value in list1:",list3)
list4=list(set(list2)-set(list1))
print("additional value in list2:",list4)
list5=list(set(list1) & set(list2))
print("common value in list1 and list2:",list5)

"Split a list into different variables"



" Generate group of five consecutive numbers in a list "
newlist1=[[5*i + j for j in range(1,6)] for i in range(5)]
print(newlist1)

" Convert a pair of values into a sorted unique array "
ltp = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
newlist=list(set().union(*ltp))
print(newlist)
"Insert an element before each element of a list"
color = ['Red', 'Green', 'Black']
newlist = [v for elt in color for v in ('c',elt)]
print(newlist)

color = ['Red', 'Green', 'Black']
for elt in color:
    print('c',elt)

"Write a Python program to print a nested lists (each list on a new line) using the print() function."
colors = [['Red'], ['Green'], ['Black']]
result='\n'.join([str(i) for i in colors])
print(result)

"Convert list to list of dictionaries"
key=['a','b','c','d']
val=[100,200,300,400]
d={}
for i in range(len(key)):
    d[key[i]]=val[i]
print(d)
"Sort a list of nested dictionaries"


"Split a list every Nth element"
data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
step=3
result=[data[i: :step] for i in range(step)]
print(result)

"Create a list with infinite elements"
lst=[None]*5
lst[0]=12
lst[1]=23
lst[2]=25
lst[3]=30
print(lst)
"Concatenate elements of a list"
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]
for i in test_list2:
    test_list1.append(i)
print(test_list1)


"Remove key values pairs from a list of dictionaries"
original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
result=[{k:v for k,v in d.items() if k!='key1'} for d in original_list]
print(result)


"Convert a string to a list"
words = 'geeks'
result=[word for word in words]
print(result)

"Check if all items of a list is equal to a given string"
inputdata=['Geeks', 'Geeks', 'Geeks', 'issss', ]
data=inputdata[0]
result=False
for item in inputdata:
    if item != data:
        result =True
        break
if result:
    print("items in list is not same")
else:
    print("items  in list is same")

"Create a list of empty dictionaries"
emptydic=[{} for i in range(5)]
print(emptydic)

"Print a list of space-separated elements"
testlist = [1, 2, 3, 4, 5, 6]
for i in testlist:
    print(i,sep=",")

"Insert a given string at the beginning of all items in a list"
inputlist = ['A', 'B', 'C']
inputstr = 'Team'
inputstr+='% s'
result=[inputstr % i for i in inputlist]
print(result)

"Iterate over two lists simultaneously"
num = [1, 2, 3]
color = ['red', 'while', 'black']
value = [255, 256,196]
for a,b,c in zip(num,color,value):
    print(a,b,c)


"How to access a dictionary key by index in Python"
a_dictionary = {"a": 1, "b": 2, "c":3}
print(list(a_dictionary))

"Find the list in a list of lists whose sum of elements is the highest"



"Find all the values in a list are greater than a specified number"
data=[10,20,40,50,63,89]
result=[i for i in data if i>25]
print(result)

"Write a Python program to extend a list without append."
x = [10, 20, 30]
y = [40, 50, 60]
y[ :0]=x
print(y)
"Get the depth of a dictionary"
dict={'a':1, 'b': {'c':'geek'}}
str_dict=str(dict)
counter=0
for i in str_dict:
    if i==":":
        counter+=1
print("Depth of dictionary:",counter)

"Check if all dictionaries in a list are empty or not"
dict={}
res=bool(dict)
print(" dictionary is not empty:",res)
res=not bool(dict)
print("Dictionary is empty:",res)

"A list contains group of strings.Convert each word to capital letter and print"
print("\n first way")
listA = ['Mon', 'Tue', 'Fri','Sun']
res=list(map(lambda x:x.upper(),listA))
print(res)
print("\nsecond way")
listA = ['Mon', 'Tue', 'Fri','Sun']
res=[x.upper() for x in listA]
print(res)

listA = ['Mon', 'Tue', 'Fri','Sun']
res=[ x.lower() for x in listA]
print(res)

" Reverse list of elements and print in upper case "
listb=['mon', 'tue', 'fri', 'sun']
res=[char.upper() for char in listb[ : :-1]]
print(res)

"Write a Python program to convert month name to a number of days."
month=input("PLease Enter the month:")
match(month.upper()):
    case("january"|"JANUARY"):
        print("22 {} is my birthday:".format(month))
        print("31 days are in {} month:".format(month))
    case("february"|"FEBRUARY"):
        print("28 or 29 days are in {}:".format(month))
    case("march"|"MARCH"):
        print("31 days are in {}:".format(month))
    case("april"|"APRIL"):
        print("30 days are in {}:".format(month))
    case("may"|"MAY"):
        print("31 days are in {}:".format(month))
    case("june"|"JUNE"):
        print("30 days are in {}:".format(month))
    case("july"|"JULY"):
        print("31 days are in {}:".format(month))
    case("auguest"|"AUGUEST"):
        print("31 days are in {}:".format(month))
    case("september"|"SEPTEMBER"):
        print("30 days are in {}".format(month))
    case("october "|"OCTOBER"):
        print("31 days in {}:".format(month))
    case("november"|"NOVEMBER"):
        print("30 days in {}:".format(month))
    case("DECEMBER"|"december"):
        print("31 days are in {}:".format(month))
    case _:
        print("please Enter month name  THANK YOU !")

string = "A - 13, B - 14, C - 15"
listdata=list((element.split("-") for element in string.split(",")))
print(listdata)
res=[i for i in listdata]
print(res)
for i in listdata:
    for j in i:
        print(j,end=",")
print()
print("**********line 623*****************")
"First,Last elements whose square value is between 1 and 30"
l=[]
for i in range(1,21):
    l.append(i**2)
print("first five element in list:",l[ :5])
print("last five element in list:",l[-5:])

"Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)"
lst=[1,2,3,4,5]
dict_p={}
for i in lst:
    dict_p[i]=i*i
print(dict_p)

"Remove the first occurrence of a specified element from an array."
arr=[10,20,30,40,60,45,60,10,20]
arr.remove(10)
arr.remove(20)
print(arr)

"Remove a specified item using the index from an array."
arr=[10,20,30,40,60,45,60,10,20]
arr.pop(4)
print(arr)

"Insert a new item before the second element in an existing array."
arr=[10,20,30,40,60,45,60,10,20]
arr.insert(0,100)
print(arr)
arr.insert(8,200)
print(arr)
arr.insert(-1,200)
print(arr)