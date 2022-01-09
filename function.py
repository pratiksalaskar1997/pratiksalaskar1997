
=====================================
name = ['pratik','rohit','pradeep','amol']
# print([word[0] for word in name])
# i want to initialize only worg starting with 'p':
print([word[0] for word in name if word.startswith('p')])
========================================
n1 = [10, 20, 30, 40]
n2 = [1, 4, 20, 30]
print([i for i in n1 if i  in n2])
============================
name = ['pratik','rohit','pradeep','amol']
print([(i.upper(), len(i)) for i in name  ])
==============================================

a = 0
b = 1
for i in range(1, 5):
    a += i
    print(a)
    b += i
    print(b)
==============================================
# WAP to execute dic with number as key and value as square od that number from range 1 to 10.
# expected output is : { (1: 1), (2:4),......}
print({i: i**2 for i in range(1, 11)})
====================================================
# WAP to swap the number
a = int(input('enter the value of a: '))
b = int(input('enter the value of b: '))
a, b = b, a
print('value of a after swapping: ',a)
print('value of b after swapping: ',b)
==========================================
WAP to get the expected output as:
[10, 40, 1, 4]
n1 = [10, 20, 30, 40]
n2 = [1, 20, 30, 4]
print([i for i in n1 + n2 if i not in set(n1).intersection(n2)])
=============================================================

a = 'pratikjdhejbncnc'
print('first number is: ', a[0], 'position of this word in given string: ', a.find(a[0]))
print('last number is: ', a[-1], 'position of this word in given string: ', a.find(a[-1]))
print('middle number is:', a[len(a) // 2], 'position of this word in given string: ', a.find(a[len(a) // 2]))
print('length of the string is: ', len(a))
===============================================================================================================

# WAP to process atm machine:
import time
nm = input('Enter your name: ')
p = int(input('Enter the password: '))
b = 5000
if p == 1234:
    print('its processing.....')
    time.sleep(3)
    print(' 1. mini statement.','\n','2. balance enquiry.','\n','3. withdrawal.')
    c = int(input('Enetr the number from option: '))
    if c == 1:
        print('your last five transactions are in the receipt &', b, 'is your available balance')
    elif c == 2:
        print('your balance is: ',b)
    elif c == 3:
        w = int(input('Enter the amount: '))
        if w <= b:
            print(w, 'withdrawal is successful, your balance is: ', int(b - w))
        else:
            print('Insufficient balance.')
    else:
        print('Please enter the number between 1 to 3.')
else:
    print('its processing.....')
    time.sleep(3)
    print('incorrect pin')
============================================================================================================

# expected output - [0, 30, 6, 30]

k = []
def add(*args):

    a = 0
    for val in args:
       a += val
    k.append(a)
    print('addition is: ', a)
add()
add(10, 20)
add(1, 2, 3)
add(12, 3, 4, 5, 6)
print('final list of addition is:', k)

# expected o/p --> [[10, 20, 30],[3, 4, 5],[200, 300]]
l1 = []
def sample(**k):
    for key in list(k.values()):
        l1.append(key)
sample(x1=10, x2=20, x3=30)
l2 = []
def sample(**k):
    for key in list(k.values()):
        l2.append(key)
sample(x1=3, x2=4, x3=5)
l3 = []
def sample(**k):

    for key in list(k.values()):
         l3.append(key)
sample(x1=200, x2=300)
print([l1, l2, l3])

#
# WA lambda fuction to calculate cub of a number
c = lambda x : x ** 3
cube = c(9)
print('cube of a number is', cube)

# WA lambda function to get even number
s = lambda x, y: x == y
k = s(1, 11)
print('is numbers are equal: ',k)


a1 = 'this is a sample program'
a2 = 'this is not good at all'
a = a1.split()
b = a2.split()
c = set(a).intersection(set(b))
print('common words are: ', c)

d = eval(input(print('Enter the dict: ')))
print(d)
d1 = sum(d.values())
print(d1)

s = input(print('enter the string: '))
n = input(print('Enter the word or alphabet to know no. of occurrence: '))
print('Number of occurrences in given string are: ',s.count(n))

s = input(print('enter the string: '))

d = {}
for i in s:
    d[i] = d.get(i, 0)+1
print(d)
================================================

d = {}
word = input(print('Enter the string: '))
vowel = ['a', 'e', 'i', 'o', 'u']
for x in word:
    if x in vowel:
        d[x] = d.get(x, 0)+1
for key in sorted(d):
    print(key,'present',d[key],'times')

n = int(input('Enter the number of rows: '))
for i in range(n):
    print((n-i) * '*')
#for i in range(1, n+1):
#    print(i * '*')

n = int(input('enter the number of rows: '))
for i in range(1, n):
    print(chr(64 + i) * i)

n = int(input('enter the number of rows: '))
for i in range(1, n):
    print(str(i) * (n-2))

for i in range(1, 7):
    for j in range(1, 5):
        #print(chr(64 + j), end='')
         print(i, end='')
    print()

for i in range(1, 6):
    for j in range(1, 6):
        print(i * '*')
    print()

n = int(input('enter the no. of rows: '))
for i in range(1, n):
    print((n - i) * str(i) )

def add(x, y):
    print('Addition is:', x + y)
add(10, 2)
add(1, 2)
print(123490004)
add(111, 222)
add(90, 9)

def sample(name):
    print('hello',name,'good morning')
sample('pratik')
sample('yameen sir')

def square(a):
    print('squre of', a, 'is: ',a ** 2)
square(2)
square(3)
square(123)
square(11)

def sample(name, age, salary):
    print(' your name is:', name, '\n', 'your age is: ', age, '\n', 'your salary is:', salary, '\n', '==========================')
sample('pratik', 24, 80000)
sample('yameen', 26, 180000)


nm = input('enter the name: ')


def student():
        m = 0
        for i in range(3):

                mr = int(input('enter the marks: '))

                m += mr
        print('hello', nm, 'avg of total marks of 3 subjects is: ', m/3)

student()

def sample(a, b, c):
    return c ** 2, b // 10, a * 10
n, m, p= sample(1, 2, 3)
print(n)
print(m)
print(p)

a = int(input('enter the number: '))
def test(a):
    if a % 2 == 0:
        print('number is even')
    else:
        print('number is odd')
test(a)

# WAP to get the factorial of a number given by the user

def fact(n):
    result = 1
    for i in range(n):

        result = result * (n-i)
    #print(result)
    return result
n = int(input('enter the number: '))
for i in range(n+1):
    print('factorial of', i,'is:', fact(i))

l = []
def sample(**k):
    c = []
    for i in k.values():

        #print(i)
         c.append(i)
    l.append(c)



sample(x1=10,x2=20)
sample(x1=1,x2=2,x3=3)
print(list(l))

def square(n):
    return n ** 2
print('squre of a number is: ',square(4))


n = lambda n: n ** 3
print(n(10))

add = lambda a, b: [a+b, a-b]
print(add(10, 20))

test = lambda a, b : a if a>b else b
print('biggest number is: ', test(101, 20))

avg = lambda a, b, c: (a+b+c)/3
print(avg(10,10,10))


k = eval(input('enter the list: '))
print(list(filter(lambda n:n % 2 == 0, k)))

d = ['pradeep','pratik','jyoti']
print(list(filter(lambda n:n.endswith('k'),d)))

a1 = [2, 4, 5, 6, 8]

#def div():
#    return n/2



print(list(map(lambda x:x/2,a1)))

from functools import reduce
p = [34, 33, 35, 65, 44, 18, 12, 10, 87]
print(reduce(lambda x, y: x + y, p))


# golabal variable
a = 20
def sample():
    a += 20  #This is not allowed
    print(a)
sample()


# WAP to find factorial of a number:

def fact(n):
    result = 1
    if n == 0:
             return result
    else:
        result = n * fact(n - 1)
        return  result
print(fact(6))
