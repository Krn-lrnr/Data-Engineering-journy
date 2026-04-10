print("hello world"); print("welcome to learning python"); print("let's get started with some basic concepts")
print('im polishing it from scratch', end= ' ')
print('lets see how it goes')
print("i am 21 years old")
print("i turned", 21, "recently")

# i know python already i am just polishing everything from scratch to get fluent with it

#print("this is a comment")

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#global

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#test
x = "1"
y = "krn"

print(type(x)); print(y)

#data types

a = 1
b = 2.5
c = "hello"
d = True
e = None
f = [1, 2, 3]
g = (1, 2, 3) 
h = {"name": "Alice", "age": 30}
i = {1, 2, 3}
j = b"hello"
k = bytearray(b"hello")
l = memoryview(b"hello")
m = range(5)
n = frozenset({1, 2, 3})
o = complex(1, 2)

print(type(a)); print(type(b)); print(type(c)); print(type(d)); print(type(e)); print(type(f)); print(type(g)); print(type(h)); print(type(i)); print(type(j)); print(type(k)); print(type(l)); print(type(m)); print(type(n)); print(type(o))

# numbers types 

x = 5
y = 3.14
z = "Hello"

print(type(x)); print(type(y)); print(type(z))

q = 3.5j
print(type(q))

# conversion 

a = 1 
b = 2.5
c = 9j

x = float(a)
y = int(b)
z = complex(c) 

print(x); print(y); print(z)
print(type(x)); print(type(y)); print(type(z))

#task

x = 1

a = float(x)
b = str(x)

print(a); print(b)

#strings

a = "Hello, World!"
print(a[0:4])

for x in "banana":
  print(x)

  a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

  txt = "The best things in life are free!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[4:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])