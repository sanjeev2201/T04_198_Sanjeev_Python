"create a tuple. "
tp=10,20
print(tp,type(tp),id(tp),len(tp))
tp2=10,
print(tp2,type(tp2),id(tp2),len(tp2))
tp3=(10,)
print(tp3,type(tp3),id(tp3),len(tp3))

"Create a tuple with different data types"
tuplex = ("tuple", False, 3.2, 1,True,1+3j)
print(tuplex)

"create a tuple with numbers and print one item"
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
element=tuplex[1]
print(element)

"add an item in a tuple."
tp1 = (4, 6, 2, 8, 3, 1)
print(tp1,id(tp1))
tp2=tp1 + (9,)
print(tp2,id(tp2))

" convert a tuple to a string "
tuple = ('g', 'e', 'e', 'k', 's')
str=" "
for tp in tuple:
    str+=tp
print(str)

"get the 4th element and 4th element from last of a tuple"
tp=("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(tp[3],tp[-4])

"check whether an element exists within a tuple"
tp=("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
result=False
for i in tp:
    if i=="0":
        result=True
        break
if result:
    print("element is exit inside tuple")
else:
    print("element is not exit inside tuple")

"find the index of an item of a tuple."
tp=("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
for i in range(len(tp)):
    if tp[i] =="u":
        print("index of u:",i)
tp=("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
index=tp.index("u")
print("index of u:",index)

"find the length of a tuple"
tp=("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
counter=0
for i in tp:
    counter+=1
print("length of tuple element:",counter)
print("length of tuple element:",len(tp))

"convert a tuple to a dictionary"
tpdata=(10,20,25,5,15)
dict={i:i**2 for i in tpdata}
print(dict)

"unzip a list of tuples into individual lists."
"zip means value will come in the form of key-value in tuple format"
test_list = [('Akshat', 1), ('Bro', 2), ('is', 3), ('Placed', 4)]
new_list = [[i for i, j in test_list], [j for i, j in test_list]]
print(new_list)

"reverse a tuple."
tpdata=(10,20,25,5,15)
for i in tpdata[ : :-1]:
    print(i,end=" ,")
print()

"convert a list of tuples into a dictionary"
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
     ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dict={}
for i,j in tups:
    dict[i]=j
print(dict)

"replace last value of tuples in a list"
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
newl = [i[ :-1] +(100,) for i in l]
print(newl)
print("******************")
" to remove an empty tuple(s) from a list of tuples"
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
for tp in tuples:
    if len(tp)!=0:
        print(tp)
print('********************')
"sort a tuple by its float element."
tup = [('lucky', '18.265'), ('nikhil', '14.107'), ('akash', '24.541'),
    ('anand', '4.256'), ('gaurav', '10.365')]
newt1=[]
newt2=[]
for i,j in tup:
    x=float(j)
    newt1.append(i)
    newt2.append(x)
print(newt1)
print(newt2)
for i in range(len(newt2)-1,0,-1):
    for j in range(i):
        if newt2[j]>newt2[j+1]:
            newt2[j],newt2[j+1]=newt2[j+1],newt2[j]
print(newt2)
res=[(i,j) for i,j in zip(newt1,newt2)]
print(res)


tup = [('lucky', '18.265'), ('nikhil', '14.107'), ('akash', '24.541'),
    ('anand', '4.256'), ('gaurav', '10.365')]
tup.sort(key=lambda x:float(x[1]))
print("ascending order of float element:",tup)

tup = [('lucky', '18.265'), ('nikhil', '14.107'), ('akash', '24.541'),
    ('anand', '4.256'), ('gaurav', '10.365')]
tup.sort(key=lambda x:float(x[1]),reverse=True)
print("descending order of float element:",tup)