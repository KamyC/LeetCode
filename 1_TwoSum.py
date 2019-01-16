# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution:
    list=[]
    def twoSum(self, nums, target):
        res = []
        for i,value_i in enumerate(nums):
            temp=target-value_i
            for j, value_j in enumerate(nums[i+1:]):
                if temp==value_j :
                    res.append(i)
                    res.append(j+i+1)
                    print(res)
                    return res

s=Solution()
arr=input()
nums=[]
temp=arr[1:len(arr)-1].split(',')
for n in temp:
    nums.append(int(n))

target_str=input()
target=int(target_str)
s.twoSum(nums,target)




