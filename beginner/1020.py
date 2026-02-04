# 1020 - Age in Days
# https://www.beecrowd.com.br/judge/en/problems/view/1020

age = int(input())
years = age // 365
months = (age % 365) // 30
days = (age % 365) % 30
print(f"{years} ano(s)")
print(f"{months} mes(es)")
print(f"{days} dia(s)")
