print("Enter your name : ")
name = input()              # khi nhap du lieu tu ban phim thi kieu du lieu cua bien do la string
print("Hello " + name)

print("Enter your age : ")
age = int(input())          # ep kieu du lieu la int cho bien truoc khi nhap
print(age)

print("In 15 years , age of " + name + " will be " + str(age + 15))

a = float(input())
b = float(input())
print("a + b = ",a+b)
print("a - b = ",a-b)
print("a * b = " + str(a*b))
print("a / b = " + str(a/b))
print("a % b = " + str(a%b))

x = int(input())
y = (input())
swap = x        # co the hoan doi cac phan tu co kieu bien khac nhau
x = y
y = swap
print("After swap : x = " +str(x) + ", y = " +str(y))

radius = float(input())
print("Circumference : " + str(2*radius*3.14))
