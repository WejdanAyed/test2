#Week2 , Day6
x = int(3.1) #x will be 3
y = int("11") #y will be 11
print(x)
print(y)
z = float(3) #z will be 3.0
f = float("11") #f will be 11.0
print(z)
print(f)
w = str (3) #w wiil be str '3'
i = str (3.1) #i wiil be str '3.1'
print(w)

#Week2 , Day7
a = """ النوع string
يعتمد على نظام unicode
وهذا يعني انك تستطيع التعامل مع النصوص
العربية والانجليزية والفرنسية.. إلخ بدون مشاكل
"""
print(a)
b= "Hello,World"
print (b[1:3])

#Week2 , Day8
V1= "Hello,World"
print(V1.strip())
print(len(V1))
print(V1.lower())
print(V1.upper())
print(V1.replace("e" , "f"))
print(V1.split (","))

#Week2 , Day9
quantity = 4
price = 29.8
itemno = 678
myorder = """ i want to pay {1}
dollars for {0}
pieces of item {2} """
print(myorder.format (quantity , price , itemno)


#Week2 , Day10
u = 12
t = 9
print( u * t)
""" h = 8
h/=2
print(h)
p = 13
l = 4
print( p < l) """


#Week2 , Day11
t = 8
print(t>5 or  t< 9)
E2 = ["A","B"]
print("C" in E2)
print("B" in E2)
code1 = ["Java" , "C#" , "Python"]
code2 = ["Java" , "C#" , "Python"]
code3 = code1
print( code1 is not code3)
print( code1 is not code2)
print( code1 != code2)


#Week2, Day12
Quiz = "Please, I want {} sandwishes and {} danutes"
print(Quzi.replace("I" , "We"))
d1 = 5
d2 = 7
print(Quzi.format(d1 , d2))
print(Quzi.upper(a))









      
