# finally a good task :)

s = "100101"

# this s is clearly a binary number we can convert it to decimal as follow
# binary =  1 0 0 1 0 1
# index =   5 4 3 2 1 0
# according to the index from right to left we apply the formula 
# so (1 * 2^0) + (0 * 2^1) + (1 * 2^2) .. 

# Time to translate this into code :)

rightPointer = len(s) - 1
result = 0
power = 0

while rightPointer >= 0:
    result += int( s[rightPointer] ) * (2**power)
    power += 1
    rightPointer -= 1

print("Binary: ", s)
print("Decimal: ", result)
