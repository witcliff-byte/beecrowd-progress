# 1012 - Area
# https://www.beecrowd.com.br/judge/en/problems/view/1012

a, b, c = map(float, input().split())

r_triangulo = (a*c)/2
circle = 3.14159 * c**2
trapezium = ((a + b) * c)/ 2
square = b**2
rectangle = a * b

print(f"TRIANGULO: {r_triangulo:.3f}\n"
      f"CIRCULO: {circle:.3f}\n"
      f"TRAPEZIO: {trapezium:.3f}\n"
      f"QUADRADO: {square:.3f}\n"
      f"RETANGULO: {rectangle:.3f}")