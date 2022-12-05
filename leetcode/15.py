class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # sort the array
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            # print(i, nums[i])
            if i>0 and nums[i] == nums[i-1]:
                continue
            # then same as TwoSum (two pointers) or TwoSum (hashmap)
            left, right = i + 1, len(nums) - 1

            while left < right:
                triplet_sum = nums[i] + nums[left] + nums[right]

                if triplet_sum > 0:
                    right -= 1
                elif triplet_sum < 0:
                    left += 1
                else:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return triplets