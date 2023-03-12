#pythagorean theorem calculator
from math import sqrt
x = 2
y = 4
h =sqrt(x*x+y*y)
print("h is equals to :" ,h)

print("Triangle with the side x, y, h")
fo = input("which side:x , y, h to be calculated:")
if fo == "h":
           x1 = int(input("Enter side x"))
           y1 = int(input("Enter side y"))
           h1 = sqrt(x1*x1 + y1*y1)
           print("h is equals to:" , h1)
