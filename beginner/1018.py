# 1018 - Banknotes
# https://www.beecrowd.com.br/judge/en/problems/view/1018

value = int(input())
print(value)
banknotes = [100, 50, 20, 10, 5, 2, 1]
for note in banknotes:
      count = value // note
      value %= note
      print(f"{count} nota(s) de R$ {note},00")