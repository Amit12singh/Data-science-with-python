# Comparison Operators
a = 10
b = 5

print("Comparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\nLogical Operators:")

x = True
y = False

print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# Combining logical and comparison operators
age = 20
has_id = True

if age >= 18 and has_id:
    print("\nAccess granted.")
else:
    print("\nAccess denied.")
