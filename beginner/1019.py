# 1019 - Time Conversion
# https://www.beecrowd.com.br/judge/en/problems/view/1019

value = int(input())
hour = value // 3600
minute = (value % 3600) // 60
second = (value % 3600) % 60
print(hour, minute, second, sep=':')