'''
def demo(*args):
    print(args)
demo()
demo(1)
demo(1,2,3,7+8j,True,False)
demo(1,2,3,7+8j,True,False,[1,2,3],{56,89},{5:90},'abc')
print()
print("after the *args uses in the Place of statement")
print()

def demo(*args):
    print(*args)
demo()
demo(1)
demo(1,2,3,7+8j,True,False)
demo(1,2,3,7+8j,True,False,[1,2,3],{56,89},{5:90},'abc')
'''
"""
Note :---->1
if we use *args in the Place of statement will get
the output in unpacked format

Note:---->2
if we use args in the Place of statement will get
the output in packed format
"""

"""
keyword arguments
Variable keyword arguments (**kwargs)
"""

'''
#keyword arguments----->Parameter=argument
def spam(a,b,c):
    print(a,b,c)
spam(a=10,b=20,c=30)
# spam(a=10,b=20#Error
# spam(a=10) Error
spam()
'''
'''
def spam(a,b,c):
    print(a,b,c)
# spam(a=10,b=20,30)#SyntaxError: positional argument follows keyword argument
spam(10,b=20,c=30)
'''

'''
#Variable keyword arguments (**kwargs)

def check(**kwargs):
    print(kwargs)
check()
check(x=900)
check(x=900,y="abc",z=[1,2,3],t={34,89},u={23:89})
check(x1=1000)

print()

def check(**kwargs):
    print(*kwargs)
check()
check(x=900)
check(x=900,y="abc",z=[1,2,3],t={34,89},u={23:89})
check(x1=1000)
'''
'''
#combination of *args and **kwargs

def Both_data(*args,**kwargs):
    print(args,kwargs)
Both_data()
Both_data(1,2,3)
Both_data(1,2,3,a=90,b=[1,2,3])
'''

'''
#ONLY POSITIONAL ARGUMENT(/)
def show(a,b,/,c):
    print(a,b,c)
show(1,2,3)
show(100,200,c=900)
show(a=100,300,400)
'''

'''
#only keyword argument (*)
def demo(a,b,*,c,d):
    print(a,b,c,d)

demo(100,200,c=900,d=1000)
# demo(100,300,c=900,1000) #Error
demo(a=100,b=200,c=900,d=123)
demo(100,b=200,c=900,d=123)
demo(100,b=200,c=900,123)
'''
'''
#combination of / and *
def Think(a,b,/,c,*,d,e):
    print(a,b,c,d,e)
Think(10,20,30,d=900,e="Hii")
Think(1,2,c=3,d=4,e=90)
# Think(1,b=2,c=3,d=9,e=1234) #Error
Think(1,2,3,4,5,6)
'''

"""
1.Positional argumnet
2.variable_Positional argumnet (*args)

3.keyword argumnets
4.variable_keyword argumnets(**kwargs)

5.only_Positional_argument(/)
6.only_keyword_arguments(*)

7.combination of *args and **kwargs
8.combination of / and *

"""

# def Check():
#     name="Python"
#     print(name)
# Check()
# print(name)




'''
def check():
    x=9000
    return x
t=check()
print(t)

def check():
    x=9000
    return x
print(check())
'''

'''
def Operations(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    print(a,b,c,d)
Operations(10,5)
'''

'''
def Operations(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    return a
    return b
    return c
    return d
w=Operations(10,5)
print(w)
'''
'''
def Operations(x,y):
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    return a,b,c,d
w=Operations(10,5)
print(w)
'''
'''
def Operations(x,y):
    return x+y,x-y,x*y,x/y,x//y,x%y
w=Operations(10,5)
print(w)
'''


'''
def HII():
    y=10  #------>Local_variable
    y=y+90
    print(y)
HII()
'''
# print(y)  #Name error

#
# def HII():
#     y=10  #------>Local_variable
#     y=y+190
#     return y
# print(HII())







'''
a=100  #Global_Varibale
def Last_Part():
    b=900  #local_variable
    print(a)
Last_Part()
print(a)
'''
'''
#global variable Modification outside
a=100  #Global_Varibale
def Last_Part():
    print(a)
Last_Part()
a=a+400  #a--->100 ----> 100=100+400
print(a)
'''
'''
#Global variable Modification inside the function

a=100  #Global_Varibale
def Last_Part():
    global a
    a=a+900
    print(a)
Last_Part()
'''
'''
x=10
def outer():
    y=20
    print(x)
    print(y)
    def inner():
        z=30
        print(x)
        print(y)
        print(z)
    inner()
    print(y)
    print(x)
    # print(z)
outer()
print(x)
# print(y)
# print(z)
'''

'''
x=10
def outer():
    y=20
    def inner():
        nonlocal y
        y=y+80
        print(y)
        z=30
    inner()
outer()
'''



'''
a=10
def First():
    global a
    a=a+190
    b=30
    print(a)
    print(b)
    def second():
        nonlocal b
        b=b+470
        print(b)
        c=40
        c=c+60
        print(c)
        print(a)
        print(b)
    second()
    print(a)
    print(b)
First()
print(a)
'''




'''
#wap to print 0 to 30 odd number and show me
#in side the list

def Number():
    k=[]
    for i in range(0,31):
        if i%2==1:
            k.append(i)
    print(k)
Number()
print()
def Number():
    k=[]
    for i in range(0,31):
        if i%2==1:
            k.append(i)
    return k
q=Number()
print(q)
'''



'''
y="Good luck"
d={}
for i in y:
    d[i]=ord(i)
print(d)
print()

y="Good luck"
d={}
for i in y:
    d.update({i:ord(i)})
print(d)
print()


def Data(y):
    e={}
    for i in y:
        e[i]=ord(i)             #e{"G"}
    print(e)
Data("Good luck")

print()



def Data(y):
    e={}
    for i in y:
        e[i]=ord(i)             #e{"G"}
    return e
w=Data("Good luck")
print(w)


'''

'''
w=["Python","Java","SQL","POWERBI","EXCEL"]
#o/p------> 0,"Python" ,1,"Java".........

def Check(w):
    for i in enumerate(w):
        print(i)
Check(["Python","Java","SQL","POWERBI","EXCEL"])

print()

def Check(w):
    for i,j in enumerate(w):
        print(i,j)
Check(["Python","Java","SQL","POWERBI","EXCEL"])

print()

def Check(w):
    for i in range(len(w)):
        print(i,w[i])  #var_name[Position]
Check(["Python","Java","SQL","POWERBI","EXCEL"])
'''
'''
s=[1,4,"Hello",5+4j,True,False,2.3,[1,2,3]]
def Total_Data(s):
    total = 0
    for i in s:
        if isinstance(i, (int, float, complex, bool)):
            total = total + i
    print(total)
Total_Data([1,4,"Hello",5+4j,True,False,2.3,[1,2,3]])


print()

total = 0
def Total_Data(s):
    global total
    for i in s:
        if isinstance(i, (int, float, complex, bool)):
            total = total + i
    print(total)
Total_Data([1,4,"Hello",5+4j,True,False,2.3,[1,2,3]])
'''

'''
#wap to Print sum of 1 to 10 Number
def Total():
    sum=0
    for i in range(1,11):
        sum=sum+i
    print(sum)
Total()

a=["walmart","kickout","punchout","lovely",
   "Thought"]

def show(a):
    d={}
    for i in a:
        d[i]=len(i)
    print(d)
show(["walmart","kickout","punchout","lovely",
   "Thought"])

'''
a=["walmart","kickout","punchout","lovely",
   "Thought"]

def Check(a):
    d={}
    for i in a:
        if len(i)%2==0:
            d[i]=i
        else:
            d[i]=i[::-1]
    print(d)
Check(a)

