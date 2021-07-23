import math
#Arc Sine Of 0.5
print(("The arc sine of 0.5 is ") + str(math.asin(0.5)))

#Euclidean distance between coordinate points (1 , 0) and (3 , 4)
print(("The Euclidean distance between coordinate points (1 , 0) and (3 , 4) is ") + str(math.dist([1 , 0], [3 , 4])))

#greatest common divisor of 265 and 345
print(("The greatest common divisor of 265 and 345 is ") + str(math.gcd(265 , 345)))

# Two Ways To Print The remainder of 26 divided by 8
print(("The remainder of 26 divided by 8 is ") + str(26 % 8))
print(("The remainder of 26 divided by 8 is ") + str(math.remainder(26 , 8)))


# Two ways to print (276/10) rounded down to the nearest integer 
print(("(276 / 10 ) rounded to the nearest integer is ") + str(276 // 10))
print(("(276 / 10 ) rounded to the nearest integer is ") + str(math.floor(276 // 10)))