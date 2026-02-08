import math

print("Perimeter Calculator")
print("---------------------")
print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")
print("5. Pentagon")

choice = int(input("Choose a shape (1-5): "))

if choice == 1:
    side = float(input("Enter side length: "))
    perimeter = 4 * side

elif choice == 2:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    perimeter = 2 * (length + width)

elif choice == 3:
    a = float(input("Enter side 1: "))
    b = float(input("Enter side 2: "))
    c = float(input("Enter side 3: "))
    perimeter = a + b + c

elif choice == 4:
    radius = float(input("Enter radius: "))
    perimeter = 2 * math.pi * radius

elif choice == 5:
    side = float(input("Enter side length: "))
    perimeter = 5 * side

else:
    print("Invalid choice")
    perimeter = None

if perimeter is not None:
    print(f"\nPerimeter = {perimeter:.2f}")
