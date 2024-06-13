# nhap 1 list res tu ban phim chua cac phan tu int va in ra ket qua 1 list cac so chan
Res = []
print("Enter element number of Res:")
n = int(input())
for i in range(n) :
    print("Enter element Res[" +str(i)+ "]:")
    i = int(input())
    Res.append(i)

def creat_even_number_list(list):
    even_number_list = []
    for i in list:
        if i%2 == 0 :
            even_number_list.append(i)
    print("The even number list is : ",even_number_list)
creat_even_number_list(Res)

# nhap hai so a va b roi tinh a^b
print("Enter number a ,b :")
a,b = int(input()),int(input())
def power(a,b):
    if b==0 :
        return 1
    else :
        return a * power(a,b-1)
answer = power(a,b)
print(f"{a} power {b} equal {answer} ")

# nhap 2 so a,b roi tim uoc chung lon nhat cua 2 so
print("Enter number a ,b :")
a,b = int(input()),int(input())
def GCD(a,b):           # ham tim uoc chung lon nhat
    if b == 0 :
        return a
    else :
        return GCD(b,a%b)   # goi de quy voi b va phan du cua a chia b
answer = GCD(a,b)
print(answer)

# nhap so do 3 canh cua 1 tam giac va xac dinh tam giac do la tam giac gi
def determine_triangle(a,b,c):
    if a == b & b == c :
        return  "Equilateral triangle"
    elif a == b or b == c :
        return "Isosceles triangle"
    else :
        return "Scalene triangle"
print("Enter length of 3 angles of the triangle :")
a,b,c = int(input()),int(input()),int(input())
print("The triangle  you entered is a "+determine_triangle(a,b,c))