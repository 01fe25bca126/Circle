import sys

if len(sys.argv) > 1:
    radius = float(sys.argv[1])
else:
    radius = 5

area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius

print("Radius:", radius)
print("Area of circle:", area)
print("Circumference of circle:", circumference)
