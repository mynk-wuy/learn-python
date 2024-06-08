print("Enter your GF age :")
age = int(input())
if age > 30 :
    print("Your GF is so old")
else :
    print("Your GF is so beautifull")

# 1 cach khac su dung toan tu 3 ngoi
print("Your GF is so beautifull") if age >30 else print("Your GF is old")

print("Enter any number :")
n = int(input())
if n % 2 == 0 :
    print("Ur number is a even number")
else:
    print("Ur number is a odd number")

m, n = 10 , 20
print("Both n and m are equal" if m == n 
      else 
      "m is greater than n" if m > n 
      else "n is greater than m")           # toan tu 3 ngoi

print("Enter the outside temperature :")
temperature = float(input())
if temperature >= 100:
    print("Stay at home anf enjoy ur movie")
elif temperature >= 92:
    print("Stay at home")
elif temperature == 75 :
    print("Go outside and enjoy the weather")
elif temperature < 0 :
    print("It's cool outside")
else:
    print("Let's go to school")

print("Enter x, y, z number :")
x , y ,z = int(input()) , int(input()) , int(input())
if x % 2 == 0 :
    if y >=20 :
       print("y is greater than or equal to 20")
    else :
        print("y is less than 20")
else :
    if z >= 30 :
        print("z is greater than or equal to 30")
    else:
        print("z is less than 30")

print("Enter a, b, c number :")
a, b, c = int(input()) , int(input()) , int(input())
avg = float((a+b+c)/3)
if (avg > a and avg > b):
    print("The average value is greater than both a and b")
elif (avg > a and avg > c):
    print("The average value is greater than both a and c")
elif (avg > b and avg > c):
    print("The average value is greater than both b and c")
elif (avg > a):
    print("The average value is greater than a")
elif (avg > b):
    print("The average value is greater than b") 
elif (avg > c):
    print("The average value is greater than c")

     