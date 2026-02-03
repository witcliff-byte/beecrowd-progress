# 1008 - Salary
# https://judge.beecrowd.com/en/problems/view/1008


emp_number = int(input())
worked_hours = int(input())
amount_per_hour = float(input())

salary= worked_hours * amount_per_hour
print(f"NUMBER = {emp_number}\nSALARY = U$ {salary:.2f}")