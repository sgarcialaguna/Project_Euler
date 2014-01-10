def is_pallindrome(n):
    return str(n) == str(n)[::-1]

largest_pallindrome = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if i*j > largest_pallindrome and is_pallindrome(i*j):
            largest_pallindrome = i*j

print largest_pallindrome