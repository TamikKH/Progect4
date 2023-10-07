print("ведите координаты точки A:")
x1 = int(input())
y1 = int(input())
print("ведите координаты точки B:")
x2 = int(input())
y2 = int(input())
print("ведите координаты точки C:")
x3 = int(input())
y3 = int(input())
print("ведите координаты точки D:")
x4 = int(input())
y4 = int(input())
AB = ((max(x1,x2)-min(x1,x2)) ** 2 + (max(y1,y2)-min(y1,y2)) ** 2) ** 0.5
BC = ((max(x3,x2)-min(x3,x2)) ** 2 + (max(y3,y2)-min(y3,y2)) ** 2) ** 0.5
CD = ((max(x3,x4)-min(x3,x4)) ** 2 + (max(y3,y4)-min(y3,y4)) ** 2) ** 0.5
AD = ((max(x1,x4)-min(x1,x4)) ** 2 + (max(y1,y4)-min(y1,y4)) ** 2) ** 0.5
AC = ((max(x1,x3)-min(x1,x3)) ** 2 + (max(y1,y3)-min(y1,y3)) ** 2) ** 0.5
S1 = AB**2 + BC**2 - 2*AB*BC*(AB/AC)
S2 = AD**2 + CD**2 - 2*AD*CD*(AD/AC)
print(S2+S1)