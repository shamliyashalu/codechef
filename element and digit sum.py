'''
nums = [1,15,6,3]
converted = str(nums)
elments_sum = sum(nums)
digit = 0
for i in nums:
    for j in str(i):
        digit = digit + int(j)
difference = elments_sum - digit
print("difference is:",difference)
'''
def finding_the_difference_Of_Sums(nums):
    element_sum = sum(nums)
    digit_sum = 0
    for num in nums:
        digit_sum += sum(int(digit) for digit in str(num))
    return abs(element_sum - digit_sum)
nums1 = [1, 15, 6, 3]
print(finding_the_difference_Of_Sums(nums1))  
nums2 = [1, 2, 3, 4]
print(finding_the_difference_Of_Sums(nums2))