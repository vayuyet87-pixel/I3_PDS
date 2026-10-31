def digit_sum(n):
    total=0
    while n>0:
        total += n % 10
        n //=10
    return total
def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return reversed_num

def is_palindrome(n):
    return n==reverse_number(n)
n=[2026,12321,9875]
for num in n:
    print(f"The sum of {num}->{digit_sum(num)},reverse digit {num}->{reverse_number(num)}")
count_palindrome=0
for i in range(10,999):
    if is_palindrome(i):
        count_palindrome+=1
print(f"The total palindrome from 10 to 999 are:{count_palindrome}")


