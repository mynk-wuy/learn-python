list1 = [1,2,3,4,5,6]
list2 = ["Quy" , "Thai" , "Vinh" , "Hoa" , "Hoang"]
print(list2[0] , list1[3])
for name in list2:
    print(name)

list1.append(7)     # ham append : co y nghia la them phan tu 
print(list1)

# nhap cac phan tu cho list va tim gia tri nho nhat cua list
num1 = []
print("Enter the number of elements : ")
n =int(input())
min_value = 0
for i in range(n):
     print("Enter element num["+str(i)+"]:")
     i = int(input())
     num1.append(i)
     if min_value > i:
          min_value = i
print("The min value of list is",min_value)

# nhap cac phan tu cho list va tinh tong cac phan tu cua list
num2 = []
print("Enter the number of elements : ")
n =int(input())
total_value = 0
for i in range(n):
     print("Enter element num["+str(i)+"]:")
     i = int(input())
     num2.append(i)
     total_value += i
print("The total value of elements is",total_value)

list3 = [1,3,5,7,8,4,2,5,2,5,8,0,1,2,4,6,2,9]
list3.clear()                 # ham clear de xoa het tat cac phan tu

print(list3.count(2))         #  ham count dem so lan xuat hien cua 1 phan tu bat ki

list3.sort()                  # ham sort() de sap xep cac phan tu tang dan trong list
print(list3)
list3.reverse                 # ham reverse() thi nguoc lai voi sort()
print(list3)

print(len(list3))       # ham len tra ve so phan tu cua list
print(max(list3))       # ham min,max tra ve gia tri nho nhat va lon nhat trong list
print(min(list3))

list3.remove(5)         # ham remove de xoa phan tu khoi list
print(list3)
list3.pop(1)            # ham pop de xoa phan tu voi chi so cho tri cho truoc
print(list3)

vowels = ['a' , 'e' , 'i' ,'u']     # vowel : nguyen am
vowels.insert(3,'o')      # ham insert dung de them 1 phan tu vao vao 1 vi tri cua list
print(vowels)

# nhap cac phan tu cho list va in ra cac phan tu theo thu tu tang dan
num3 = []
print("Enter the number of elements : ")
n =int(input())
for i in range(n):
     print("Enter element num["+str(i)+"]:")
     i = int(input())
     num3.append(i)
     num3.sort()         
print("The list after resort is",num3)

# nhap cac phan tu cho list va in ra list chua cac so le
num4 = []
odd_num = []
print("Enter the number of elements : ")
n =int(input())
for i in range(n):
     print("Enter element num["+str(i)+"]:")
     i = int(input())
     num4.append(i)
     if i % 2 == 1:
          odd_num.append(i)
print("The odd number list is",odd_num)

# nhap cac phan tu cho list va in ra list chua cac so chia het cho 5
num5 = []
answer = []
print("Enter the number of elements : ")
n =int(input())
for i in range(n):
     print("Enter element num["+str(i)+"]:")
     i = int(input())
     num5.append(i)
     if i % 5 == 0:
          answer.append(i)
if len(answer) == 0:
          answer = [0]     
print("The list of numbers devided by 5 is",answer)
