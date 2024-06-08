i = 1
n = int(input())
ans = 0
while i <= n:
    ans += i 
    i += 1
print(ans)

# vong lap while co the thay the bang cong lap for nhu sau
answer = 0
m = int(input())
for i in range(1,m+1):
    answer += i
print(answer)

a , b = int(input()), int(input())
total = 0
for i in range (a,b+1):
    if i % 2 == 1:
        total += i
print(total)

a = int(input())
ans = 1
for i in range(1,6):
    ans = a * i
    print(a,"x",i,"=",ans)

# vong lap for co the in cac ki tu trong 1 chuoi 
name = "Mynk_Wuy"
for o in name :
    print(o)        

s = input()
for o in s :
    if o != "y" :
        print(o)

# cau lenh break 
for i in range (1,10):
    if i == 5 :
        break
    print(i)

# cau lenh continue
for i in range (1,20):
    if i % 2 == 1 :
        continue
    print(i)

even = 0
odd = 0
a, b = int(input()), int(input())
for i in range(a,b+1):
    if i % 2 == 1 :
        odd += 1
    else:
        even += 1
print("Number of even and odd numbers from",a,"to",b,":",even,",",odd)

n = int(input())
answer = 0
for i in range(1,n+1):
    answer += i/(i+1)
print(round(answer,2))          # ham round de lam trong chu so sau dau phay