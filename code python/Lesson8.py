s1 = 'minhQUY2003'
s2 = 'minhquy.2003'
s3 = 'minhquy'
s4 = '2003'

print(len(s1))
# ham len() tra ve do dai cua chuoi
print(s1.lower())
# ham lower() dung de chuyen 1 chuoi ve dang thuong
print(s1.upper())
# ham upper() dung de chuyen 1 chuoi ve dang in hoa

print(s1.isalnum())
print(s2.isalnum())
# ham isalnum() dung de kiem tra xem 1 xau chi co cac ki tu chu va so hay khong

print(s3.isalpha())
print(s1.isalpha())
# ham isalpha() dung de kiemtra xem 1 chuoi chua toan cac ky tu chu ko

print(s4.isnumeric())
print(s1.isnumeric())
# ham isnumeric() dung de kiem tra xem 1 chuoi chua toan ky tu so hay khong

s5 = "Time is the harmony to let everything be graceful"
s6 = "We,don't,want,anyone,to,be,lonely"
print(s5.split(" "))
print(s6.split(","))
# ham split() dung de cat 1 chuoi ra thanh list cac chuoi khac dua tren mot phan tu trong chuoi dau vao

list1 = ["Welcome", "to" ,"Summoner's Rift"]
print(" ".join(list1))
print("-".join(list1))
# ham join() de noi 1 tap hop thanh mot chuoi su dung cac ki tu cho truoc

s7 = "L3arn Cod3 Python !"
print(s7.replace("3", "e"))

name = "Kylian Mbappe"
print(name[0])
print(name[-1])
'''
    co the lay ra 1 ki tu cua 1 chuoi theo vi tri cua no trong chuoi
    vi tri cua phan tu co the la so am nhu -1 -2 -3
    vi tri -1 la phan tu cuoi cung cua chuoi
    vi tri -2 la phan tu dung truoc phan tu cuoi cung trong chuoi
'''
print(name[0:2])
print(name[7:11])       # co the cat chuoi trong python

# nhap chuoi s8 tu ban phim va in ra 1 chuoi noi 2 ki tu dau va cuoi
s8 = input()
if len(s8) <2 :
    print("")
else:
    print(s8[0:2]+s8[-2:])

# nhap chuoi s9 s10 tu ban phim 
# doi cho 2 ky tu dau tien cua 2 chuoi cho nhau va in ra s9 + " " + s10
s9, s10 = input(), input()
swap = s9[0:2] + s10[2:]
s9 = s10[0:2] + s9[2:]
s10 = swap
print(s9 + " " + s10)

# nhap chuoi s11 tu ban phim va in ra chuoi dao nguoc
s11 = input()
list2 = s11.split(" ")
list2.reverse()
print(" ".join(list2))
