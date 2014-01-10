def is_palindrome(n):
    return str(n) == str(n)[::-1]

largest_palindrome = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if i*j > largest_palindrome and is_palindrome(i*j):
            largest_palindrome = i*j

print largest_palindrome