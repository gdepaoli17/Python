# def numsZeroes(nums):
#     nums = list(nums)
#     lastNum = len(nums) - 1
    
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             # nums[i],nums[lastNum] = nums[lastNum],nums[i]
#             nums[i]=nums[lastNum]
#             nums[lastNum] = nums[i]
#             lastNum -= 1
#     return nums


# numbers = 0,1,0,3,12

# print(numsZeroes(numbers))


# Reverse something
def reverseString(data):
    
    return data[::-1]

value = input("Enter a string value: ")
print(reverseString(value))
print(len(value))