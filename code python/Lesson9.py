list1 = []
# ham tao list
def creat_list(list) :
    print("enter number of element : ")
    n = int(input())
    for i in range(n) :
        print("Enter element list["+ str(i) +"]:")
        i = float(input())
        list.append(i)
    return list

# ham tinh tong cac phan tu cua list
def sum_of_list (list):
    total = 0
    for i in list:
        total += i
    return total
print(sum_of_list([3,9,6,7]))
print(sum_of_list(creat_list(list1)))

# ham tim ra so lon nhat trong 3 so
def max_of_3numbers(a,b,c):
    if a>b & a>c:           # co the dung and hoac &
        return a
    else:
        return b if b>c else c
    
a,b,c = int(input()),int(input()),int(input())
print(max_of_3numbers(a,b,c))

# ham dem so ki tu hoa va thuong cua 1 chuoi
def count_number_of_uppercase_and_lowercase_characters(str):
    uppercase_count = 0
    lowercase_count = 0
    for i in str:                   # co the dung ham for de xac dinh tung phan tu trong chuoi
        if i.isupper():
            uppercase_count += 1
        else:
            lowercase_count += 1
    print("Number of uppercase characters :",uppercase_count)
    print("Number of lowercase characters :",lowercase_count)

print("Given string :")
str = input()
count_number_of_uppercase_and_lowercase_characters(str)

# nhap 1 list va tra ve cac so xuat hien trong list do
def get_unique_value(list):         # ham lay gia tri xuat hien trong list da cho
    answer =[]
    for i in range(len(list)):          # for i in list
        if list[i] not in answer:       # if i not in answer
            answer.append(list[i])      # answer.append(i)               
    print("The unique value list is :",answer)
print("Enter element number of list :")
n = int(input())
num1 = []
for i in range(n):
    print("Enter element num["+str(i)+"]:")
    a = int(input())
    num1.append(a)
get_unique_value(num1)

# ham kiem tra so nguyen to
def is_prime_number(number):
    for i in range(2,(int)((number+1)**(1/2))):
        if number % i == 0:
            return False
        else:
            return True
print("Enter your number :")
num2 = int(input())
print("Number "+str(num2)+" is prime number ? "+str(is_prime_number(num2)))   