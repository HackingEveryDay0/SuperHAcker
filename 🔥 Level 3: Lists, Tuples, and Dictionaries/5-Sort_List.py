# Sort a list of random numbers without using .sort()
import random

# Generate random list
random_list = random.sample(range(1,101),5)
print("Random List Before sorting: ", random_list)


# I'll use bubble sort algo here.

for i in range(len(random_list)):
    for j in range(i, len(random_list)):
        if random_list[j] < random_list[i]:
            random_list[j], random_list[i] = random_list[i], random_list[j]
        
print("Sorted Array: ", random_list)

