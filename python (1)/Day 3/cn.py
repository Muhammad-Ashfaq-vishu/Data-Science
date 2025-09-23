# ⭐loops⭐
# loops are used to repeat instructions until a certain condition is met.

# Syntax for while loop
while count <= 10000:
    print(f"{count} I love you")
    count += 1

# Syntax for for loop
for i in range(1, 11):
    print(f"{i} I love you")

# Syntax for for loop with if,else
name = "vishu"
for char in name:
    print(char)
else:
    print("ended")

# Syntax for range function
for el in range(5):
    print(el)

# Syntax for range function with two parameters
for el in range(1, 100):
    print(el)

# Syntax for built-in functions
print(len("hello"))
print(type("hello"))

# Syntax for user-defined functions
def name_sum(a, b):
    sum = a + b
    print(sum)

name_sum(2, 10)

# Syntax for default parameters
def cat_prod(a=3, b=5):
    print(a + b)

cat_prod()

# Syntax for recursion
def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)

show(5)

