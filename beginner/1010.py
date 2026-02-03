# 1010 - Simple Calculate
# https://judge.beecrowd.com/en/problems/view/1010

c1, q1, v1 = map(float,input().split())
c2, q2, v2 = map(float,input().split())

total = q1*v1+q2*v2
print(f"VALOR A PAGAR: R$ {total:.2f}")