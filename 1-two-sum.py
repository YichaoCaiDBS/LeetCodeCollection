def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            restL = nums[:i]
            restR = nums[i+1:]
            remain = target - nums[i]
            if(remain in restL):
                return [restL.index(remain), i]
            elif(remain in restR):
                return [i, restR.index(remain) + i + 1]
        return "There is no solution."


# Python's dictionary object can be used as a hashable object.
# Consider keys as hash table, because no duplicate keys can be found
# in a dictionary.

# Put the value of input list as key and its index as value.
# When storing nums[i] into the dictionary, find whether the remain is in the list of keys.
# If not, add nums[i] into the dicitonary.
# If found, return the indexes.
# NOTE:
# The sequence of find remain and insert element into dictionary actually matters!
# Consider a list [3,2,4] and target 6.
# Insert first would cause the result to be [0,0]. They are actually the same element.
# Find first would return [1,2].
def twoSum2(nums, target):
    DICT = {}
    for i in range(len(nums)):
        remain = target - nums[i]
        if(remain in DICT.keys()):
            solution = [i, DICT[remain]]
            solution.sort()
            return solution
        DICT[nums[i]] = i
    return "There is no solution."
