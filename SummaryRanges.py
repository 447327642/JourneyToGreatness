class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        ranges = [[nums[0]]]
        for x in nums[1:]:
            if len(ranges[-1]) == 1:
                if x == ranges[-1][0] + 1:
                    ranges[-1].append(x)
                else:
                    ranges.append([x])
            else: # len is 2
                if x == ranges[-1][1] + 1:
                    ranges[-1][1] = x
                else:
                    ranges.append([x])
        
        return ['->'.join(map(str, r)) for r in ranges]


if __name__ == '__main__':
    so = Solution()
    print so.summaryRanges([0,1,2,4,5,7])
    print so.summaryRanges([0, 3])
