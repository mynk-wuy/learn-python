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
print("The odd number list is",answer)