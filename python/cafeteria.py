a = int(input())
b = int(input())
c = int(input())
d = int(input())
ale = False
i = 0
while i < c:
    if i >= a and i <=b:
        ale = True
        break
    i += d
print("S" if ale else "N")