h = int(input())
a = int(input())
print("The area of triangle is " , str(0.5*a*h))
print("a // b = ", str(a//h))   # toan tu chia lay phan nguyen cua a/h
print("a ^ b = ", str(a**h))    # toan tu mu a^h

x = int(input())
y = int(input())
print("x > y is", x>y)
print("x < y is", x<y)
print("x == y is", x==y)
print("x != y is", x!=y)
print("x >= y is", x>=y)
print("x <= y is", x<=y)

'''
    += : tang ve trai mot phan bang ve phai sau do gan gia tri cho ve trai
    - Tuong tu ta co the dung cho cac phep + - * /

    %= : gia tri ve trai chia lay du cho gia tri phai roi gan gia tri cho ve trai
    - Tuong tu voi phep chia lay phan nguyen va lay luy thua

    &= : Phep toan cua toan tu AND cho 2 ve sau do gan gia tri cho ve trai
    - Tuong tu voi cac phep toan OR , XOR , phep dich sang trai va sang phai
    |= : Toan tu OR
    ^= : Toan tu XOR
    >>= : Phep toan dich phai
    <<= : Phep toan dich trai
'''

print("Quy" in "Ngo Minh Quy")          # in va not in la hai toan tu membership
print("Ngo" not in "Ngo Minh Quy")      # kiem tra xem 1 xau co nam trong 1 xau khac khong 
                                        # kieu gia tri tra ve la bool
b = 5
c = 3
print(b is c)       # is va is not la hai toan tu dinh danh
print(b is not c)   # toan tu nay tuong duong voi toan tu == , kieu du lieu tra ve la bool

print("The result is",(b>c) and (b>0))
'''
    and : ket qua tra ve la true khi ca 2 dieu kien deu dung va nguoc lai
    or  : ket qua tra ve la true khi 1 trong 2 dieu kien la dung
    not : ket qua tra ve la false dieu kien la true
'''
