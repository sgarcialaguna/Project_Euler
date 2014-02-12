sumOfSquares = 0
squaredSums = 0

for i in range(1,101):
    sumOfSquares += i**2
    squaredSums += i

squaredSums **= 2


print sumOfSquares, squaredSums, sumOfSquares - squaredSums
