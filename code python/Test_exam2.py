# nhap chuoi str tu ban phim va in ra 1 list chua cac chuoi co do dai lon hon 3
print("Enter your string :")
str = input()
list = str.split(" ")
answer = []
for i in list:
    if len(i) > 3:
        answer.append(i)
print("The words of your string with length greater than 3 :",answer) 

# nhap chuoi so num va chuyen doi cac so do thanh 1 so tu nhien roi in ra
print("Enter your length list :")
length = int(input())
num =[]
for i in range(length):
    print("Enter element num[" +str(i)+ "]:")
    i = int(input())
    num.append(str(i))

print("".join(num))

# nhap chuoi str1 tu ban phim va in ra chuoi theo dieu kien
def modify_string(str):
    if len(str) >= 3:
        if str[-3:] != "ing":
             str = str + "ing"
        else:
             str = str + "ly"  
    return str
print("Enter your string :")
str1=input()
print("Your string after checking is "+modify_string(str1))

# nhap so nguyen duong n va in ra tong tat ca cac uoc so nguyen duong khac n :
print("Enter your number :")
n = int(input())
total = 0
for i in range(1,abs(n)):
    if n % i == 0:
        total += i
print(f"Sum of divisors of {n} is {total}")

# nhap so nguyen duong n va kiem tra so do co phai so abundant ko
print("Enter your number :")
n = int(input())
def is_abundant_number(n):      # so abudant la so co tong cac uoc lon hon so do
    total = 0
    for i in range(1,abs(n)):
        if n % i == 0:
            total += i
    if total > n:
        return True
    else:
        return False
print(f"Number {n} is abundant number ? {is_abundant_number(n)}")