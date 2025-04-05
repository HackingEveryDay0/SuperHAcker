# Write a function that removes duplicates from a list.

# I used two pointer strategy here

def removeDuplicates(nums) -> list:
    left, right = 0, 1

    while left < len(nums):
        while right < len(nums):
            if nums[left] == nums[right]:
                nums.pop(right)
            else:
                right += 1
        left +=1 
        right = left+1

    return nums





list_with_duplicates = [11, 10, 11, 30, 10, 50, 30, 30, 11]
print("Array Before removing duplicates: ", list_with_duplicates)
print("Array After removing duplicates: ", removeDuplicates(list_with_duplicates))