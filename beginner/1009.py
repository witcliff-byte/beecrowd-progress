# 1009 - Salary with Bonus
# https://judge.beecrowd.com/en/problems/view/1009

seller_name =input()
salary = float(input())
sales = float(input())

final_salary = (sales*0.15)+salary
print(f"TOTAL = R$ {final_salary:.2f}")