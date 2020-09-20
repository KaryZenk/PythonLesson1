# 1 point
a = int(input())
b = int(input())
c = int(input())
print(a and b and c and "Нет нулевых значений!!!")  

# 2 point
print(a or b or c or "Введены все нули!")

# 3-4 point
if a > (b + c):
    print(a - b - c)
else:
    print(b + c - a) 

# 5 point
if a > 50 and (b > a or c > a):
    print("Вася")

# 6 point
if a > 5 or (b == c == 7):
    print("Петя")
