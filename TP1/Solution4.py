print("============================================")
print("int('7') + 3.5 = ", int("7") + 3.5)
print("str(10) * 3  = ", str(10) * 3)
print("bool(''), bool(' ') = ", bool(""), bool(" "))
print("int(3.99) = ", int(3.99))
print("float('1e3') = ", float("1e3"))
print("int(True) + float('2.5') = ", int(True) + float("2.5"))
print("round(2.5), round(3.5) = ", round(2.5), round(3.5))
print("type(10 / 2) = ", type(10 / 2))
print("============================================")

def safe_int(text):
    try:
        return int(float(str(text).strip()))
    except (ValueError, TypeError):
        return None
samples = ["42", "  -8  ", "3.9", "abc", ""]
for sample in samples:
    print(repr(sample), "->", safe_int(sample))

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
if num1 is not None and num2 is not None:
    print(f"The sum of {num1} and {num2} is: ", safe_int(num1) + safe_int(num2))
else:
    print("Invalid input. Please enter valid numbers.")