# 1015 - Distance Between Two Points
# https://www.beecrowd.com.br/judge/en/problems/view/1015

p1 = input().split()
p2 = input().split()
x1, y1 = float(p1[0]), float(p1[1])
x2, y2 = float(p2[0]), float(p2[1])

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"{distance:.4f}")
